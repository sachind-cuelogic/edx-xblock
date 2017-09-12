function TestXBlockEdit(runtime, element) {

   
    var a=$('#para_edit').val();
    var b = "there is no content";
    
    for (var i = 0, len = b.length; i < len; i++)
        if (a.charAt(i) != b.charAt(i)) 
        {
             $('li#show').show();
             $('li#edit').hide();
             $('#result').text(a);
        }
        else
        {
          $('li#show').hide();
          $('li#edit').show();
          $('#result').text(a);
        }

    var data = { };
    var handlerUrla = runtime.handlerUrl(element, 'get_keywords_studio');
    
    $.ajax({
        type: "POST",
        url: handlerUrla,
        data: JSON.stringify(data),
        dataType: "json",
        success: function(response) {

          var result=response.keywords  
          var text = $('#para_edit').val(); 
           for (i = 0; i < result.length; i++) 
        {
                var spn = '<span data-word=\"'+result[i].keyword.toLowerCase()+'\">' + result[i].keyword+ '</span>';
                $('#result').html($('#result').html().replace(result[i].keyword, spn));
                $("[data-word='" + result[i].keyword + "']").css("color", "blue");    
        }
            

        },
        error: function(err) {
            console.log(err)
        }
    });

    $(element).find('.action-cancel').bind('click', function() {
         runtime.notify('cancel', {});
    });

    $('#save').click(function(){
        $('li#show').show();
        $('li#edit').hide();

    });
    $('#edit_para').click(function(){
         $('li#show').hide();
        $('li#edit').show();

    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $('#edit_display_name').val(),
            'paragraph': $('#para_edit').val()
        };
        
         runtime.notify('save', {state: 'start'});
        
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                 runtime.notify('save', {state: 'end'});
                
            } else {
                 runtime.notify('error', {msg: response.message})
           
            }
        });
    });



      $('#send').click(function(e){
        e.preventDefault();
        var data = {
            'keyword': $('input#key').val(),
            'defination': $('input#def').val()
        };
        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'studio_send');

        $.ajax({
        type: "POST",
        url: handlerUrl,
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
                 $('#keyword').hide();
                 var x=result.key
                 var spn = '<span data-word=\"'+x.toLowerCase()+'\">' + x + '</span>';
                 $('#result').html($('#result').html().replace(x, spn));
                 $("[data-word='" + x + "']").css("color", "blue");
                 runtime.notify('save', {state: 'end'});

        },
        error: function(err) {
            runtime.notify('error', {msg: response.message})
        }
        });
    });

     $('#sel-textarea').click(function(){
      var x= getSelectedTextWithin(document.getElementById('result'));
      if (x == "")
        {
          console.log("plz click on paragraph give below");
        } 
      else {
        $('#def').val("");
        $("#key").val(x);
        $('#keyword').show();
      }      
        
    });


    function getSelectedTextWithin(el) {
    var selectedText = "";
    if (typeof window.getSelection != "undefined") {
        var sel = window.getSelection(), rangeCount;
        if ( (rangeCount = sel.rangeCount) > 0 ) {
            var range = document.createRange();
            for (var i = 0, selRange; i < rangeCount; ++i) {
                range.selectNodeContents(el);
                selRange = sel.getRangeAt(i);
                if (selRange.compareBoundaryPoints(range.START_TO_END, range) == 1 && selRange.compareBoundaryPoints(range.END_TO_START, range) == -1) {
                    if (selRange.compareBoundaryPoints(range.START_TO_START, range) == 1) {
                        range.setStart(selRange.startContainer, selRange.startOffset);
                    }
                    if (selRange.compareBoundaryPoints(range.END_TO_END, range) == -1) {
                        range.setEnd(selRange.endContainer, selRange.endOffset);
                    }
                    selectedText += range.toString();
                }
            }
        }
    } else if (typeof document.selection != "undefined" && document.selection.type == "Text") {
        var selTextRange = document.selection.createRange();
        var textRange = selTextRange.duplicate();
        textRange.moveToElementText(el);
        if (selTextRange.compareEndPoints("EndToStart", textRange) == 1 && selTextRange.compareEndPoints("StartToEnd", textRange) == -1) {
            if (selTextRange.compareEndPoints("StartToStart", textRange) == 1) {
                textRange.setEndPoint("StartToStart", selTextRange);
            }
            if (selTextRange.compareEndPoints("EndToEnd", textRange) == -1) {
                textRange.setEndPoint("EndToEnd", selTextRange);
            }
            selectedText = textRange.text;
        }
    }
    return selectedText;
  }

   


}
