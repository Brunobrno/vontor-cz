$(document).ready(function() {
    const $stickyElm = $('nav');
    const stickyOffset = $stickyElm.offset().top;

    $(window).on('scroll', function() {
        
        const isSticky = $(window).scrollTop() > stickyOffset;
        //console.log("sticky: " + isSticky);

        $stickyElm.toggleClass('isSticky-nav', isSticky);
    });

    $('#toggle-nav').click(function () {
        $('nav ul').toggleClass('nav-open');
        $('#toggle-nav').toggleClass('toggle-nav-rotated');
    });
});
