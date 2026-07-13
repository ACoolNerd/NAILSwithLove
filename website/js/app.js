/* ── Service Worker registration ── */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js')
      .then(reg => console.log('SW registered:', reg.scope))
      .catch(err => console.warn('SW registration failed:', err));
  });
}

/* ── Mobile nav toggle ── */
const navToggle = document.getElementById('navToggle');
const navMenu   = document.getElementById('navMenu');

navToggle.addEventListener('click', () => {
  const isOpen = navMenu.classList.toggle('is-open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
  navToggle.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
});

/* Close nav when a link is clicked */
navMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', 'Abrir menú');
  });
});

/* ── Sticky nav shadow on scroll ── */
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.style.boxShadow = window.scrollY > 10
    ? '0 2px 16px rgba(0,0,0,.14)'
    : '0 1px 8px rgba(0,0,0,.08)';
}, { passive: true });

/* ── Animate elements into view ── */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(
  '.service-card, .loyalty__card, .step, .pricing__group'
).forEach(el => {
  el.classList.add('fade-up');
  observer.observe(el);
});

/* Inject the fade-up animation via JS so it only runs with JS enabled */
const style = document.createElement('style');
style.textContent = `
  .fade-up { opacity: 0; transform: translateY(20px); transition: opacity .5s ease, transform .5s ease; }
  .fade-up.visible { opacity: 1; transform: translateY(0); }
`;
document.head.appendChild(style);
