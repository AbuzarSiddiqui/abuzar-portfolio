# Builds courses.html, courses/<slug>.html and certificate.html from courses_content.py.
# Run from the site root:  python scripts/build_courses.py
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from courses_content import COURSES

PASS = 80  # quiz pass mark, percent
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape

def head(title, desc, prefix):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <script>document.documentElement.classList.add('js');try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
  <link rel="stylesheet" href="{prefix}styles.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="nav"><div class="wrap">
    <a class="brand" href="{prefix}index.html"><span class="mark">A</span>Abuzar Siddiqui</a>
    <nav class="links" aria-label="Primary"><a href="{prefix}index.html#work">Work</a><a href="{prefix}index.html#approach">Approach</a><a href="{prefix}index.html#experience">Experience</a><a href="{prefix}blog.html">Writing</a><a href="{prefix}courses.html" aria-current="page">Courses</a><a href="{prefix}education.html">Education</a></nav>
    <div class="nav-end">
      <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 2a6 6 0 0 1 0 12z" fill="currentColor"/></svg></button>
      <a class="btn primary small" href="{prefix}contact.html">Get in touch</a>
    </div>
  </div></header>
'''

def foot(prefix, extra=''):
    return f'''
  <footer><div class="wrap"><span>© 2026 Abuzar Ahmed Siddiqui</span><nav aria-label="Footer"><a href="https://linkedin.com/in/abuzarahmedsiddiqui" target="_blank" rel="noreferrer">LinkedIn</a><a href="https://github.com/abuzarsiddiqui" target="_blank" rel="noreferrer">GitHub</a><a href="{prefix}contact.html">Contact</a></nav></div></footer>
  <script src="{prefix}site.js"></script>{extra}
