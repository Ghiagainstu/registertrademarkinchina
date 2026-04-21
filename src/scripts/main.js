// Minimal client script: language switcher stub, lazy-load case, simple analytics placeholder
(function () {
  'use strict';
  function loadCase() {
    var container = document.getElementById('featured-case');
    if (!container) return;
    container.innerHTML = '<p class="text-slate-500">Example: "ABC Corp" — a global brand entering China. We secured domain-like marks and mitigated conflicting registrations within 6 months.</p>';
  }
  document.addEventListener('DOMContentLoaded', loadCase);
  function initCookieConsent() {
    if (document.cookie.indexOf('tc_consent') !== -1) return;
    var bar = document.createElement('div');
    bar.style.cssText = 'position:fixed;bottom:0;left:0;right:0;background:#0F172A;color:#fff;padding:.75rem 1rem;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:.5rem;z-index:9999;font-size:.85rem;';
    bar.innerHTML = 'This site uses cookies to deliver our services and improve your experience. Necessary cookies are enabled. <a href="/cookie.html" style="color:#60A5FA;">Privacy</a> <button id="tc-accept" style="background:#10B981;border:none;color:#fff;padding:.35rem .6rem;border-radius:4px;cursor:pointer;">Accept</button>';
    document.body.appendChild(bar);
    document.getElementById('tc-accept').addEventListener('click', function () {
      document.cookie = 'tc_consent=1; path=/; max-age=' + 365*24*60*60;
      bar.style.display = 'none';
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initCookieConsent); else initCookieConsent();
})();
