
function getkeywordstatus(runtime, element, key) {

    var handlerUrlc = runtime.handlerUrl(element, 'get_keyword');
    var lesson_id = $('textarea').attr('id')
    $.ajax({
        type: "POST",
        url: handlerUrlc,
        data: JSON.stringify({"lesson_id": lesson_id, "keyword": key }),
        dataType: "json",
        success: function(result) {
            console.log("result==>",result)
            if (result.key_defination == "none") {
                $('#defination').val("");
            } else {
                $('#defination').val(result.key_defination);
            }

        },
        error: function(err) {
            console.log(err)
        }
    });


}


function EditParagraphXBlock(runtime, element) {


    var p = $('p#updated-para');

    p.html(function(index, oldHtml) {
        return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" key-word=$1>$1</span>')
    });

    $("[key-word]").each(function(index) {
        $(this).attr('key-word', $(this).attr('key-word').toLowerCase())
/*        console.log($(this).attr('key-word'))*/
    });
    var modal = document.getElementById('myModal');
    $(".word").click(function(event) {
        key = event.target.innerHTML;
        $('#keyword').val(key)
        getkeywordstatus(runtime, element, key);
        modal.style.display = "block";
        var result = event.target.innerHTML
    });

    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
        modal.style.display = "none";
    }
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    $(function($) {
        $('.submit', element).click(function(eventObject) {
            eventObject.preventDefault();
            var text = $('textarea').val();
            var lesson_id = $('textarea').attr('id')
            console.log("lid==>",lesson_id)

            var handlerUrlb = runtime.handlerUrl(element, 'post_paragraph_studio');
            $.ajax({
                type: "POST",
                url: handlerUrlb,
                data: JSON.stringify({"lesson_id": lesson_id, "paragraph": text }),
                dataType: "json",
                success: function(result) {
                    console.log("paragraph updated");
                    $('.show-paragraph .updated-para').text(result.new_para);   
                    location.reload(); 
                    console.log(result);
                },
                error: function(err) {
                    console.log(err)
                }
            });

        });

        $('#submit-key', element).click(function(eventObject) {
            eventObject.preventDefault();
            var key = $('#keyword').val();
            console.log("key==>",key)
            var def = $('#defination').val();
            console.log("def==>",def)
            var modal = document.getElementById('myModal');
            var lesson_id = $('textarea').attr('id')
            console.log("lesson_id==>",lesson_id)
            var handlerUrld = runtime.handlerUrl(element, 'post_keyword');
            
            if (def) {

                $.ajax({
                    type: "POST",
                    url: handlerUrld,
                    data: JSON.stringify({ "lesson_id": lesson_id, "keyword": key, "defination": def }),
                    dataType: "json",
                    success: function(result) {
                        modal.style.display = "none";
                        var key = result.keyword.toLowerCase();

                        $("[key-word='" + key + "']").css("color", "red");
                    },
                    error: function(err) {
                        console.log(err)
                    }
                });
            } else {
                alert("plz fill the defination");

            }
        });

    }(jQuery));






}

