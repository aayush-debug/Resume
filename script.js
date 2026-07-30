// ==========================================================================
// PORTFOLIO & RESUME INTERACTIVE SCRIPT
// Features: Theme Switcher (Dark/Light), Smooth Scroll, Spotlight FX, Form Handler
// ==========================================================================

// Smooth scroll to target section with header offset
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        const headerOffset = 90;
        const elementPosition = section.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });

        // Close mobile nav menu if open
        const navMenu = document.getElementById('nav-menu');
        const mobileToggleIcon = document.querySelector('#mobile-toggle i');
        if (navMenu && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            if (mobileToggleIcon) mobileToggleIcon.className = 'fas fa-bars';
        }
    }
}

// Download Resume function
function downloadResume() {
    const link = document.createElement('a');
    link.href = 'resume.pdf';
    link.download = 'Aayush_Patel_Resume.pdf';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Client-side Contact Form Handler
function handleFormSubmit(event) {
    event.preventDefault();
    const form = document.getElementById('contact-form');
    const statusMsg = document.getElementById('form-status');

    if (!form || !statusMsg) return;

    // Show simulated success status
    statusMsg.className = 'form-status-msg success';
    statusMsg.style.display = 'block';
    statusMsg.innerHTML = '<i class="fas fa-check-circle"></i> Thank you! Your message has been sent successfully. I will get back to you shortly.';

    // Reset form fields
    form.reset();

    // Auto hide success message after 5 seconds
    setTimeout(() => {
        statusMsg.style.display = 'none';
    }, 5000);
}

document.addEventListener('DOMContentLoaded', function() {
    // --- 1. MOUSE SPOTLIGHT CARD EFFECT ---
    const spotlightCards = document.querySelectorAll('.spotlight-card');
    spotlightCards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });

    // --- 2. MOBILE NAVIGATION TOGGLE ---
    const mobileToggle = document.getElementById('mobile-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            navMenu.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (icon) {
                if (navMenu.classList.contains('active')) {
                    icon.className = 'fas fa-xmark';
                } else {
                    icon.className = 'fas fa-bars';
                }
            }
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                const icon = mobileToggle.querySelector('i');
                if (icon) icon.className = 'fas fa-bars';
            }
        });
    }

    // --- 3. SCROLL HEADER HIDE / REVEAL ---
    let lastScrollTop = 0;
    const navbarWrapper = document.querySelector('.navbar-wrapper');

    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop < 0) scrollTop = 0;

        if (scrollTop > lastScrollTop && scrollTop > 150) {
            // Scroll Down - hide header
            if (navbarWrapper) navbarWrapper.style.transform = 'translateY(-130%)';
        } else {
            // Scroll Up or top - reveal header
            if (navbarWrapper) navbarWrapper.style.transform = 'translateY(0)';
        }

        lastScrollTop = scrollTop;
    }, { passive: true });

    // --- 4. ACTIVE NAV LINK INTERSECTION OBSERVER ---
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-link');

    const observerOptions = {
        root: null,
        rootMargin: '-30% 0px -40% 0px',
        threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => sectionObserver.observe(section));

    // --- 5. REVEAL ANIMATIONS ON SCROLL ---
    const revealElements = document.querySelectorAll('.spotlight-card, .section-header');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });

    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(25px)';
        el.style.transition = 'opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)';
        revealObserver.observe(el);
    });
});
