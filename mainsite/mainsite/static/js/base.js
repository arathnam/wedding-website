window.onload = function() {
    resize();
}

$(window).resize(function() {
    resize();
});

function resize() {
    $('#main').css({
        left: ($(window).width() - $('#main').outerWidth())/2,
        top: ($(window).height() - $('#main').outerHeight())/2
    });
}

$(function() {
    $('#main img').load(function() {
        $(this).css('visibility', 'visible');
    });
});
