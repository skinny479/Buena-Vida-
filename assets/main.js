// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
}

// Reveal-on-scroll
const io = 'IntersectionObserver' in window
  ? new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 })
  : null;
document.querySelectorAll('.reveal').forEach((el) => (io ? io.observe(el) : el.classList.add('visible')));

// Footer year
document.querySelectorAll('[data-year]').forEach((el) => (el.textContent = new Date().getFullYear()));

// Contact form: no backend yet — open the visitor's email client with the request prefilled
const form = document.querySelector('#appointment-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = new FormData(form);
    const body = [
      `Name: ${d.get('name')}`,
      `Phone: ${d.get('phone')}`,
      `Email: ${d.get('email')}`,
      `Service: ${d.get('service')}`,
      `Preferred time: ${d.get('time')}`,
      '',
      d.get('message') || '',
    ].join('\n');
    window.location.href = `mailto:${form.dataset.to}?subject=${encodeURIComponent('Appointment request')}&body=${encodeURIComponent(body)}`;
  });
}