</body>
</html>
'''

def count_lessons(c): return sum(len(m['lessons']) for m in c['modules'])

def duration(c):
    # Reading time plus ~10 min for the quiz, rounded to the nearest half hour.
    mins = sum(l['minutes'] for m in c['modules'] for l in m['lessons']) + 10
    h = max(0.5, round(mins / 30) / 2)
    return f"{h:g} hour" + ("" if h == 1 else "s")

def thumb(c, big=False):
    return f'<div class="thumb{" big" if big else ""}" style="--hue:{c["hue"]}" aria-hidden="true"><span>{c["glyph"]}</span></div>'

def course_page(c):
    n = count_lessons(c)
    syllabus, body, i = [], [], 0
    for mi, m in enumerate(c['modules'], 1):
        items = []
        body.append(f'<h2 class="module-title" id="m{mi}"><span class="eyebrow accent">Module {mi}</span>{e(m["title"])}</h2>')
        for li, l in enumerate(m['lessons'], 1):
            i += 1
            lid = f'l{i}'
            items.append(f'<li><a href="#{lid}"><span class="tick" aria-hidden="true"></span>{e(l["title"])}<small>{l["minutes"]} min</small></a></li>')
            take = ''.join(f'<li>{e(t)}</li>' for t in l['takeaways'])
            body.append(f'''<article class="lesson reveal" id="{lid}">
          <div class="eyebrow">Lesson {i} of {n} · {l["minutes"]} min read</div>
          <h3 class="lesson-title">{e(l["title"])}</h3>
          <div class="prose">{l["body"]}</div>
          <div class="takeaways"><b>Key takeaways</b><ul>{take}</ul></div>
          <button class="btn small mark" type="button">Mark lesson complete</button>
        </article>''')
        syllabus.append(f'<li><b>Module {mi} · {e(m["title"])}</b><ol>{"".join(items)}</ol></li>')
    quiz = []
    for qi, q in enumerate(c['quiz'], 1):
        opts = ''.join(f'<label><input type="radio" name="q{qi}" value="{oi}" required> {e(o)}</label>' for oi, o in enumerate(q['o']))
        quiz.append(f'<fieldset class="q" data-answer="{q["a"]}"><legend><span>{qi}.</span> {e(q["q"])}</legend>{opts}</fieldset>')
    outcomes = ''.join(f'<li>{e(o)}</li>' for o in c['outcomes'])
    skills = ''.join(f'<span class="pill">{e(s)}</span>' for s in c['skills'])
    total_min = sum(l['minutes'] for m in c['modules'] for l in m['lessons'])
    return head(f'{c["title"]} — Free course by Abuzar Ahmed Siddiqui', c['subtitle'], '../') + f'''
  <main id="main" data-course="{c["slug"]}" data-pass="{PASS}">
    <section class="course-hero"><div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="../courses.html">Courses</a> / <span>{e(c["title"])}</span></nav>
      <div class="course-hero-grid">
        <div>
          <div class="eyebrow accent">{c["level"]} · {duration(c)} · {len(c["modules"])} modules · {n} lessons</div>
          <h1 class="display">{e(c["title"])}</h1>
          <p class="lede">{e(c["subtitle"])}</p>
          <div class="tags" style="margin-top:20px">{skills}</div>
          <div class="actions"><a class="btn primary" href="#l1">Start learning <span class="arr">→</span></a><a class="btn" href="#certificate">Get the certificate</a></div>
        </div>
        <aside class="course-card">
          {thumb(c, True)}
          <ul class="facts">
            <li><b>Free</b><span>No sign-up needed</span></li>
            <li><b>{total_min} min</b><span>of reading across {n} lessons</span></li>
            <li><b>Final quiz</b><span>{len(c["quiz"])} questions · pass at {PASS}%</span></li>
            <li><b>Certificate</b><span>of completion, shareable on LinkedIn</span></li>
          </ul>
          <div class="progress"><div class="bar"><i data-progress-bar></i></div><span data-progress-text>0 of {n} lessons · 0%</span></div>
        </aside>
      </div>
    </div></section>

    <div class="wrap">
      <section class="learn reveal"><h2 class="display">What you’ll learn</h2><ul class="checks">{outcomes}</ul></section>
      <div class="course-body">
        <aside class="syllabus" aria-label="Syllabus">
          <div class="eyebrow">Syllabus</div>
          <ol>{"".join(syllabus)}<li><b>Finish</b><ol><li><a href="#assessment"><span class="tick" aria-hidden="true"></span>Final assessment</a></li><li><a href="#certificate"><span class="tick" aria-hidden="true"></span>Certificate</a></li></ol></li></ol>
          <div class="progress"><div class="bar"><i data-progress-bar></i></div><span data-progress-text></span></div>
        </aside>
        <div class="course-main">
          {"".join(body)}

          <section class="assessment" id="assessment">
            <h2 class="module-title"><span class="eyebrow accent">Final assessment</span>Check your understanding</h2>
            <p class="muted">Answer all {len(c["quiz"])} questions. You need {PASS}% to pass, and you can retake it as often as you like.</p>
            <form id="quiz">{"".join(quiz)}<button class="btn primary" type="submit">Submit answers</button><p id="quiz-result" class="quiz-result" role="status" hidden></p></form>
          </section>

          <section class="cert-box" id="certificate">
            <h2 class="module-title"><span class="eyebrow accent">Certificate</span>Earn your certificate</h2>
            <ul class="reqs"><li id="cert-lessons">Complete all {n} lessons</li><li id="cert-quiz">Pass the final assessment ({PASS}%+)</li></ul>
            <p id="cert-locked" class="muted">Finish both steps above to unlock your certificate of completion.</p>
            <form id="cert-form" hidden>
              <label for="cert-name">Your full name, as it should appear on the certificate</label>
              <div class="cert-row"><input id="cert-name" required maxlength="80" autocomplete="name" placeholder="e.g. Priya Sharma"><button class="btn primary" type="submit">Generate certificate</button></div>
              <p class="hint">Your progress is saved in this browser only. Nothing is sent to a server.</p>
            </form>
          </section>

          <section class="instructor">
            <img src="../abuzar-siddiqui-headshot.jpg" alt="" width="72" height="72" loading="lazy">
            <div><div class="eyebrow">Your instructor</div><b>Abuzar Ahmed Siddiqui</b><p class="muted">AI Product Manager building agentic AI and SaaS products. Creator of the AI PM Agent.</p></div>
            <a class="btn small li-follow" href="https://www.linkedin.com/in/abuzarahmedsiddiqui/" target="_blank" rel="noreferrer">Follow on LinkedIn ↗</a>
          </section>
        </div>
      </div>
    </div>
  </main>
''' + foot('../', '\n  <script src="../courses.js"></script>')

def catalog():
    cards = []
    for c in COURSES:
        cards.append(f'''<a class="ccard reveal" href="courses/{c["slug"]}.html">
          {thumb(c)}
          <div class="ccard-body">
            <div class="eyebrow">{c["level"]} · {duration(c)}</div>
            <h3>{e(c["title"])}</h3>
            <p>{e(c["subtitle"])}</p>
            <div class="ccard-meta"><span>{len(c["modules"])} modules · {count_lessons(c)} lessons</span><span class="state live">CERTIFICATE</span></div>
          </div>
        </a>''')
    return head('Courses — Abuzar Ahmed Siddiqui', 'Free, practical courses on AI, AI APIs, token optimisation, Claude Code and AI product management, with certificates of completion.', '') + f'''
  <main id="main"><div class="wrap">
    <section class="page-hero reveal">
      <div class="eyebrow accent">Free courses</div>
      <h1 class="display">Learn AI, <em>practically</em>.</h1>
      <p class="lede">Short, practical courses for product people and builders — from AI foundations to APIs, cost optimisation and shipping AI products. Free, self-paced, with a certificate of completion.</p>
    </section>
    <ol class="how reveal">
      <li><b>01</b><span>Read the lessons at your own pace</span></li>
      <li><b>02</b><span>Pass the final assessment ({PASS}%+)</span></li>
      <li><b>03</b><span>Get a certificate you can add to LinkedIn</span></li>
    </ol>
    <section class="catalog" style="padding-top:48px">{"".join(cards)}</section>
    <p class="hint" style="padding-bottom:96px">Certificates are certificates of completion issued by Abuzar Ahmed Siddiqui. They are not accredited qualifications.</p>
  </div></main>
