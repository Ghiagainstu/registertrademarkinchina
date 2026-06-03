(function () {
  'use strict';

  // Mobile menu toggle
  function initMobileMenu() {
    var btn = document.getElementById('mobile-menu-btn');
    var menu = document.getElementById('mobile-menu');
    if (!btn || !menu) return;
    btn.addEventListener('click', function () {
      menu.classList.toggle('hidden');
    });
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        menu.classList.add('hidden');
      });
    });
  }

  // Scroll reveal
  function initReveal() {
    var elements = document.querySelectorAll('.reveal');
    if (!elements.length) return;
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    elements.forEach(function (el) { observer.observe(el); });
  }

  // Cookie consent
  function initCookieConsent() {
    if (document.cookie.indexOf('rtmcn_consent') !== -1) return;
    var banner = document.getElementById('cookie-banner');
    var acceptBtn = document.getElementById('cookie-accept');
    if (!banner || !acceptBtn) return;
    banner.classList.remove('hidden');
    acceptBtn.addEventListener('click', function () {
      document.cookie = 'rtmcn_consent=1; path=/; max-age=' + (365 * 24 * 60 * 60);
      banner.classList.add('hidden');
    });
  }

  // Smooth scroll for anchor links
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        var target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  // Form handling (Formspree AJAX)
  function initForm() {
    var form = document.getElementById('contactFormEl');
    var success = document.getElementById('formSuccess');
    var error = document.getElementById('formError');
    var btn = document.getElementById('contactSubmitBtn');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }
      if (error) error.classList.add('hidden');
      var formData = new FormData(form);
      fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: { 'Accept': 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          form.classList.add('hidden');
          if (success) success.classList.remove('hidden');
        } else {
          return res.json().then(function (data) {
            if (data && data.errors) {
              var msgs = data.errors.map(function (e) { return e.message; }).join(', ');
              if (error) error.querySelector('p').textContent = msgs;
            }
            if (error) error.classList.remove('hidden');
          });
        }
      }).catch(function () {
        if (error) error.classList.remove('hidden');
      }).then(function () {
        if (btn) { btn.disabled = false; btn.textContent = 'Send Inquiry'; }
      });
    });
  }

  // Nav background on scroll
  function initNavScroll() {
    var nav = document.querySelector('nav');
    if (!nav) return;
    window.addEventListener('scroll', function () {
      if (window.scrollY > 50) {
        nav.style.background = 'rgba(11, 15, 26, 0.95)';
      } else {
        nav.style.background = 'rgba(11, 15, 26, 0.6)';
      }
    });
  }

  // Init
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initMobileMenu();
      initReveal();
      initCookieConsent();
      initSmoothScroll();
      initForm();
      initNavScroll();
    });
  } else {
    initMobileMenu();
    initReveal();
    initCookieConsent();
    initSmoothScroll();
    initForm();
    initNavScroll();
  }
})();
