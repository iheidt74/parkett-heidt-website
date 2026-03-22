/**
 * Konfigurator – Parkett Heidt
 * Step navigation, option selection, file upload, validation, form submission
 */
(function() {
  'use strict';

  const state = {
    currentStep: 1,
    totalSteps: 6,
    data: {
      arbeiten: [],
      bodenart: [],
      flaeche: '',
      raeume: '',
      objekttyp: '',
      etage: '',
      aufzug: '',
      files: [],
      zeitrahmen: '',
      kundentyp: 'privat',
      firmenname: '',
      vorname: '',
      nachname: '',
      telefon: '',
      email: '',
      strasse: '',
      plz: '',
      ort: '',
      kanal: 'whatsapp',
      nachricht: '',
      dsgvo: false
    }
  };

  // --- Option Card Selection ---
  document.querySelectorAll('.option-grid').forEach(grid => {
    const isMulti = grid.dataset.multi === 'true';
    const field = grid.dataset.field;

    grid.querySelectorAll('.option-card').forEach(card => {
      card.addEventListener('click', () => {
        if (isMulti) {
          card.classList.toggle('selected');
          const selected = [...grid.querySelectorAll('.option-card.selected')].map(c => c.dataset.value);
          state.data[field] = selected;
        } else {
          grid.querySelectorAll('.option-card').forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          state.data[field] = card.dataset.value;
        }
      });
    });
  });

  // --- Channel Selection ---
  document.querySelectorAll('.channel-grid .channel-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.channel-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      state.data.kanal = card.dataset.value;
    });
  });

  // --- Privat / Firma Toggle ---
  document.querySelectorAll('.toggle-group button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.toggle-group button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      state.data.kundentyp = btn.dataset.value;
      document.getElementById('firmaField').style.display = btn.dataset.value === 'firma' ? 'block' : 'none';
    });
  });

  // --- Step Navigation ---
  function goToStep(step) {
    document.querySelectorAll('.konfig-step').forEach(el => {
      el.classList.remove('active');
      el.style.display = 'none';
    });

    const target = document.querySelector(`.konfig-step[data-step="${step}"]`);
    if (target) {
      target.style.display = 'block';
      // Trigger animation
      target.classList.remove('active');
      void target.offsetWidth; // reflow
      target.classList.add('active');
    }

    state.currentStep = step;
    document.getElementById('currentStep').textContent = step;

    // Update progress bar
    const pct = (step / state.totalSteps) * 100;
    document.querySelector('.progress-bar-fill').style.width = pct + '%';

    // Scroll to top of wizard
    document.querySelector('.konfig-wrapper').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // Bind all next/back buttons
  for (let i = 1; i <= 6; i++) {
    const nextBtn = document.getElementById(`next-${i}`);
    const backBtn = document.getElementById(`back-${i}`);
    if (nextBtn) nextBtn.addEventListener('click', () => { if (validateStep(i)) goToStep(i + 1); });
    if (backBtn) backBtn.addEventListener('click', () => goToStep(i - 1));
  }

  // --- Validation ---
  function validateStep(step) {
    switch(step) {
      case 1:
        if (state.data.arbeiten.length === 0) {
          showToast('Bitte wählen Sie mindestens eine Arbeitsart.');
          return false;
        }
        return true;
      case 2:
        if (state.data.bodenart.length === 0) {
          showToast('Bitte wählen Sie mindestens einen Bodenbelag.');
          return false;
        }
        state.data.flaeche = document.getElementById('flaeche').value;
        state.data.raeume = document.getElementById('raeume').value;
        if (!state.data.flaeche) {
          showToast('Bitte geben Sie die Gesamtfläche an.');
          document.getElementById('flaeche').focus();
          return false;
        }
        return true;
      case 3:
        if (!state.data.objekttyp) {
          showToast('Bitte wählen Sie den Objekttyp.');
          return false;
        }
        state.data.etage = document.getElementById('etage').value;
        if (!state.data.etage) {
          showToast('Bitte wählen Sie die Etage.');
          return false;
        }
        return true;
      case 4:
        // Files are optional
        return true;
      case 5:
        if (!state.data.zeitrahmen) {
          showToast('Bitte wählen Sie einen Zeitrahmen.');
          return false;
        }
        return true;
      default:
        return true;
    }
  }

  // --- Toast Notification ---
  function showToast(msg) {
    let toast = document.getElementById('konfig-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'konfig-toast';
      toast.style.cssText = 'position:fixed;bottom:2rem;left:50%;transform:translateX(-50%);background:#2c3e50;color:white;padding:0.75rem 1.5rem;border-radius:8px;font-size:0.95rem;z-index:9999;opacity:0;transition:opacity 0.3s;box-shadow:0 4px 12px rgba(0,0,0,0.2);max-width:90%;text-align:center;';
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.opacity = '1';
    setTimeout(() => { toast.style.opacity = '0'; }, 3000);
  }

  // --- File Upload ---
  const uploadZone = document.getElementById('uploadZone');
  const fileInput = document.getElementById('fileInput');
  const fileList = document.getElementById('fileList');
  const MAX_FILES = 8;
  const MAX_SIZE = 25 * 1024 * 1024; // 25 MB

  if (uploadZone && fileInput) {
    uploadZone.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('dragover', e => { e.preventDefault(); uploadZone.classList.add('dragover'); });
    uploadZone.addEventListener('dragleave', () => uploadZone.classList.remove('dragover'));
    uploadZone.addEventListener('drop', e => {
      e.preventDefault();
      uploadZone.classList.remove('dragover');
      handleFiles(e.dataTransfer.files);
    });
    fileInput.addEventListener('change', () => handleFiles(fileInput.files));
  }

  function handleFiles(files) {
    for (const file of files) {
      if (state.data.files.length >= MAX_FILES) {
        showToast(`Maximal ${MAX_FILES} Dateien erlaubt.`);
        break;
      }
      if (file.size > MAX_SIZE) {
        showToast(`"${file.name}" ist zu groß (max. 25 MB).`);
        continue;
      }
      state.data.files.push(file);
    }
    renderFileList();
  }

  function renderFileList() {
    fileList.innerHTML = '';
    state.data.files.forEach((file, idx) => {
      const li = document.createElement('li');
      const sizeKB = (file.size / 1024).toFixed(0);
      li.innerHTML = `<span><i class="fas fa-file"></i> ${file.name} <small>(${sizeKB} KB)</small></span>
        <button class="file-remove" data-idx="${idx}"><i class="fas fa-times"></i></button>`;
      fileList.appendChild(li);
    });
    fileList.querySelectorAll('.file-remove').forEach(btn => {
      btn.addEventListener('click', () => {
        state.data.files.splice(parseInt(btn.dataset.idx), 1);
        renderFileList();
      });
    });
  }

  // --- Submit ---
  const submitBtn = document.getElementById('submitBtn');
  if (submitBtn) {
    submitBtn.addEventListener('click', () => {
      // Collect remaining fields
      state.data.firmenname = document.getElementById('firmenname').value;
      state.data.vorname = document.getElementById('vorname').value;
      state.data.nachname = document.getElementById('nachname').value;
      state.data.telefon = document.getElementById('telefon').value;
      state.data.email = document.getElementById('email').value;
      state.data.strasse = document.getElementById('strasse').value;
      state.data.plz = document.getElementById('plz').value;
      state.data.ort = document.getElementById('ort').value;
      state.data.nachricht = document.getElementById('nachricht').value;
      state.data.dsgvo = document.getElementById('dsgvo').checked;

      // Validate
      if (!state.data.vorname || !state.data.nachname) {
        showToast('Bitte geben Sie Ihren Namen ein.');
        return;
      }
      if (!state.data.telefon) {
        showToast('Bitte geben Sie Ihre Telefonnummer ein.');
        return;
      }
      if (!state.data.dsgvo) {
        showToast('Bitte stimmen Sie der Datenschutzerklärung zu.');
        return;
      }

      // Build summary and show success
      console.log('Konfigurator Data:', JSON.stringify(state.data, null, 2));

      // Build mailto fallback
      const subject = encodeURIComponent('Anfrage über Konfigurator – Parkett Heidt');
      const body = encodeURIComponent(buildEmailBody());
      const mailtoLink = `mailto:support@parkett-heidt.de?subject=${subject}&body=${body}`;

      // Show success
      document.querySelectorAll('.konfig-step').forEach(el => { el.classList.remove('active'); el.style.display = 'none'; });
      const successStep = document.querySelector('.konfig-step[data-step="success"]');
      successStep.style.display = 'block';
      successStep.classList.add('active');

      // Update progress to 100%
      document.querySelector('.progress-bar-fill').style.width = '100%';
      document.getElementById('currentStep').textContent = '✓';
      document.querySelector('.step-indicator').textContent = 'Fertig!';

      // Open email client as fallback
      window.open(mailtoLink, '_self');
    });
  }

  function buildEmailBody() {
    const d = state.data;
    return `ANFRAGE ÜBER KONFIGURATOR
========================

ARBEITEN: ${d.arbeiten.join(', ')}
BODENART: ${d.bodenart.join(', ')}
FLÄCHE: ${d.flaeche} m² | RÄUME: ${d.raeume || 'k.A.'}
OBJEKTTYP: ${d.objekttyp}
ETAGE: ${d.etage} | AUFZUG: ${d.aufzug || 'k.A.'}
ZEITRAHMEN: ${d.zeitrahmen}

KONTAKT
-------
${d.kundentyp === 'firma' ? 'FIRMA: ' + d.firmenname + '\n' : ''}NAME: ${d.vorname} ${d.nachname}
TELEFON: ${d.telefon}
E-MAIL: ${d.email || 'k.A.'}
ADRESSE: ${d.strasse}, ${d.plz} ${d.ort}
KANAL: ${d.kanal}

NACHRICHT: ${d.nachricht || '–'}
`;
  }

})();