''' + foot('')

def certificate():
    titles = {c['slug']: c['title'] for c in COURSES}
    hours = {c['slug']: duration(c) for c in COURSES}
    return head('Certificate of Completion — Abuzar Ahmed Siddiqui', 'Certificate of completion for a course by Abuzar Ahmed Siddiqui.', '') + '''
  <main id="main"><div class="wrap cert-page">
    <div id="cert-error" class="page-hero" hidden><h1 class="display">Certificate not found.</h1><p class="lede">This link looks incomplete. <a class="link" href="courses.html">Browse the courses →</a></p></div>
    <div id="cert-view" hidden>
      <div class="certificate" id="cert">
        <div class="cert-top"><span class="brand"><span class="mark">A</span>Abuzar Siddiqui</span><span class="eyebrow">Certificate ID <b id="c-id"></b></span></div>
        <div class="eyebrow accent">Certificate of completion</div>
        <p class="cert-small">This certifies that</p>
        <h1 class="display" id="c-name"></h1>
        <p class="cert-small">has successfully completed the course</p>
        <h2 id="c-course"></h2>
        <p class="cert-small" id="c-meta"></p>
        <div class="cert-foot">
          <div><span class="sig">Abuzar Ahmed Siddiqui</span><span class="cert-small">Course author · AI Product Manager</span></div>
          <div class="seal" aria-hidden="true">✦</div>
          <div style="text-align:right"><b id="c-date"></b><span class="cert-small">abuzarsiddiqui.in/courses</span></div>
        </div>
      </div>
      <div class="actions cert-actions">
        <button class="btn primary" onclick="print()">Download as PDF</button>
        <a class="btn li-follow" id="c-linkedin" target="_blank" rel="noreferrer">Add to LinkedIn profile ↗</a>
        <button class="btn" id="c-copy">Copy certificate link</button>
        <a class="btn" id="c-back">Back to course</a>
      </div>
      <p class="hint">Certificate of completion issued by Abuzar Ahmed Siddiqui. Not an accredited qualification. Use “Download as PDF” and choose “Save as PDF” in the print dialog.</p>
    </div>
  </div></main>
''' + foot('', '''
  <script>
    const TITLES = ''' + json.dumps(titles) + ''', HOURS = ''' + json.dumps(hours) + ''';
    // Details live in the URL fragment (#c=..&n=..&d=..), which is never sent to the server.
    const p = new URLSearchParams(location.hash.slice(1)), c = p.get('c'), n = (p.get('n') || '').trim(), d = p.get('d') || '';
    if (!TITLES[c] || !n || !/^\\d{4}-\\d{2}-\\d{2}$/.test(d)) document.getElementById('cert-error').hidden = false;
    else {
      // FNV-1a hash → short, stable ID for this name + course + date.
      let h = 2166136261; for (const ch of c + '|' + n + '|' + d) { h ^= ch.codePointAt(0); h = Math.imul(h, 16777619) >>> 0; }
      const id = 'AS-' + h.toString(36).toUpperCase().padStart(7, '0');
      const date = new Date(d + 'T00:00:00');
      const $ = x => document.getElementById(x);
      $('c-name').textContent = n; $('c-course').textContent = TITLES[c]; $('c-id').textContent = id;
      $('c-meta').textContent = 'A self-paced course · ' + HOURS[c] + ' · final assessment passed';
      $('c-date').textContent = date.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
      $('c-back').href = 'courses/' + c + '.html';
      $('c-linkedin').href = 'https://www.linkedin.com/profile/add?' + new URLSearchParams({ startTask: 'CERTIFICATION_NAME', name: TITLES[c], organizationName: 'Abuzar Ahmed Siddiqui', issueYear: date.getFullYear(), issueMonth: date.getMonth() + 1, certUrl: location.href, certId: id });
      $('c-copy').onclick = () => navigator.clipboard.writeText(location.href).then(() => $('c-copy').textContent = 'Link copied ✓');
      document.title = n + ' — ' + TITLES[c] + ' certificate';
      $('cert-view').hidden = false;
    }
  </script>''')

def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8', newline='\n').write(text)

if __name__ == '__main__':
    for c in COURSES:
        write(f'courses/{c["slug"]}.html', course_page(c))
    write('courses.html', catalog())
    write('certificate.html', certificate())
    print('built', len(COURSES), 'courses:', ', '.join(c['slug'] for c in COURSES))
    import seo; seo.main()
