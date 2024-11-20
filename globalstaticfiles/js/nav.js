$(document).ready(function() {
    const $stickyElm = $('nav');
    const stickyOffset = $stickyElm.offset().top;

    $(window).on('scroll', function() {
        const isSticky = $(window).scrollTop() > stickyOffset;
        $stickyElm.toggleClass('isSticky-nav', isSticky);
    });
});
