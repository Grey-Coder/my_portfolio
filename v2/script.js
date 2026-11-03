const progress = document.querySelector('.scroll-progress');
const orb = document.querySelector('.contact-orb');
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.site-nav');

const updateScrollState = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = `${scrollable ? (window.scrollY / scrollable) * 100 : 0}%`;
    if (orb) orb.style.transform = `translate(28%, ${15 + window.scrollY * 0.015}%)`;
};

window.addEventListener('scroll', updateScrollState, { passive: true });
updateScrollState();

menuToggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
});

nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    nav.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
}));

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
