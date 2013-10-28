window.onload = function() {
    resize();
}

$(window).resize(function() {
    resize();
});

function resize() {
    var element = document.getElementById('event-container');
    var style = window.getComputedStyle(element);
    var event_container_height = parseInt(style.getPropertyValue('height'));
    var img = document.getElementById('img-container-image');
    var image_height = img.clientHeight;
    $('#img-container').css({
        top: (event_container_height - image_height)/2
    });
}
