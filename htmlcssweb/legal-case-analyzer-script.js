// Loading Screen Animation
document.addEventListener('DOMContentLoaded', function() {
    const loadingScreen = document.getElementById('loading-screen');
    
    // Simulate loading time (you can replace this with actual loading logic)
    setTimeout(() => {
        loadingScreen.style.opacity = '0';
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500);
    }, 2000);
});

// Stats Counter Animation
function animateStats() {
    const stats = document.querySelectorAll('.stat-number[data-count]');
    
    stats.forEach(stat => {
        const targetValue = parseInt(stat.getAttribute('data-count'));
        const duration = 2000; // Animation duration in milliseconds
        const startTime = Date.now();
        const startValue = 0;
        
        function updateCount() {
            const currentTime = Date.now();
            const elapsedTime = currentTime - startTime;
            
            if (elapsedTime < duration) {
                const progress = elapsedTime / duration;
                // Use easeOutQuad for smoother animation
                const easeProgress = 1 - (1 - progress) * (1 - progress);
                const currentValue = Math.floor(startValue + (targetValue - startValue) * easeProgress);
                stat.textContent = currentValue;
                requestAnimationFrame(updateCount);
            } else {
                stat.textContent = targetValue;
            }
        }
        
        updateCount();
    });
}

// Feature Cards Animation
function animateFeatureCards() {
    const featureCards = document.querySelectorAll('.feature-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add animation with delay based on index
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
                
                // Unobserve after animation
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    featureCards.forEach(card => {
        observer.observe(card);
    });
}

// Dashboard image hover effect
function initDashboardPreview() {
    const dashboardImg = document.querySelector('.dashboard-img');
    const container = document.querySelector('.dashboard-preview');
    
    if (dashboardImg && container) {
        container.addEventListener('mousemove', (e) => {
            const rect = container.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Convert coordinates to rotation angles
            const rotateY = ((x / rect.width) - 0.5) * 10; // -5 to 5 degrees
            const rotateX = ((y / rect.height) - 0.5) * -10; // 5 to -5 degrees
            
            dashboardImg.style.transform = `perspective(1000px) rotateY(${rotateY}deg) rotateX(${rotateX}deg)`;
        });
        
        container.addEventListener('mouseleave', () => {
            dashboardImg.style.transform = 'perspective(1000px) rotateY(-5deg) rotateX(0)';
        });
    }
}

// Handle smooth scrolling for navigation links
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const targetId = link.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Account for navbar height
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Initialize all functions when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Wait for loading screen to finish
    setTimeout(() => {
        animateStats();
        animateFeatureCards();
        initDashboardPreview();
        initSmoothScroll();
    }, 2500);
    
    // Add scroll animation for stat counter
    const statsSection = document.querySelector('.stats');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    if (statsSection) {
        observer.observe(statsSection);
    }
    
    // Handle authentication buttons
    const loginBtn = document.querySelector('.btn-login');
    const signupBtn = document.querySelector('.btn-signup');
    const ctaSignupBtn = document.querySelector('.cta-buttons .btn-primary');
    const demoBtn = document.querySelector('.cta-buttons .btn-secondary');
    const freeAccessBtn = document.querySelector('.free-access .btn-primary');
    
    // Event listeners are kept but alert messages are removed
    if (loginBtn) {
        loginBtn.addEventListener('click', () => {
            // Alert removed
        });
    }
    
    if (signupBtn) {
        signupBtn.addEventListener('click', () => {
            // Alert removed
        });
    }
    
    if (ctaSignupBtn) {
        ctaSignupBtn.addEventListener('click', () => {
            // Alert removed
        });
    }
    
    if (demoBtn) {
        demoBtn.addEventListener('click', () => {
            // Alert removed
        });
    }
    
    if (freeAccessBtn) {
        freeAccessBtn.addEventListener('click', () => {
            // Alert removed
        });
    }
});