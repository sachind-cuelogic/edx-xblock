/* Javascript for TestXBlock. */
function TestXBlock(runtime, element) {

   $('.action-save').on('click', function() {
    debugger
        var data = {
            'eassy_title': $('#eassyQuestion').val(),
            'eassy_text': $('#eassyText').val()
        };
        // runtime.notify('save', {state: 'start'});
        
        var handlerUrl = runtime.handlerUrl(element, 'student_submit');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                alert("saved successFully!!!")
                console.log(data)
                // runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                // window.location.reload(false);
            } else {
                // runtime.notify('error', {msg: response.message})
            }
        });
    });

    $(element).find('.action-cancel').bind('click', function() {
        // runtime.notify('cancel', {});
    });
}
