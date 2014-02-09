var rsvp_table;

$(document).ready(function() {
    $('#rsvp-form').submit( function() {
        var group_name = document.getElementById("group_name").value;
        var submit_rsvp_page_path = document.getElementById("submit_rsvp_page_path").value;
        var thank_you_page_path = document.getElementById("thank_you_page_path").value;

        var rsvp_data = $("input", rsvp_table.fnGetNodes()).serialize();
        if (rsvp_data.length > 0) {
           rsvp_data = rsvp_data.concat("&group_name=" + group_name);
        } else {
           rsvp_data = "group_name=" + group_name;
        }

        $.ajax({
            url: submit_rsvp_page_path,
            type: "POST",
            data: rsvp_data,
            dataType: 'json',
            success: function(data) {
                window.location.assign(thank_you_page_path);
            },
            error: function(data) {
            }
        });
        return false;
    });

    rsvp_table = $("#rsvp-table").dataTable( { "bPaginate": false,
                                               "bFilter": false,
                                               "bSort": false,
                                               "bInfo": false } );
}
);
