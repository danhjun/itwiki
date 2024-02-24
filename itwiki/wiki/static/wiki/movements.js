document.addEventListener('DOMContentLoaded', function() {
    // Select all article-box elements
    const boxes = document.querySelectorAll('.article-box');

    // Add hover event listeners to each box
    boxes.forEach(box => {
        box.addEventListener('mouseenter', function() {
            // When the mouse enters the box, zoom in the image
            const img = this.querySelector('img');
            img.style.transform = 'scale(1.1)'; // Adjust scale value to control zoom level
            img.style.transition = 'transform 0.5s ease'; // Smooth transition
        });

        box.addEventListener('mouseleave', function() {
            // When the mouse leaves the box, reset the image zoom
            const img = this.querySelector('img');
            img.style.transform = 'scale(1)';
        });
    });
});