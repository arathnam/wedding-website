window.onload = function() {
    resize();
    document.getElementById('hide-till-load').style.display = 'none'; 
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

    // HACK: For the individual event pages.
    if ($('#event-container').length) {
        if ($('.shadowed').length) {
            $('#img-container').css({
                top: ($('#event-container').height() - $('.img-container-image').height() - 30) / 2
            });
        } else {
            $('#img-container').css({
                top: ($('#event-container').height() - $('.img-container-image').height()) / 2
            });
        }
    }
}

$(function() {
    $('#main img').load(function() {
        $(this).css('visibility', 'visible');
    });
});
