window.onload = function() {
    resize();
    if ($('#loading-icon').length) {
        $('#loading-icon').hide();
    }
    document.getElementById('hide-till-load').style.display = 'none'; 
}

$(window).resize(function() {
    resize();
});

function resize() {
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
