document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const revealItems = Array.from(document.querySelectorAll('.reveal'));
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    body.classList.add('js-ready');

    if (!revealItems.length) {
        return;
    }

    if (reduceMotion) {
        revealItems.forEach((item) => item.classList.add('reveal-visible'));
        return;
    }

    revealItems.forEach((item) => {
        const delay = item.dataset.revealDelay;
        if (delay) {
            item.style.setProperty('--reveal-delay', `${delay}ms`);
        }
    });

    let ticking = false;

    const updateRevealState = () => {
        const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
        const visibleStart = viewportHeight * 0.12;
        const visibleEnd = viewportHeight * 0.92;

        revealItems.forEach((item) => {
            const rect = item.getBoundingClientRect();
            const isVisible = rect.top < visibleEnd && rect.bottom > visibleStart;
            item.classList.toggle('reveal-visible', isVisible);
        });

        ticking = false;
    };

    const requestRevealUpdate = () => {
        if (ticking) {
            return;
        }

        ticking = true;
        window.requestAnimationFrame(updateRevealState);
    };

    window.addEventListener('scroll', requestRevealUpdate, { passive: true });
    window.addEventListener('resize', requestRevealUpdate);
    window.addEventListener('orientationchange', requestRevealUpdate);

    requestRevealUpdate();
});
