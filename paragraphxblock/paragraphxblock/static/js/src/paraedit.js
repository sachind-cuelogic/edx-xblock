
function divide_paragraph_inwords(runtime, element) {

    var p = $('p#new-para');
    var modal = document.getElementById('myModal');

    p.html(function(index, oldHtml) {
        return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" key-word=$1>$1</span>')
    });

    $("[key-word]").each(function(index) {
        $(this).attr('key-word', $(this).attr('key-word').toLowerCase())
    });
    $(".word").click(function(event) {

        key = event.target.innerHTML;
        $('#keyword').val(key)
        getkeywordstatus(runtime, element, key);
        modal.style.display = "block";
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

}

function getkeywordstatus(runtime, element, key) {

    var handlerUrlc = runtime.handlerUrl(element, 'get_keyword');
    var lesson_id = $('.add-paragraph input').attr('id')
    $.ajax({
        type: "POST",
        url: handlerUrlc,
        data: JSON.stringify({"lesson_id": lesson_id, "keyword": key }),
        dataType: "json",
        success: function(result) {

            if (result.key_defination == "none") {
                $('#defination').val("");
            } 
            else {
                $('#defination').val(result.key_defination);
            }
        },
        error: function(err) {
            console.log(err)
        }
    });
}


function update_highlighted_keys(runtime, element) {

    var lesson_id = $('.add-paragraph input').attr('id')
    var handlerUrla = runtime.handlerUrl(element, 'update_highlighted_keys');
    $.ajax({
        type: "POST",
        url: handlerUrla,
        data: JSON.stringify({"lesson_id": lesson_id }),
        dataType: "json",
        success: function(result) {

/*            $('textarea.para-textarea').val(result.paragraph);
            var text = $('textarea').val();*/
            $('.new-para').html(result.paragraph);

            var dividedword = divide_paragraph_inwords(runtime, element);
            $.when(dividedword).done(function() {
                var keys = result.keys
                for (i = 0; i < keys.length; i++) {
                    var key = keys[i].keyword.toLowerCase();
                    var def = keys[i].defination
                    $("[key-word='" + key + "']").css("color", "red");
                    $("[key-word='" + key + "']").attr('title',def);
                    $("[key-word='" + key + "']").tooltipster({
                                                       theme: 'tooltipster-punk'

                        });
                }
            });
        },
        error: function(err) {
         
            console.log(err)
        }
    });
}


function EditParagraphXBlock(runtime, element) {
    localStorage.clear();
    update_highlighted_keys(runtime, element);
    $(function($) {
        $('.submit', element).click(function(eventObject) {
            eventObject.preventDefault();
            var text = $('textarea').val();
            console.log("text==>", text);
            var lesson_id = $('textarea').attr('id')
            console.log("lid==>", lesson_id);
            var handlerUrlb = runtime.handlerUrl(element, 'post_paragraph');

            $.ajax({
                type: "POST",
                url: handlerUrlb,
                data: JSON.stringify({"lesson_id": lesson_id, "paragraph": text }),
                dataType: "json",
                success: function(result) {
                    console.log("result==>",result)
                    if(result.result == "fail")
                    {
                        alert("plz add paragraph")
                    }
                    else
                    {
                        $('.show-para .new-para').text(result.new_para);   

                        var url =  "/scenario/paragraphxblock.0/?lesson_id=" + lesson_id
                        console.log("url===>",url)
                        window.location.href = url; 
                        update_highlighted_keys(runtime, element);

                    }
                },
                error: function(err) {
                    console.log(err)
                }
            });

        });

        $('#submit-key', element).click(function(eventObject) {
            eventObject.preventDefault();
            var key = $('#keyword').val();
            console.log("key==>",key);
            var def = $.trim($('#defination').val());
            console.log("def==>",def);
            var modal = document.getElementById('myModal');
            var lesson_id = $('.add-paragraph input').attr('id')
            var handlerUrld = runtime.handlerUrl(element, 'post_keyword');
            
            if (def) {

                $.ajax({
                    type: "POST",
                    url: handlerUrld,
                    data: JSON.stringify({ "lesson_id": lesson_id, "keyword": key, "defination": def }),
                    dataType: "json",
                    success: function(result) {
                        console.log("result==>", result)
                        modal.style.display = "none";
                        var key = result.keyword.toLowerCase();
                        var def = result.defination
                        console.log("def",def)
                        $("[key-word='" + key + "']").css("color", "red");
                        $("[id='" + key + "']").attr('title',def);

                       /* $("#"+key+"").attr('title',def);*/

                      /*  $('#'+ i +'').attr('title', 'your new title');*/

                    },
                    error: function(err) {
                        console.log(err)
                    }
                });
            } 
            else {
                alert("plz fill the defination");
            }
        });

        $(".edit-para").click(function(event) {
            event.preventDefault();
            var para_id = $('.add-paragraph input').attr('id')
            console.log("para_id==>", para_id)
            var url =  "/scenario/paragraphxblock.0/?para_id=" + para_id
            console.log("url===>",url)
            window.location.href = url;  
        });


    }(jQuery));
}
