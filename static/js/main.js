// create a dynamic year and insert into the js-year span
document.getElementById('js-year').innerHTML = new Date().getFullYear();

// // Check if Masonry is loaded
// document.addEventListener("DOMContentLoaded", function() {
//     if (typeof Masonry !== 'undefined') {
//         // Initialize Masonry after all images have loaded
//         // setTimeout(() => {
//             var container = document.querySelector('.row').imagesLoaded(container, function() {
//                 new Masonry(container, {
//                     itemSelector: '.col-6',
//                     percentPosition: true
//                 });
//             });
//             // }, 1000)
//     }
// });


