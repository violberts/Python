function toggleSection(header) {
    const section = header.parentElement;
    const isActive = section.classList.contains('active');

    // Закрыть все секции
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));

    // Открыть текущую секцию, если она была закрыта
    if (!isActive) {
        section.classList.add('active');
    }
}

// Открыть первую секцию по умолчанию
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.section').classList.add('active');
});