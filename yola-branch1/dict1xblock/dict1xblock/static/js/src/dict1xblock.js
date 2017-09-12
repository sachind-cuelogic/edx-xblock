/* Javascript for DictXBlock. */
/* 
 $('p').html(function(index, oldHtml) {
    return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" data-toggle="tooltip">$1</span>')
 });

$('span').hover(function(event){
     var word=event.target.innerHTML;
     $('span').attr('title', word);
    
});
*/

/*
$(function(){
            $(document.body).KOglossaryLinks({
                sourceURL    : 'https://rawgit.com/mrmartineau/KOglossaryLinks/master/glossaryTerms.json',
                element      : '.glossaryLink',
                tooltipwidth : 260,
                debug        : true
            });
        });
        
 */

function Dict1XBlock(runtime, element, settings) {

    /*$('p').html(function(index, oldHtml) {
        return oldHtml.replace(/\b(\w+?)\b/g, '<span class="word" data-toggle="tooltip">$1</span>')
    });
    $('span').click(function(event) {

        alert(event.target.innerHTML);

    });*/

    function updatecourse(result) {

        var courses = result.course
        var scenario_id = settings.scenario_id
        var view = settings.view
        for (i = 0; i < courses.length; i++) 
        {
            var x = courses[i].id
            if (view == "student")
            {
                var url = "\"" + "/course/" + scenario_id + "/" + x + "\""
            }
            else
            {
                var url = "\"" + "/course/studio/" + scenario_id + "/" + x + "\""
                //var url='\"{% url \" workbench_show_studio_scenario\" '+scenario_id+' '+x+' %}\"'
            }
            
            $('ul').append('<li><a href=' + url + '>' + courses[i].course + '</a></li>'); + '<br>';
            // console.log(courses[i].course)
            //$( 'ul').append( "<li><a href='/scenario/courses/'>"+courses[i]+"</a></li>" ); + "<br>";
        }

    }

    function updatelesson(result) {

        var lessons = result.lessons
        var course_id = settings.course_id
        var scenario_id = settings.scenario_id        
        var view = settings.view
        var i = 0;
        if (i < lessons.length) {
            var x = lessons[i].id
            if (view == "student")
            {
                var url = "\"" + "/course/" + scenario_id + "/" + course_id + "/" + x + "\""
            }
            else
            {
                var url = "\"" + "/course/studio/" + scenario_id + "/" + course_id + "/" + x + "\""
            }
            
            $('ul').append('<li>Lesson id : ' + lessons[i].id + '<br>lesson name : <a href=' + url + '>' + lessons[i].lesson + '</a></li>'); + '<br><br>';

        }

    }

    function updatepara(result) {
        var para = result.paragraph
        $('ul').append('<li><b>Paragraph</b> : <p>' + para.paragraph + '</p></li>'); + '<br><br>';

        var keywordDictionary = result.keys;
            $('body p').keywordize({
                dictionary: keywordDictionary
            }, function() {
                $('[title]').popup();
            });
    }
    // var handlerUrl = runtime.handlerUrl(element, 'post_paragraph');

    // $('h1', element).click(function(eventObject) {
    //     $.ajax({
    //         type: "POST",
    //         url: handlerUrl,
    //         data: JSON.stringify({}),
    //         dataType: "json",
    //         success: updateCount, 
    //         error : function(err){
    //             alert("Failure!!")
    //             console.log(err)
    //         }
    //     });
    // });



    $(function($) {
        var course_id = settings.course_id
        var lesson_id = settings.lesson_id
        var scenario_id = settings.scenario_id
        var view = settings.view
        if (lesson_id) {
            var handlerUrla = runtime.handlerUrl(element, 'post_paragraph');

            $.ajax({

                type: "POST",
                url: handlerUrla,
                data: JSON.stringify({ "course_id": course_id, "lesson_id": lesson_id }),
                dataType: "json",
                success: updatepara,
                error: function(err) {
                    // alert("Failure!!")
                    console.log(err)
                }
            });
        } else if (course_id) {
            var handlerUrlb = runtime.handlerUrl(element, 'post_lessons');
            $.ajax({
                type: "POST",
                url: handlerUrlb,
                data: JSON.stringify({ "course_id": course_id }),
                dataType: "json",
                success: updatelesson,
                error: function(err) {
                    // alert("Failure!!")
                    console.log(err)
                }
            });
        } else {
            var handlerUrlc = runtime.handlerUrl(element, 'post_courses');
            $.ajax({
                type: "POST",
                url: handlerUrlc,
                data: JSON.stringify({}),
                dataType: "json",
                success: updatecourse,
                error: function(err) {
                    // alert("Failure!!")
                    console.log(err)
                }
            });
        }

    }(jQuery));
}
