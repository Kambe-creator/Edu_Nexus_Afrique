// Hamburger Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
});
document.addEventListener('DOMContentLoaded', () => {
    // Handle Edu-Konnect Click
    const eduKonnect = document.getElementById('edu-konnect');
    const eduSubsections = document.getElementById('edu-subsections');
    eduKonnect.addEventListener('click', () => {
        eduSubsections.classList.toggle('active');
    });

    // Handle Mtaa Legit Click
    const mtaaLegit = document.getElementById('mtaa-legit');
    const mtaaSubsections = document.getElementById('mtaa-subsections');
    mtaaLegit.addEventListener('click', () => {
        mtaaSubsections.classList.toggle('active');
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const toggleSubsections = (id) => {
        const subsections = document.getElementById(id);
        subsections.classList.toggle('hidden');
        subsections.classList.toggle('visible');
    };

    // Add event listeners to toggle buttons
    document.querySelectorAll('.toggle-btn').forEach((button) => {
        button.addEventListener('click', (event) => {
            const parentSection = event.target.parentElement;
            const subsectionId = parentSection.querySelector('.subsections').id;
            toggleSubsections(subsectionId);
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const toggleSubsections = (id) => {
        const subsections = document.getElementById(id);
        subsections.classList.toggle('hidden');
        subsections.classList.toggle('visible');
    };

    // Add event listeners to toggle buttons
    document.querySelectorAll('.toggle-btn').forEach((button) => {
        button.addEventListener('click', (event) => {
            const parentSection = event.target.parentElement;
            const subsectionId = parentSection.querySelector('.subsections').id;
            toggleSubsections(subsectionId);
        });
    });
});

// Toggle visibility of subsections
function toggleSubsections(subsectionId) {
    const subsection = document.getElementById(subsectionId);
    subsection.classList.toggle("hidden");
    subsection.classList.toggle("visible");
}


