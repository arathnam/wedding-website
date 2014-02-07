var rsvp_table;

$(document).ready(function() {
    $('#rsvp-table-container').submit( function() {
        var rsvp_data = $('input', rsvp_table.fnGetNodes()).serialize();
        alert("The following data would have been submitted to the server: \n\n" + rsvp_data);
        return false;
    });

    rsvp_table = $('#rsvp-table-container').dataTable();
}
);
