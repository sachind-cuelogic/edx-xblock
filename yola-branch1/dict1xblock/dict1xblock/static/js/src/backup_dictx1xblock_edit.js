//popup form to store defination of particular word
function dividepara(runtime, element, settings) {
    $('.para').html(function(index, oldHtml) {
          return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" id=$1>$1</span>')
      })

    $(".word").click(function(event) {
      $("#contactdiv").css("display", "block");
      $("#key").val(event.target.innerHTML);
      var result=event.target.innerHTML
      popupform(runtime, element, settings,result);
    });
 }

// close the popup form and reset form's fields  
function popupform(runtime, element, settings,result) {

    var course_id = settings.course_id
    var lesson_id = settings.lesson_id
    var scenario_id = settings.scenario_id

    // To fetch defination of selected word
    var handlerUrlc = runtime.handlerUrl(element, 'get_keyword_studio'); 
   
    $.ajax({
                type: "POST",
                url: handlerUrlc,
                data: JSON.stringify({"course_id": course_id, "lesson_id": lesson_id ,"keyword":result}),
                dataType: "json",
                success: function(result){  
                if (result.key_defination == "none") 
                {
                  $('#def').val("");
                }  
                else
                {
                  $('#def').val(result.key_defination);
                }             
                  
                },
                error: function(err) {
                    //alert("Failure!!")
                    console.log(err)
                }
    });


    // To update defination of selected word
    var handlerUrld = runtime.handlerUrl(element, 'post_keyword_studio');
    $('#send', element).click(function(eventObject) {
              eventObject.preventDefault();
              var key = $('input#key').val();
              var def=$('input#def').val();
              if (def)
              {
                 
                $.ajax({
                type: "POST",
                url: handlerUrld,
                data: JSON.stringify({"course_id": course_id, "lesson_id": lesson_id ,"keyword":key,"defination":def}),
                dataType: "json",
                success: function(){
                  $('#def').val("");
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
            }
            else
            {
              $('#send').notify("plz fill the defination", { position:"top" });
              
            }
        }); 
   
    $("img#cancel").click(function() {
        $(this).parent().parent().hide();

    });
    $("input#reset").click(function() {
       $('input#def').val("");

    });

 }

// To fetch paragraph from database
function post_changes(runtime, element, settings)
{
  var course_id = settings.course_id
  var lesson_id = settings.lesson_id
  var scenario_id = settings.scenario_id
  var handlerUrla = runtime.handlerUrl(element, 'get_paragraph_studio');
        $.ajax({
                type: "POST",
                url: handlerUrla,
                data: JSON.stringify({"course_id": course_id, "lesson_id": lesson_id }),
                dataType: "json",
                success: function(result){

                  $('textarea#para').val(result.paragraph);
                  var text = $('textarea').val();
                  $('.para').html(text);
                  

                    var deferred = dividepara(runtime, element, settings); 
                    $.when(deferred).done(function() 
                    {

                      var keys = result.keys
                      for (i = 0; i < keys.length; i++) 
                     {
                        var key = keys[i].keyword
                        var key_id="span#"+key
                        $(key_id).css("color", "blue");
                      }
                    });
                 
                  

                  // dividepara(runtime, element, settings); 

                  // var keys = result.keys
                  // for (i = 0; i < keys.length; i++) 
                  // {
                  //   var key = keys[i].keyword
                  //   var key_id="span#"+key
                  //   $(key_id).css("color", "blue");
                  // }
                },
                error: function(err) {
                    //alert("Failure!!")
                    console.log(err)
                }
              });
}



function Dict1XBlockEditBlock(runtime, element, settings) {

  $(function($) {

        var course_id = settings.course_id
        var lesson_id = settings.lesson_id
        var scenario_id = settings.scenario_id
        post_changes(runtime, element, settings);

        // To update paragraph into table
  			$('.submit', element).click(function(eventObject) {
              eventObject.preventDefault();
  				    var text = $('textarea').val();

              
              var handlerUrlb = runtime.handlerUrl(element, 'post_paragraph_studio'); 
              $.ajax({
                type: "POST",
                url: handlerUrlb,
                data: JSON.stringify({"course_id": course_id, "lesson_id": lesson_id ,"paragraph":text}),
                dataType: "json",
                success: function(result){                 
                  console.log("paragraph updated")
                },
                error: function(err) {
                    //alert("Failure!!")
                    console.log(err)
                }
              });

        }); 

       
        
        // To clear paragraph
        $("input.cancel").click(function(eventObject) 
              {
                  eventObject.preventDefault();
                  $('textarea#para').val("");
                  
              });


  			
    }(jQuery));

}


        