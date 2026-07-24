function showPage(pageId) {
    // Hide all sections by adding the 'hidden' class
    document.querySelectorAll('.content').forEach(section => {
        section.classList.add('hidden');
    });

    // Show the section with the provided pageId by removing the 'hidden' class
    document.getElementById(pageId).classList.remove('hidden');
}