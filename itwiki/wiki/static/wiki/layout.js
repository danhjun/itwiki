// document.addEventListener("DOMContentLoaded", function() {
//     const containerWidth = document.querySelector('.article-list').offsetWidth;
//     const articleBoxes = document.querySelectorAll('.article-box');
//     let totalWidthNeeded = 0;

//     articleBoxes.forEach((box, index) => {
//         totalWidthNeeded += box.offsetWidth + 15; // Include the gap
//         if (index >= 2 && totalWidthNeeded > containerWidth) {
//             box.style.display = 'none';
//         }
//     });
// });