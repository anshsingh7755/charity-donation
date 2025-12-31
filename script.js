// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Close menu when a link is clicked
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
        });
    });
}

// Donation Amount Selection
const amountButtons = document.querySelectorAll('.amount-btn');
const customAmount = document.getElementById('custom-amount');

if (amountButtons.length > 0) {
    amountButtons.forEach(button => {
        button.addEventListener('click', () => {
            amountButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            customAmount.value = '';
        });
    });

    customAmount.addEventListener('input', () => {
        amountButtons.forEach(btn => btn.classList.remove('active'));
    });
}

// Form Submission
const donationForm = document.getElementById('donationForm');
if (donationForm) {
    donationForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const selectedAmount = document.querySelector('.amount-btn.active');
        const customAmountValue = customAmount.value;
        const amount = selectedAmount ? selectedAmount.dataset.amount : customAmountValue;
        
        if (!amount) {
            alert('Please select or enter a donation amount');
            return;
        }

        const formData = {
            name: donationForm.querySelector('input[type="text"]').value,
            email: donationForm.querySelector('input[type="email"]').value,
            phone: donationForm.querySelector('input[type="tel"]').value,
            cause: donationForm.querySelector('select').value,
            message: donationForm.querySelector('textarea').value,
            amount: amount
        };

        // Show success message
        alert(`Thank you for your generous donation of $${amount}! We will contact you shortly.`);
        donationForm.reset();
        amountButtons.forEach(btn => btn.classList.remove('active'));
    });
}

// Contact Form Submission
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const formData = {
            name: contactForm.querySelector('input[type="text"]').value,
            email: contactForm.querySelector('input[type="email"]').value,
            subject: contactForm.querySelector('select').value,
            message: contactForm.querySelector('textarea').value
        };

        alert('Thank you for reaching out! We will respond to your message shortly.');
        contactForm.reset();
    });
}

// Scroll Animation for Elements
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe cause cards and quote cards
document.querySelectorAll('.cause-card, .quote-card, .stat').forEach(el => {
    observer.observe(el);
});

// Smooth navbar background change on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.2)';
    } else {
        navbar.style.boxShadow = 'var(--shadow)';
    }
});

// Counter Animation
const animateCounter = (element, target, duration = 1000) => {
    let current = 0;
    const increment = target / (duration / 10);
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.floor(current) + '+';
            setTimeout(updateCounter, 10);
        } else {
            element.textContent = target + '+';
        }
    };
    
    updateCounter();
};

// Trigger counters when stats section is visible
const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            const numbers = entry.target.querySelectorAll('h3');
            numbers.forEach(num => {
                const text = num.textContent;
                const target = parseInt(text.replace(/[^0-9]/g, ''));
                animateCounter(num, target);
            });
            entry.target.dataset.animated = 'true';
            statObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const aboutStats = document.querySelector('.about-stats');
if (aboutStats) {
    statObserver.observe(aboutStats);
}

// Smooth scroll to sections
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            const target = document.querySelector(href);
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Progress bar animation
const progressBars = document.querySelectorAll('.progress');
const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'progressFill 1.5s ease forwards';
            progressObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

progressBars.forEach(bar => progressObserver.observe(bar));

// Add keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        navLinks.classList.remove('active');
    }
});

console.log('Charity Website Loaded Successfully');
