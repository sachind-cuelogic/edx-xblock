/* Javascript for ReferenceXBlock. */
function ReferenceXBlock(runtime, element) {

    var handlerUrl = runtime.handlerUrl(element,'reference_data');

    $('#submit').on('click', function() {

        var refname = $('#id_name').val()
        var reflink = $('#id_link').val()
        var reftype = $('#id_ref_type').val()
        var refdesc = $('#id_description').val()
        var refstatus = $('#id_ref_status').val()

        $.ajax({

            type: 'POST',
            url: handlerUrl,
            data: JSON.stringify({
                'ref_name':refname,
                'ref_link':reflink,
                'ref_type':reftype,
                'ref_description':refdesc,
                'ref_status':refstatus
            }),
            success: function(result) 
            {

            }
        });

    });
    $('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
        });
}