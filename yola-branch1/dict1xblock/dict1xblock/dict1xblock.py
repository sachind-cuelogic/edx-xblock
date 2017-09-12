"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from django.conf import settings
from xblock.core import XBlock
from xblock.fields import Scope, Integer,String,Dict,List
from xblock.fragment import Fragment
from workbench.models import Dict1XBlock_Course,Dict1XBlock_Lessons,Dict1XBlock_Key
from django.shortcuts import render
class Dict1XBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    course = List(help="list of course",scope=Scope.settings)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the Dict1XBlock, shown to students
        when viewing courses.
        """

        if context['lesson_id']:
            html = self.resource_string("static/html/paragraph.html")
            frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }            
            
        elif context['course_id']:
            html = self.resource_string("static/html/lesson.html")
            frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }

        else : 
            settings = {
            'scenario_id': context['scenario_id'],
            'view':  context['view'] 
            }
            html = self.resource_string("static/html/dict1xblock.html")
            frag = Fragment(html.format(self=self))
            
        frag.add_css(self.resource_string("static/css/popup.css"))
        frag.add_css(self.resource_string("static/css/transition.css"))
        frag.add_css(self.resource_string("static/css/dict1xblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/dict1xblock.js"))
        frag.add_javascript(self.resource_string("static/js/src/keywordize.js"))
        frag.add_javascript(self.resource_string("static/js/src/popup.js"))
        frag.add_javascript(self.resource_string("static/js/src/transition.js"))
        frag.initialize_js('Dict1XBlock',json_args=settings)
        return frag


    def studio_view(self, context):
        """
        Editing view in Studio
        """
        if context['lesson_id']:
            html = self.resource_string("static/html/dict1xblock_edit.html")
            frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }
            frag.add_css(self.resource_string("static/css/dict1xblock_edit.css"))
            frag.add_javascript(self.resource_string("static/js/src/dict1xblock_edit.js"))
            frag.initialize_js('Dict1XBlockEditBlock',json_args=settings)            
            
        elif context['course_id']:
            html = self.resource_string("static/html/lesson.html")
            frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }
            frag.add_javascript(self.resource_string("static/js/src/dict1xblock.js"))
            frag.initialize_js('Dict1XBlock',json_args=settings)

        else : 
            settings = {
            'scenario_id': context['scenario_id'],
            'view':  context['view'] 
            }
            html = self.resource_string("static/html/dict1xblock.html")
            frag = Fragment(html.format(self=self))
            frag.add_javascript(self.resource_string("static/js/src/dict1xblock.js"))
            frag.initialize_js('Dict1XBlock',json_args=settings)
        
        
        return frag 
   

    @XBlock.json_handler
    def get_paragraph_studio(self, data, suffix=''):
       
        para=Dict1XBlock_Lessons.objects.get(course=data["course_id"],id=data["lesson_id"])
        keywords=Dict1XBlock_Key.objects.filter(lesson=data["lesson_id"])
        keys=[]
        for i in keywords:
            key={}
            key["keyword"]=i.keyword
            keys.append(key)
        return {"paragraph":para.paragraph,"keys":keys}

    @XBlock.json_handler
    def post_paragraph_studio(self, data, suffix=''):

       lesson=Dict1XBlock_Lessons.objects.get(pk=data["lesson_id"]);
       lesson.paragraph=data["paragraph"]
       lesson.save();
       return {"hello":"hello"}

    @XBlock.json_handler
    def get_keyword_studio(self, data, suffix=''):
        
        lesson=Dict1XBlock_Lessons.objects.get(pk=data["lesson_id"])
        try:
            key=Dict1XBlock_Key.objects.get(lesson=lesson,keyword=data["keyword"].lower())
        except Dict1XBlock_Key.DoesNotExist:
            key = None
        if key:             
             return {"key_defination":key.defination}
        else:
            return {"key_defination":"none"}     
        
        

    @XBlock.json_handler
    def post_keyword_studio(self, data, suffix=''):

        lesson=Dict1XBlock_Lessons.objects.get(pk=data["lesson_id"])  
        try:
            key=Dict1XBlock_Key.objects.get(lesson=lesson,keyword=data["keyword"].lower())
            key.defination=data["defination"]
            
        except Dict1XBlock_Key.DoesNotExist:            
            key =Dict1XBlock_Key(lesson=lesson,keyword=data["keyword"].lower(),defination=data["defination"])
        key.save()
        return {"keyword":data["keyword"]}

    @XBlock.json_handler
    def post_courses(self, data, suffix=''):
        
        courses=Dict1XBlock_Course.objects.all()
        course=[]
        
        for crs in courses:
            dictionary={}
            dictionary["id"]=crs.id
            dictionary["course"]=crs.course_name                
            course.append(dictionary)
            
        self.course = list(course)
        return {"course": self.course}

    @XBlock.json_handler
    def post_lessons(self, data, suffix=''):
          
        lessons=Dict1XBlock_Lessons.objects.filter(course=data["course_id"] )
        lessonss=[]
        for i in lessons:
            lesson={}
            lesson["lesson"]=i.lesson_name
            lesson["id"]=i.id
            lessonss.append(lesson)
        return {"lessons":lessonss}

    @XBlock.json_handler
    def post_paragraph(self, data, suffix=''): 
           
        para=Dict1XBlock_Lessons.objects.get(course=data["course_id"],id=data["lesson_id"])
        keywords=Dict1XBlock_Key.objects.filter(lesson=data["lesson_id"])
        keys=[]
        for i in keywords:
            key={}
            key["keyword"]=i.keyword
            key["definition"]=i.defination
            keys.append(key)       

        paragraphs={}
        paragraphs["paragraph"]=para.paragraph
        return {"paragraph":paragraphs,"keys":keys} 
        
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Dict1XBlock",
             """<dict1xblock/>
             """),
            
        ]
