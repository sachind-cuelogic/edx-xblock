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

    def student_view(self, context=None):
        """
        The primary view of the ParagraphXBlock, shown to students
        when viewing courses.
        """
        if context['course_id']:
            lessons_list = Lessons.objects.filter(course=context['course_id'])
            course       = Course.objects.get(id=context['course_id'])
            context      = {
            'lessons_list': lessons_list,
            'course':course,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }
            fragment     = Fragment(loader.render_template("static/html/lessons.html", context))

        elif context['lesson_id']:
            paragraph = Lessons.objects.get(id=context['lesson_id'])
            context   = {
            'paragraph': paragraph,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'view':  context['view'] 
            }
            fragment  = Fragment(loader.render_template("static/html/paragraph.html", context))            
            fragment.initialize_js('AddParagraphXBlock')

        else: 
            course_list = Course.objects.all()
            context     = {
            'course_list': course_list,
            'scenario_id': context['scenario_id']
            }
            fragment    = Fragment(loader.render_template("static/html/paragraphxblock.html", context))

        fragment.add_css(self.resource_string("static/css/paragraphxblock.css"))
        fragment.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
        fragment.add_javascript(self.resource_string("static/js/src/add_paragraph.js"))
        
        fragment.add_css(self.resource_string("static/css/tooltipster.bundle.min.css"))
        fragment.add_css(self.resource_string("static/css/tooltipster-sideTip-punk.min.css"))
        fragment.add_javascript(self.resource_string("static/js/src/jquery.min.js"))
        fragment.add_javascript(self.resource_string("static/js/src/tooltipster.bundle.min.js"))
        fragment.initialize_js('ParagraphXBlock')
        return fragment


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
            fragment = Fragment(loader.render_template("static/html/paraedit.html", context))
            fragment.add_css(self.resource_string("static/css/paraedit.css"))
            # fragment.add_javascript(self.resource_string("static/js/src/tooltipster-SVG.js"))

            # fragment.add_css(self.resource_string("static/css/tooltipster-sideTip-noir.min.css"))
            fragment.add_css(self.resource_string("static/css/tooltipster.bundle.min.css"))
            fragment.add_css(self.resource_string("static/css/tooltipster-sideTip-punk.min.css"))
            fragment.add_javascript(self.resource_string("static/js/src/jquery.min.js"))
            fragment.add_javascript(self.resource_string("static/js/src/tooltipster.bundle.min.js"))
            fragment.add_javascript(self.resource_string("static/js/src/paraedit.js"))
            fragment.initialize_js('EditParagraphXBlock')  

            
        elif context['course_id']:
            lessons_list = Lessons.objects.filter(course=context['course_id'])
            course       = Course.objects.get(id=context['course_id'])
            context      = {
            'lessons_list': lessons_list,
            'course':course,
            'scenario_id': context['scenario_id'],
            'course_id': context['course_id'],
            'lesson_id': context['lesson_id'],
            'view':  context['view'] 
            }
            fragment = Fragment(loader.render_template("static/html/lessons.html", context))
            fragment.add_css(self.resource_string("static/css/paragraphxblock.css"))
            fragment.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
            fragment.initialize_js('ParagraphXBlock')

        elif context['para_id']:
            paragraph = Lessons.objects.get(id=context['para_id'])
            context = {
            'paragraph': paragraph,
            'scenario_id': context['scenario_id'],
            'view':  context['view'] 
            }
            fragment = Fragment(loader.render_template("static/html/paragraph_edit.html", context))
            fragment.add_css(self.resource_string("static/css/paraedit.css"))
            # fragment.add_javascript(self.resource_string("static/js/src/tooltipster-SVG.js"))

            fragment.add_css(self.resource_string("static/css/tooltipster-sideTip-punk.min.css"))
            fragment.add_css(self.resource_string("static/css/tooltipster.bundle.min.css"))
            # fragment.add_css(self.resource_string("static/css/tooltipster-sideTip-noir.min.css"))
            fragment.add_javascript(self.resource_string("static/js/src/jquery.min.js"))
            fragment.add_javascript(self.resource_string("static/js/src/tooltipster.bundle.min.js"))
            fragment.add_javascript(self.resource_string("static/js/src/paraedit.js"))
            fragment.initialize_js('EditParagraphXBlock')              

        else : 
            course_list = Course.objects.all()
            context = {
            'course_list': course_list,
            'scenario_id': context['scenario_id']
            }
            fragment = Fragment(loader.render_template("static/html/paragraphxblock.html", context))
            fragment.add_css(self.resource_string("static/css/paragraphxblock.css"))
            # fragment.add_css(self.resource_string("static/css/bootstrap.min.css"))
            fragment.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
            # fragment.add_javascript(self.resource_string("static/js/src/bootstrap.min.js"))
            # fragment.add_javascript(self.resource_string("static/js/src/jquery.min.js"))
            fragment.initialize_js('ParagraphXBlock')
        
        return fragment 


    @XBlock.json_handler
    def post_paragraph(self, data, suffix=''):

        lesson           = Lessons.objects.get(id=data["lesson_id"]);
        lesson.paragraph = data["paragraph"]
        para             = (lesson.paragraph).replace(" ","")
        if(para):
            lesson.save();
            para_dict    = {'new_para':lesson.paragraph}
            updated_para = json.dumps(para_dict)
            return json.loads(updated_para)
        
        else:
            return {"result": "fail"}


    @XBlock.json_handler
    def get_keyword(self, data, suffix=''):

        lesson = Lessons.objects.get(pk=data["lesson_id"])
        
        try:
            key = KeyDefinition.objects.get(lesson=lesson, keyword=data["keyword"].lower())
        except KeyDefinition.DoesNotExist:
            key = None

        if key:             
            return {"key_defination":key.defination, "keyword":key.keyword}
        else:
            return {"key_defination":"none"}   


    @XBlock.json_handler
    def post_keyword(self, data, suffix=''):
        # import pdb; pdb.set_trace()
        lesson  = Lessons.objects.get(pk=data["lesson_id"])  
        try:
            key = KeyDefinition.objects.get(lesson=lesson, keyword=data["keyword"].lower())
            key.defination = data["defination"]
            
        except KeyDefinition.DoesNotExist:            
            key =KeyDefinition(lesson=lesson, 
                                keyword=data["keyword"].lower(), 
                                defination=data["defination"])
        key.save()
        return {"keyword":data["keyword"], "defination":key.defination}


    @XBlock.json_handler
    def update_highlighted_keys(self, data, suffix=''):

        paragraph         = Lessons.objects.get(id=data["lesson_id"])
        keywords          = KeyDefinition.objects.filter(lesson=data["lesson_id"])
        keys              = []
        for i in keywords:
            key           = {}
            key["keyword"]= i.keyword
            key["defination"] = i.defination
            keys.append(key)
        return {"paragraph":paragraph.paragraph,"keys":keys}


    @XBlock.json_handler
    def post_paragraph_student(self, data, suffix=''): 
           
        para     = Lessons.objects.get(course=data["course_id"],id=data["lesson_id"])
        keywords = KeyDefinition.objects.filter(lesson=data["lesson_id"])
        keys     = []

        for i in keywords:
            key               = {}
            key["keyword"]    = i.keyword
            key["definition"] = i.defination
            keys.append(key)

        paragraphs              = {}
        paragraphs["paragraph"] = para.paragraph
        return {"paragraph":paragraphs,"keys":keys} 



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
