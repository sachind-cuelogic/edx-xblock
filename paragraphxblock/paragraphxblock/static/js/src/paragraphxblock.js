/* Javascript for ParagraphXBlock. */
function ParagraphXBlock(runtime, element, settings) {



    /*$('p').html(function(index, oldHtml) {
        return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" data-toggle="tooltip">$1</span>')
    });
    $('span').click(function(event) {

        alert(event.target.innerHTML);

    });*/
    
    $('.submit', element).click(function(e) {
        e.preventDefault();
        debugger;
        var text = $('textarea').val();
        console.log("para",text)


        var handlerUrlb = runtime.handlerUrl(element, 'post_paragraph_studio');
        $.ajax({
            type: "POST",
            url: handlerUrlb,
            data: JSON.stringify({ "course_id": course_id, "lesson_id": lesson_id, "paragraph": text }),
            dataType: "json",
            success: function(result) {
                console.log("paragraph updated");
    /*             post_changes(runtime, element, settings);*/
            },
            error: function(err) {
                //alert("Failure!!")
                console.log(err)
            }
        });

    });


}
