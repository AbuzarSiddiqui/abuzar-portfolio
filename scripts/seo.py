# Adds canonical URLs, social cards, icons and JSON-LD structured data to every page,
# and writes sitemap.xml + robots.txt. Idempotent: re-run after any page change.
# Run from the site root:  python scripts/seo.py   (build_courses.py runs it automatically)
import datetime, glob, html, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))

SITE = 'https://www.abuzarsiddiqui.in'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERSON_ID, SITE_ID = SITE + '/#person', SITE + '/#website'
LINKEDIN, GITHUB = 'https://www.linkedin.com/in/abuzarahmedsiddiqui/', 'https://github.com/abuzarsiddiqui'
NOINDEX = {'certificate.html'}  # per-learner pages built from the URL fragment

PERSON = {
    '@type': 'Person', '@id': PERSON_ID,
    'name': 'Abuzar Ahmed Siddiqui', 'alternateName': ['Abuzar Siddiqui', 'Abuzar A. Siddiqui'],
    'givenName': 'Abuzar', 'additionalName': 'Ahmed', 'familyName': 'Siddiqui',
    'url': SITE + '/', 'image': SITE + '/abuzar-siddiqui.jpg',
    'jobTitle': 'AI Product Manager',
    'description': 'AI Product Manager building agentic AI and SaaS products from 0 to 1.',
    'worksFor': {'@type': 'Organization', 'name': 'N Force One', 'url': 'https://www.nforceone.com'},
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Hyderabad', 'addressRegion': 'Telangana', 'addressCountry': 'IN'},
    'alumniOf': [
        {'@type': 'CollegeOrUniversity', 'name': 'Jawaharlal Nehru Engineering College, MGM University', 'address': 'Aurangabad, Maharashtra, India'},
        {'@type': 'Organization', 'name': 'Harvard Project for Asian and International Relations (HPAIR)'},
    ],
    'hasCredential': [{'@type': 'EducationalOccupationalCredential', 'credentialCategory': 'degree', 'name': 'B.Tech in Computer Science & Engineering'}],
    'knowsAbout': ['Product management', 'AI product management', 'Agentic AI', 'Generative AI', 'B2B SaaS', 'Product strategy', 'Product discovery', 'Agile delivery', 'Claude Code', 'AI APIs'],
    'sameAs': [LINKEDIN, GITHUB],
}
WEBSITE = {'@type': 'WebSite', '@id': SITE_ID, 'url': SITE + '/', 'name': 'Abuzar Ahmed Siddiqui',
           'alternateName': ['Abuzar Siddiqui', 'abuzarsiddiqui.in'], 'inLanguage': 'en', 'publisher': {'@id': PERSON_ID}}

def git_date(path, first=False):
    args = ['git', 'log', '--format=%cs'] + (['--diff-filter=A', '--follow'] if first else ['-1']) + ['--', path]
    out = subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.split()
    return (out[-1] if first else out[0]) if out else datetime.date.today().isoformat()  # uncommitted: today

def meta(s, name, attr='name'):
    m = re.search(rf'<meta {attr}="{re.escape(name)}" content="([^"]*)"', s)
    return html.unescape(m.group(1)) if m else ''

def title_of(s):
    return html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())

def crumbs(*items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i, 'name': n, 'item': SITE + '/' + u} for i, (n, u) in enumerate(items, 1)]}

