// Всплывающие подсказки для терминов программирования
const terms = document.querySelectorAll('.term');

terms.forEach(term => {
    term.addEventListener('mouseover', () => {
        const definition = term.getAttribute('data-definition');
        const tooltip = document.createElement('div');
        tooltip.classList.add('tooltip');
        tooltip.textContent = definition;
        document.body.appendChild(tooltip);

        const rect = term.getBoundingClientRect();
        tooltip.style.left = `${rect.left + rect.width / 2}px`;
        tooltip.style.top = `${rect.top - tooltip.offsetHeight - 10}px`;
    });

    term.addEventListener('mouseout', () => {
        const tooltip = document.querySelector('.tooltip');
        if (tooltip) {
            tooltip.remove();
        }
    });
});
