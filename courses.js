// Course pages: lesson progress, final quiz and certificate unlock.
// Progress lives in this browser only (localStorage); everything still works if storage is blocked.
(() => {
  const page = document.querySelector('[data-course]');
  if (!page) return;
  const slug = page.dataset.course, key = 'course:' + slug;
  const load = () => { try { return JSON.parse(localStorage.getItem(key)) || {}; } catch (e) { return {}; } };
  const save = s => { try { localStorage.setItem(key, JSON.stringify(s)); } catch (e) {} };
  let state = Object.assign({ done: [], score: 0 }, load());

  const lessons = [...document.querySelectorAll('.lesson')];
  const total = lessons.length, passMark = +page.dataset.pass;

  function render() {
    lessons.forEach(l => {
      const done = state.done.includes(l.id);
      const btn = l.querySelector('.mark');
      btn.textContent = done ? '✓ Completed' : 'Mark lesson complete';
      btn.classList.toggle('is-done', done);
      document.querySelectorAll(`.syllabus a[href="#${l.id}"]`).forEach(a => a.classList.toggle('is-done', done));
    });
    const pct = Math.round(state.done.length / total * 100);
    document.querySelectorAll('[data-progress-bar]').forEach(b => b.style.width = pct + '%');
    document.querySelectorAll('[data-progress-text]').forEach(t => t.textContent = `${state.done.length} of ${total} lessons · ${pct}%`);
    const lessonsDone = state.done.length === total, passed = state.score >= passMark;
    document.getElementById('cert-lessons').classList.toggle('ok', lessonsDone);
    document.getElementById('cert-quiz').classList.toggle('ok', passed);
    document.getElementById('cert-form').hidden = !(lessonsDone && passed);
    document.getElementById('cert-locked').hidden = lessonsDone && passed;
  }

  lessons.forEach(l => l.querySelector('.mark').addEventListener('click', () => {
    state.done = state.done.includes(l.id) ? state.done.filter(x => x !== l.id) : [...state.done, l.id];
    save(state); render();
  }));

  // Quiz: one radio group per question; data-answer holds the index of the right option.
  const quiz = document.getElementById('quiz');
  quiz.addEventListener('submit', e => {
    e.preventDefault();
    const qs = [...quiz.querySelectorAll('.q')];
    let right = 0;
    qs.forEach(q => {
      const picked = q.querySelector('input:checked');
      const ok = picked && +picked.value === +q.dataset.answer;
      right += ok;
      q.classList.toggle('right', !!ok);
      q.classList.toggle('wrong', !ok);
    });
    const score = Math.round(right / qs.length * 100);
    state.score = Math.max(state.score, score); save(state);
    const out = document.getElementById('quiz-result');
    out.hidden = false;
    out.className = 'quiz-result ' + (score >= passMark ? 'pass' : 'fail');
    out.textContent = score >= passMark
      ? `You scored ${score}% (${right}/${qs.length}). Passed — well done!`
      : `You scored ${score}% (${right}/${qs.length}). You need ${passMark}% to pass. Review the highlighted questions and try again.`;
    render();
  });

  // Certificate: details travel in the URL fragment (#…), which never reaches the server.
  document.getElementById('cert-form').addEventListener('submit', e => {
    e.preventDefault();
    const name = document.getElementById('cert-name').value.trim();
    if (!name) return;
    const now = new Date(), d = [now.getFullYear(), now.getMonth() + 1, now.getDate()].map(x => String(x).padStart(2, '0')).join('-'); // local date, not UTC
    location.href = '../certificate.html#' + new URLSearchParams({ c: slug, n: name, d });
  });

  render();
})();