def structured(path, s, url):
    from courses_content import COURSES
    from build_courses import duration
    by_slug = {c['slug']: c for c in COURSES}
    page = {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title_of(s),
            'description': meta(s, 'description'), 'isPartOf': {'@id': SITE_ID}, 'about': {'@id': PERSON_ID}, 'inLanguage': 'en'}
    graph = [WEBSITE, PERSON]
    if path == 'index.html':
        page['@type'] = 'ProfilePage'; page['mainEntity'] = {'@id': PERSON_ID}
        page['dateModified'] = git_date(path)
    elif path.startswith('notes/'):
        h1 = html.unescape(re.sub('<[^>]+>', '', re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1)))
        graph.append({'@type': 'BlogPosting', '@id': url + '#article', 'headline': h1, 'description': meta(s, 'description'),
                      'url': url, 'mainEntityOfPage': url, 'image': SITE + '/og-image.jpg', 'inLanguage': 'en',
                      'datePublished': git_date(path, True), 'dateModified': git_date(path),
                      'author': {'@id': PERSON_ID}, 'publisher': {'@id': PERSON_ID}})
        graph.append(crumbs(('Home', ''), ('Writing', 'blog.html'), (h1, path)))
    elif path.startswith('courses/'):
        c = by_slug[os.path.basename(path)[:-5]]
        hours = float(duration(c).split()[0])
        graph.append({'@type': 'Course', '@id': url + '#course', 'name': c['title'], 'description': c['subtitle'], 'url': url,
                      'provider': {'@id': PERSON_ID}, 'creator': {'@id': PERSON_ID}, 'inLanguage': 'en',
                      'educationalLevel': c['level'], 'teaches': c['skills'], 'isAccessibleForFree': True,
                      'educationalCredentialAwarded': 'Certificate of completion',
                      'offers': {'@type': 'Offer', 'category': 'Free', 'price': 0, 'priceCurrency': 'USD'},
                      'hasCourseInstance': {'@type': 'CourseInstance', 'courseMode': 'Online', 'courseWorkload': f'PT{int(hours * 60)}M'}})
        graph.append(crumbs(('Home', ''), ('Courses', 'courses.html'), (c['title'], path)))
    elif path == 'courses.html':
        graph.append({'@type': 'ItemList', 'name': 'Free AI courses by Abuzar Ahmed Siddiqui', 'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'url': f'{SITE}/courses/{c["slug"]}.html'} for i, c in enumerate(COURSES, 1)]})
        graph.append(crumbs(('Home', ''), ('Courses', 'courses.html')))
    elif path == 'blog.html':
        posts = re.findall(r'href="(notes/[^"]+\.html)"', s)
        graph.append({'@type': 'ItemList', 'name': 'Writing by Abuzar Ahmed Siddiqui', 'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'url': f'{SITE}/{p}'} for i, p in enumerate(dict.fromkeys(posts), 1)]})
        graph.append(crumbs(('Home', ''), ('Writing', 'blog.html')))
    else:
        graph.append(crumbs(('Home', ''), (title_of(s).split(' — ')[0], path)))
    graph.insert(2, page)
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))

def process(path):
    full = os.path.join(ROOT, path)
    s = open(full, encoding='utf-8').read()
    prefix = '../' * path.count('/')
    url = SITE + '/' + ('' if path == 'index.html' else path)
    # Drop anything a previous run (or the page) set, so the block below is the single source.
    s = re.sub(r'\s*<!-- seo -->.*?<!-- /seo -->', '', s, flags=re.S)
    s = re.sub(r'\s*<meta property="og:(image|url|site_name|locale)"[^>]*>', '', s)
    title, desc = title_of(s), meta(s, 'description')
    tags = [f'<link rel="canonical" href="{url}">'] if path not in NOINDEX else ['<meta name="robots" content="noindex, follow">']
    tags += [
        f'<meta name="author" content="Abuzar Ahmed Siddiqui">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:site_name" content="Abuzar Ahmed Siddiqui">',
        f'<meta property="og:locale" content="en_IN">',
        f'<meta property="og:image" content="{SITE}/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Abuzar Ahmed Siddiqui, AI Product Manager">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{SITE}/og-image.jpg">',
        f'<link rel="icon" href="{prefix}favicon.ico" sizes="48x48"><link rel="icon" href="{prefix}icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">',
    ]
    if 'og:type' not in s:
        tags.append(f'<meta property="og:type" content="{"profile" if path == "index.html" else "website"}">')
    if 'og:title' not in s:
        tags.append(f'<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">')
    if path not in NOINDEX:
        tags.append(f'<script type="application/ld+json">{structured(path, s, url)}</script>')
    block = '\n  <!-- seo -->\n  ' + '\n  '.join(tags) + '\n  <!-- /seo -->'
    s = s.replace('\n</head>', block + '\n</head>', 1)
    open(full, 'w', encoding='utf-8', newline='\n').write(s)
    return url

def main():
    pages = sorted(['index.html'] + [p for p in glob.glob('*.html', root_dir=ROOT) if p != 'index.html' and not p.startswith('google')]
                   + [p.replace('\\', '/') for p in glob.glob('notes/*.html', root_dir=ROOT) + glob.glob('courses/*.html', root_dir=ROOT)])
    entries = []
    for p in pages:
        url = process(p)
        if p not in NOINDEX:
            pri = '1.0' if p == 'index.html' else '0.8' if p in ('courses.html', 'blog.html') or p.startswith('courses/') else '0.7'
            entries.append(f'  <url><loc>{url}</loc><lastmod>{git_date(p)}</lastmod><priority>{pri}</priority></url>')
    entries.sort(key=lambda e: e.find('<loc>' + SITE + '/</loc>') < 0)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(entries) + '\n</urlset>\n')
    open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n').write(
        f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    print(f'seo: {len(pages)} pages, {len(entries)} in sitemap')

if __name__ == '__main__':
    main()
