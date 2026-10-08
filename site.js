// Shared behaviour: theme toggle, nav border on scroll, reveal-on-scroll.
// The saved theme and the .js class are set by the inline snippet in each page's <head> (avoids a flash).
const root = document.documentElement;

document.querySelectorAll('[data-theme-toggle]').forEach(b => b.addEventListener('click', () => {
  const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  root.dataset.theme = dark ? 'light' : 'dark';
  try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
}));

const nav = document.querySelector('.nav');
if (nav) addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 8), { passive: true });

const io = 'IntersectionObserver' in window && new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('in'));
