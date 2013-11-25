window.onload = function() {
    resize();
}

$(window).resize(function() {
    resize();
});

function resize() {
    if (($('#footer-container').is(':visible'))) {
        $('#main').css({
            left: ($(window).width() - $('#main').outerWidth())/2,
            top: ($(window).height() - $('#main').outerHeight() - $('#footer-container').outerHeight())/2
        });
    } else {
        $('#main').css({
            left: ($(window).width() - $('#main').outerWidth())/2,
            top: ($(window).height() - $('#main').outerHeight())/2
        });
    }
}

$(function() {
    $('#main img').load(function() {
        $(this).css('visibility', 'visible');
    });
});
