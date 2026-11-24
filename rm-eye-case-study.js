(() => {
  'use strict';
  const PDF_URL = 'assets/rm-eye-case-study.enc';
  const CONTENT_URL = 'assets/rm-eye-case-study-content.enc';
  const MAGIC = 'RMEYE1';
  const ITERATIONS = 600000;
  const form = document.querySelector('#access-form');
  const codeInput = document.querySelector('#access-code');
  const message = document.querySelector('#access-message');
  const accessPanel = document.querySelector('#access-panel');
  const documentPanel = document.querySelector('#document-panel');
  const caseContent = document.querySelector('#case-study-content');
  const download = document.querySelector('#download-document');
  const lock = document.querySelector('#lock-document');
  let objectUrl = '';

  const setMessage = (text, error = false) => {
    message.textContent = text;
    message.classList.toggle('is-error', error);
  };

  const clearDocument = () => {
    download.removeAttribute('href');
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    objectUrl = '';
    caseContent.replaceChildren();
    documentPanel.hidden = true;
    accessPanel.hidden = false;
    form.reset();
    setMessage('Enter the code to continue.');
    codeInput.focus();
  };

  async function decrypt(url, code) {
    const response = await fetch(url, { cache: 'no-store' });
    if (!response.ok) throw new Error('The protected document is unavailable. Please contact Abuzar.');
    const data = new Uint8Array(await response.arrayBuffer());
    const header = new TextDecoder().decode(data.slice(0, 6));
    if (header !== MAGIC || data.length < 35) throw new Error('The protected document is invalid.');
    const salt = data.slice(6, 22);
    const nonce = data.slice(22, 34);
    const ciphertext = data.slice(34);
    const material = await crypto.subtle.importKey('raw', new TextEncoder().encode(code), 'PBKDF2', false, ['deriveKey']);
    const key = await crypto.subtle.deriveKey({ name: 'PBKDF2', salt, iterations: ITERATIONS, hash: 'SHA-256' }, material, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    return crypto.subtle.decrypt({ name: 'AES-GCM', iv: nonce }, key, ciphertext);
  }

  const esc = value => String(value).replace(/[&<>"']/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' })[char]);
  const list = items => `<ul>${items.map(item => `<li>${esc(item)}</li>`).join('')}</ul>`;
  const card = (title, copy, label = '') => `<article class="case-card">${label ? `<span class="case-kicker">${esc(label)}</span>` : ''}<h3>${esc(title)}</h3><p>${esc(copy)}</p></article>`;
  const table = (headers, rows) => `<div class="case-table-wrap"><table class="case-table"><thead><tr>${headers.map(h => `<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>${rows.map(row => `<tr>${row.map(cell => `<td>${esc(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;

  function productViews(data) {
    const view = data.productViews;
    return `<section class="case-section case-product"><div class="case-section-head"><div><span class="case-number">04</span><h2>Product experience</h2></div><p>Four product surfaces turn a raw alert into an explained, auditable decision and a field outcome.</p></div><div class="prototype-tabs" role="tablist" aria-label="Product prototype views">${view.map((item, index) => `<button type="button" role="tab" aria-selected="${index === 0}" data-view="${index}">${esc(item.label)}</button>`).join('')}</div><div class="prototype-stage">${view.map((item, index) => `<article class="prototype ${index ? 'is-hidden' : ''}" data-prototype="${index}"><div class="prototype-bar"><span>RM EYE</span><span>${esc(item.label)}</span><span class="prototype-status">SAMPLE DATA</span></div>${item.html}</article>`).join('')}</div><div class="case-grid three">${view.map(item => card(item.label, item.note, 'Design rationale')).join('')}</div></section>`;
  }

  function renderCase(data) {
    const nav = data.sections.map((section, index) => `<button type="button" class="${index === 0 ? 'is-active' : ''}" data-section="${index}">${String(index + 1).padStart(2, '0')} · ${esc(section.nav)}</button>`).join('');
    const sections = data.sections.map((section, index) => `<article class="case-view ${index ? 'is-hidden' : ''}" data-case-section="${index}">${section.html}</article>`).join('');
    caseContent.innerHTML = `<div class="case-nav" aria-label="Case study sections"><div class="case-nav-scroll">${nav}</div></div><div class="case-views">${sections}</div>`;
    caseContent.querySelectorAll('[data-section]').forEach(button => button.addEventListener('click', () => {
      const current = button.dataset.section;
      caseContent.querySelectorAll('[data-section]').forEach(item => item.classList.toggle('is-active', item === button));
      caseContent.querySelectorAll('[data-case-section]').forEach(item => item.classList.toggle('is-hidden', item.dataset.caseSection !== current));
      caseContent.querySelector('[data-case-section="' + current + '"]').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }));
    caseContent.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => {
      const current = button.dataset.view;
      caseContent.querySelectorAll('[data-view]').forEach(item => item.setAttribute('aria-selected', String(item === button)));
      caseContent.querySelectorAll('[data-prototype]').forEach(item => item.classList.toggle('is-hidden', item.dataset.prototype !== current));
    }));
  }

  form.addEventListener('submit', async event => {
    event.preventDefault();
    const code = codeInput.value;
    if (!code) { setMessage('Enter the access code to continue.', true); codeInput.focus(); return; }
    const button = form.querySelector('button');
    button.disabled = true;
    setMessage('Unlocking the encrypted document…');
    try {
      const [pdfBytes, contentBytes] = await Promise.all([decrypt(PDF_URL, code), decrypt(CONTENT_URL, code)]);
      const data = JSON.parse(new TextDecoder().decode(contentBytes));
      objectUrl = URL.createObjectURL(new Blob([pdfBytes], { type: 'application/pdf' }));
      download.href = objectUrl;
      renderCase(data);
      accessPanel.hidden = true;
      documentPanel.hidden = false;
      codeInput.value = '';
    } catch (error) {
      setMessage(error.message.includes('OperationError') ? 'That access code is not valid. Please try again.' : error.message, true);
      codeInput.select();
    } finally {
      button.disabled = false;
    }
  });
  lock.addEventListener('click', clearDocument);
  window.addEventListener('pagehide', () => { if (objectUrl) URL.revokeObjectURL(objectUrl); });
})();
