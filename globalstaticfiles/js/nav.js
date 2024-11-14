$(document).ready(function () {
    $('#toggleNav').click(function () {
        console.log("Nav Toggle");
        $('nav').toggleClass('nav-collapsed');
        $(this).find('img').toggleClass('toggle-icon-rotated');
    });
});