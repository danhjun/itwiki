document.addEventListener('DOMContentLoaded', function() {
    // Select the link using its class
    var viewMoreLink = document.querySelector('.view-more-link');

    // Check if the link exists to avoid errors
    if (viewMoreLink) {
        // Add mouseover event listener to change the link color to green
        viewMoreLink.addEventListener('mouseover', function() {
            this.style.color = '#918D8C';
        });

        // Add mouseout event listener to revert the link color back to its original color
        // Replace 'originalColor' with the actual color you want it to revert to
        // If using CSS :link { color: #yourColor; }, you can set this to 'inherit'
        viewMoreLink.addEventListener('mouseout', function() {
            this.style.color = 'inherit'; // or specify the color explicitly
        });
    }
});
