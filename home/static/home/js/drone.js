$(document).ready(function () {
    // Define video sources for different screen sizes
    const videoSources = {
        fullHD: 'home/video/drone-background-video-1080p.mp4', // For desktops (1920x1080)
        hd: 'home/video/drone-background-video-720p.mp4',     // For tablets/smaller screens (1280x720)
        lowRes: 'home/video/drone-background-video-480p.mp4'  // For mobile devices or low performance (854x480)
    };
    // Function to set video quality
    function setVideoDroneQuality() {
        const screenWidth = $(window).width(); // Get screen width
        const $sourceElement = $('#drone-video');

        console.log($('#drone-video').data("static"));
        // Determine the appropriate video source
        if (screenWidth >= 1920) {
            $sourceElement.attr('src', $('#drone-video').data("static") + videoSources.fullHD);
        } else if (screenWidth >= 1280) {
            $sourceElement.attr('src', $('#drone-video').data("static") + videoSources.hd);
        } else {
            $sourceElement.attr('src', $('#drone-video').data("static") + videoSources.lowRes);
        }

        // Reload the video
        $('#drone-video')[0].load();
    }

    // Set video quality on page load
    setVideoDroneQuality();

    // Optional: Adjust on window resize
    $(window).resize(setVideoDroneQuality);
});