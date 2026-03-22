import './style.css';

document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  const dropdown = document.querySelector('.dropdown');
  const dropbtn = document.querySelector('.dropbtn');

  // --- Inject mobile-only elements ---
  if (window.innerWidth <= 768 || true) { // Always inject, CSS hides on desktop
    // 1. Close button (X) for Level 1
    const closeBtn = document.createElement('button');
    closeBtn.className = 'mobile-close-btn';
    closeBtn.innerHTML = '<i class="fas fa-times"></i>';
    closeBtn.setAttribute('aria-label', 'Menü schließen');
    document.body.appendChild(closeBtn);

    // 2. Kontakt CTA button at bottom
    const kontaktCta = document.createElement('div');
    kontaktCta.className = 'mobile-kontakt-cta';
    kontaktCta.innerHTML = '<a href="/kontakt.html">Kontakt</a>';
    document.body.appendChild(kontaktCta);

    // 3. Back button for Level 2 (submenu)
    const backBtn = document.createElement('button');
    backBtn.className = 'mobile-back-btn';
    backBtn.innerHTML = '<i class="fas fa-chevron-left"></i> zurück';
    document.body.appendChild(backBtn);

    // 4. Close button (X) for Level 2
    const backCloseBtn = document.createElement('button');
    backCloseBtn.className = 'mobile-back-btn-close';
    backCloseBtn.innerHTML = '<i class="fas fa-times"></i>';
    backCloseBtn.setAttribute('aria-label', 'Menü schließen');
    document.body.appendChild(backCloseBtn);

    // --- Functions ---
    function openNav() {
      navLinks.classList.add('active');
      toggleBtn.querySelector('i').className = 'fas fa-times';
      closeBtn.style.display = 'flex';
      kontaktCta.style.display = 'block';
      document.body.style.overflow = 'hidden';
      // Hide back button elements (Level 2 not open yet)
      backBtn.style.display = 'none';
      backCloseBtn.style.display = 'none';
    }

    function closeNav() {
      navLinks.classList.remove('active');
      if (dropdown) dropdown.classList.remove('active');
      toggleBtn.querySelector('i').className = 'fas fa-bars';
      closeBtn.style.display = 'none';
      kontaktCta.style.display = 'none';
      backBtn.style.display = 'none';
      backCloseBtn.style.display = 'none';
      document.body.style.overflow = '';
    }

    function openSubmenu() {
      if (dropdown) {
        dropdown.classList.add('active');
        // Switch to Level 2 UI
        closeBtn.style.display = 'none';
        backBtn.style.display = 'flex';
        backCloseBtn.style.display = 'flex';
      }
    }

    function closeSubmenu() {
      if (dropdown) {
        dropdown.classList.remove('active');
        // Switch back to Level 1 UI
        closeBtn.style.display = 'flex';
        backBtn.style.display = 'none';
        backCloseBtn.style.display = 'none';
      }
    }

    // --- Event Listeners ---
    
    // Hamburger toggle
    if (toggleBtn && navLinks) {
      toggleBtn.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
          closeNav();
        } else {
          openNav();
        }
      });
    }

    // Close button (X) on Level 1
    closeBtn.addEventListener('click', closeNav);

    // Kontakt CTA closes nav
    kontaktCta.querySelector('a').addEventListener('click', () => {
      closeNav();
    });

    // Dropdown button opens Level 2
    if (dropbtn) {
      dropbtn.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          openSubmenu();
        }
      });
    }

    // Back button returns to Level 1
    backBtn.addEventListener('click', closeSubmenu);

    // Close button (X) on Level 2 closes everything
    backCloseBtn.addEventListener('click', closeNav);

    // Close nav when clicking a regular (non-dropdown) link
    navLinks.querySelectorAll('a:not(.dropbtn)').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          closeNav();
        }
      });
    });

    // Close on resize to desktop
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        closeNav();
      }
    });

    // Initially hide mobile elements
    closeBtn.style.display = 'none';
    kontaktCta.style.display = 'none';
    backBtn.style.display = 'none';
    backCloseBtn.style.display = 'none';
  }

  // Cookie Banner Logic
  const cookieBanner = document.getElementById('cookie-banner');
  const acceptBtn = document.getElementById('accept-cookies');

  if (cookieBanner && acceptBtn) {
    if (!localStorage.getItem('cookiesAccepted')) {
      cookieBanner.style.display = 'block';
    }

    acceptBtn.addEventListener('click', () => {
      localStorage.setItem('cookiesAccepted', 'true');
      cookieBanner.style.display = 'none';
    });
  }
});
