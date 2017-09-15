/* Javascript for ParagraphXBlock. */

function divideparagraph_inword(runtime, element) {

    var p = $('.paragraph');
    var modal = document.getElementById('myModal');

    p.html(function(index, oldHtml) {
        return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" key-word=$1>$1</span>')
    });

    $("[key-word]").each(function(index) {
        $(this).attr('key-word', $(this).attr('key-word').toLowerCase())

    });

    $(".word").click(function(event) {
        key = event.target.innerHTML;
        getkeywordstatus(runtime, element, key);
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
    var modal = document.getElementById('myModal');
    var handlerUrlc = runtime.handlerUrl(element, 'get_keyword');
    var lesson_id = $('.paragraph-div div').attr('id')
    $.ajax({
        type: "POST",
        url: handlerUrlc,
        data: JSON.stringify({"lesson_id": lesson_id, "keyword": key }),
        dataType: "json",
        success: function(result) {
            if (result.key_defination == "none") {

                $('#defination').val("");
            } 
            else 
            {   
                modal.style.display = "block";
                $('#keyword').val(result.keyword);
                $('#defination').val(result.key_defination);
            }

        },
        error: function(err) {
            console.log(err)
        }
    });


}


function ParagraphXBlock(runtime, element) {
    $(function($) {
      
    var lesson_id = $('.paragraph-div div').attr('id')
    var handlerUrla = runtime.handlerUrl(element, 'update_highlighted_keys');
    $.ajax({
        type: "POST",
        url: handlerUrla,
        data: JSON.stringify({"lesson_id": lesson_id }),
        dataType: "json",
        success: function(result) {

            $('.paragraph').html(result.paragraph);

            var divided_words = divideparagraph_inword(runtime, element);
            $.when(divided_words).done(function() {

                var keys = result.keys
                for (i = 0; i < keys.length; i++) {
                    var key = keys[i].keyword.toLowerCase();
                    $("[key-word='" + key + "']").css("color", "red");
                }
            });
          
        },
        error: function(err) {
         
            console.log(err)
        }
    });

    }(jQuery));
}
