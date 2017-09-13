function post_changes(runtime, element, settings) {
    var course_id = settings.course_id
    var lesson_id = settings.lesson_id
    var scenario_id = settings.scenario_id
    var handlerUrla = runtime.handlerUrl(element, 'get_paragraph_studio');
    $.ajax({
        type: "POST",
        url: handlerUrla,
        data: JSON.stringify({ "course_id": course_id, "lesson_id": lesson_id }),
        dataType: "json",
        success: function(result) {

            $('textarea#para').val(result.paragraph);
            var text = $('textarea').val();
            $('.para').html(text);


            var deferred = dividepara(runtime, element, settings);
            $.when(deferred).done(function() {

                var keys = result.keys
                for (i = 0; i < keys.length; i++) {
                    var key = keys[i].keyword.toLowerCase();
                    $("[data-word='" + key + "']").css("color", "blue");
                }
            });

        },
        error: function(err) {
            //alert("Failure!!")
            console.log(err)
        }
    });
}


function AddParagraphXBlock(runtime, element, settings) {

    $(function($) {
        var course_id = settings.course_id
        var lesson_id = settings.lesson_id
        var scenario_id = settings.scenario_id
/*        post_changes(runtime, element, settings);*/
        console.log("cid==>",course_id)
        console.log("lid==>",lesson_id)
        console.log("sid==>",scenario_id)
        // To update paragraph into table
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

        // To update defination of selected word
        var handlerUrld = runtime.handlerUrl(element, 'post_keyword_studio');
        $('#send', element).click(function(eventObject) {
            eventObject.preventDefault();
            var key = $('input#key').val();
            var def = $('input#def').val();
            if (def) {

                $.ajax({
                    type: "POST",
                    url: handlerUrld,
                    data: JSON.stringify({ "course_id": course_id, "lesson_id": lesson_id, "keyword": key, "defination": def }),
                    dataType: "json",
                    success: function(result) {
                        $('#def').val("");
                        var key = result.keyword.toLowerCase();

                        $("[data-word='" + key + "']").css("color", "blue");

                        //var key_id = "span#" + key
                        //$(key_id).css("color", "blue");

                        //alert("defination updated"); 
                        // var url =  "/course/" + scenario_id + "/" + course_id + "/" + lesson_id + "/" 
                        // window.location.href = url;            
                    },
                    error: function(err) {
                        //alert("Failure!!")
                        console.log(err)
                    }
                });
                $(this).parent().parent().hide();
            } else {
                $('#send').notify("plz fill the defination", { position: "top" });

            }
        });

        // To clear paragraph
        $("input.cancel").click(function(eventObject) {
            eventObject.preventDefault();
            $('textarea#para').val("");

        });



    }(jQuery));

}
