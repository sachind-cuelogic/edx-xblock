"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import json
from xblock.core import XBlock
from django.conf import settings

from xblock.fields import Integer, Scope
from xblock.fragment import Fragment
from workbench.models import Course, Lessons, KeyDefinition
from mako.template import Template
from .utils import loader


class ParagraphXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ParagraphXBlock, shown to students
        when viewing courses.
        """
        # import pdb; pdb.set_trace()

        print "context==>", context

        if context['course_id']:
            print "inside course"

            lessons_list = Lessons.objects.filter(course=context['course_id'])
            course = Course.objects.get(id=context['course_id'])
            context = {
            'lessons_list': lessons_list,
            'course':course,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }

            frag = Fragment(loader.render_template("static/html/lessons.html", context))
            # html = self.resource_string("static/html/lessons.html")
            # frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }            
            
        elif context['lesson_id']:
            print "inside lesson"

            paragraph = Lessons.objects.get(id=context['lesson_id'])

            context = {
            'paragraph': paragraph,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }

            frag = Fragment(loader.render_template("static/html/paragraph.html", context))

            # html = self.resource_string("static/html/paragraph.html")
            # frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }

            # frag.add_css(self.resource_string("static/css/paragraph.css"))
            
            frag.initialize_js('AddParagraphXBlock',json_args=settings)

        else : 

            settings = {
            'scenario_id': context['scenario_id'],
            'view':  context['view'] 
            }

            # print "sc id==>",context['scenario_id']

            course_list = Course.objects.all()
            context = {
            'course_list': course_list,
            'scenario_id': context['scenario_id']
            }

            frag = Fragment(loader.render_template("static/html/paragraphxblock.html", context))
            # html = self.resource_string("static/html/paragraphxblock.html")
            # frag = Fragment(html.format(self=self))

        # course_list = Course.objects.all()

        # context = {
        # 'course_list': course_list
        # }

        # settings = {
        #     'view':  context['view'] 
        #     }    
        # print "view==>",settings
        # print "course id==>",context['course_id']
        # html = self.resource_string("static/html/paragraphxblock.html")
        # frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/paragraphxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
        frag.add_javascript(self.resource_string("static/js/src/add_paragraph.js"))
        frag.initialize_js('ParagraphXBlock')
        return frag

        # fragment = Fragment(loader.render_template("static/html/paragraphxblock.html", context))
        # fragment.add_css(self.resource_string("static/css/paragraphxblock.css"))
        # fragment.add_javascript(
        # self.resource_string("static/js/src/paragraphxblock.js"))
        # fragment.initialize_js("ParagraphXBlock", json_args=settings)
        # return fragment

    def studio_view(self, context):
        """
        Editing view in Studio
        """
        if context['lesson_id']:



            paragraph = Lessons.objects.get(id=context['lesson_id'])

            context = {
            'paragraph': paragraph,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }

            frag = Fragment(loader.render_template("static/html/paraedit.html", context))
            frag.add_css(self.resource_string("static/css/paraedit.css"))

            # html = self.resource_string("static/html/paraedit.html")
            # frag = Fragment(html.format(self=self))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            # 'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }
            frag.add_css(self.resource_string("static/css/paraedit.css"))
            # frag.add_css(self.resource_string("static/css/bootstrap.min.css"))
            # frag.add_javascript(self.resource_string("static/js/src/bootstrap.min.js"))
            frag.add_javascript(self.resource_string("static/js/src/popup.js"))
            frag.add_javascript(self.resource_string("static/js/src/jquery.min.js"))
            frag.add_javascript(self.resource_string("static/js/src/paraedit.js"))
            frag.initialize_js('EditParagraphXBlock',json_args=settings)  

            
        elif context['course_id']:
            lessons_list = Lessons.objects.filter(course=context['course_id'])
            course = Course.objects.get(id=context['course_id'])
            context = {
            'lessons_list': lessons_list,
            'course':course,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }

            frag = Fragment(loader.render_template("static/html/lessons.html", context))
            frag.add_css(self.resource_string("static/css/paragraphxblock.css"))
            settings = {
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }
            frag.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
            frag.initialize_js('ParagraphXBlock',json_args=settings)

        else : 
            settings = {
            'scenario_id': context['scenario_id'],
            'view':  context['view'] 
            }
            course_list = Course.objects.all()
            context = {
            'course_list': course_list,
            'scenario_id': context['scenario_id']
            }

            frag = Fragment(loader.render_template("static/html/paragraphxblock.html", context))
            frag.add_css(self.resource_string("static/css/paragraphxblock.css"))
            frag.add_css(self.resource_string("static/css/bootstrap.min.css"))
            frag.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
            frag.add_javascript(self.resource_string("static/js/src/bootstrap.min.js"))
            frag.add_javascript(self.resource_string("static/js/src/jquery.min.js"))
            frag.initialize_js('ParagraphXBlock',json_args=settings)
        
        
        return frag 


    @XBlock.json_handler
    def post_paragraph_studio(self, data, suffix=''):

        # import pdb; pdb.set_trace()
        print "lesonid==>",data["lesson_id"]
        lesson=Lessons.objects.get(id=data["lesson_id"]);
        lesson.paragraph=data["paragraph"]
        lesson.save();

        para_dict ={
            'new_para':lesson.paragraph
        }
        updated_para = json.dumps(para_dict)

        return json.loads(updated_para)

    @XBlock.json_handler
    def get_keyword(self, data, suffix=''):
        
        lesson=Lessons.objects.get(pk=data["lesson_id"])
        try:
            key=KeyDefinition.objects.get(lesson=lesson,keyword=data["keyword"].lower())
        except KeyDefinition.DoesNotExist:
            key = None
        if key:             
             return {"key_defination":key.defination}
        else:
            return {"key_defination":"none"}   

    @XBlock.json_handler
    def post_keyword(self, data, suffix=''):
        # import pdb; pdb.set_trace()
        lesson=Lessons.objects.get(pk=data["lesson_id"])  
        try:
            key=KeyDefinition.objects.get(lesson=lesson,keyword=data["keyword"].lower())
            key.defination=data["defination"]
            
        except KeyDefinition.DoesNotExist:            
            key =KeyDefinition(lesson=lesson,keyword=data["keyword"].lower(),defination=data["defination"])
        key.save()
        return {"keyword":data["keyword"]}


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ParagraphXBlock",
             """<paragraphxblock/>
             """),
            ("Multiple ParagraphXBlock",
             """<vertical_demo>
                <paragraphxblock/>
                <paragraphxblock/>
                <paragraphxblock/>
                </vertical_demo>
             """),
        ]
