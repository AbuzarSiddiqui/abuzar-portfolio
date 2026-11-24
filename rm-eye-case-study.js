(() => {
  'use strict';
  const PAYLOAD_URL = 'assets/rm-eye-case-study.enc';
  const MAGIC = 'RMEYE1';
  const ITERATIONS = 600000;
  const form = document.querySelector('#access-form');
  const codeInput = document.querySelector('#access-code');
  const message = document.querySelector('#access-message');
  const accessPanel = document.querySelector('#access-panel');
  const documentPanel = document.querySelector('#document-panel');
  const pdfObject = document.querySelector('#case-study-document');
  const download = document.querySelector('#download-document');
  const lock = document.querySelector('#lock-document');
  let objectUrl = '';

  const setMessage = (text, error = false) => {
    message.textContent = text;
    message.classList.toggle('is-error', error);
  };

  const clearDocument = () => {
    pdfObject.removeAttribute('data');
    download.removeAttribute('href');
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    objectUrl = '';
    documentPanel.hidden = true;
    accessPanel.hidden = false;
    form.reset();
    setMessage('Enter the code to continue.');
    codeInput.focus();
  };

  async function decrypt(code) {
    const response = await fetch(PAYLOAD_URL, { cache: 'no-store' });
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

  form.addEventListener('submit', async event => {
    event.preventDefault();
    const code = codeInput.value;
    if (!code) { setMessage('Enter the access code to continue.', true); codeInput.focus(); return; }
    const button = form.querySelector('button');
    button.disabled = true;
    setMessage('Unlocking the encrypted document…');
    try {
      const bytes = await decrypt(code);
      objectUrl = URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' }));
      pdfObject.data = objectUrl;
      download.href = objectUrl;
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
