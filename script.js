document.addEventListener('DOMContentLoaded', function() {
    
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navbar = document.querySelector('.navbar');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }));

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = '#fff';
            navbar.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
        } else {
            if (!navMenu.classList.contains('active')) {
                navbar.style.background = 'transparent';
                navbar.style.boxShadow = 'none';
            }
        }
    });

    const projectBtns = document.querySelectorAll('.project-btn');
    const modals = document.querySelectorAll('.modal');
    const closeBtns = document.querySelectorAll('.close-btn');

    projectBtns.forEach(btn => {
        btn.onclick = function() {
            let modal = document.getElementById(btn.getAttribute('data-modal'));
            modal.style.display = "block";
        }
    });

    closeBtns.forEach(btn => {
        btn.onclick = function() {
            let modal = btn.closest('.modal');
            modal.style.display = "none";
        }
    });

    window.onclick = function(event) {
        modals.forEach(modal => {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        });
    }


    
    const logos = document.querySelectorAll('.background-logos i');

    window.addEventListener('scroll', () => {
        const scrollValue = window.scrollY;

    
        logos.forEach((logo, index) => {
            let speed = (index % 3 + 1) * 0.1; 
            logo.style.transform = `translateY(-${scrollValue * speed}px)`;
        });
    });
});