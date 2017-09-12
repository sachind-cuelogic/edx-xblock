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
        course_list = Course.objects.all()

        context = {
        'course_list': course_list
        }

        settings = {
            'view':  context['view'] 
            }    
        print "view==>",settings
        # print "course id==>",context['course_id']
        # html = self.resource_string("static/html/paragraphxblock.html")
        # frag = Fragment(html.format(self=self))
        # frag.add_css(self.resource_string("static/css/paragraphxblock.css"))
        # frag.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
        # frag.initialize_js('ParagraphXBlock')
        # return frag

        fragment = Fragment(loader.render_template("static/html/paragraphxblock.html", context))
        fragment.add_css(self.resource_string("static/css/paragraphxblock.css"))
        fragment.add_javascript(
        self.resource_string("static/js/src/paragraphxblock.js"))
        fragment.initialize_js("ParagraphXBlock")
        return fragment


    def lessons_view(self, context=None):
        """
        The primary view of the ParagraphXBlock, shown to students
        when viewing courses.
        """
        # course_list = Course.objects.all()

        context = {
        'course_list': course_list
        }
        # print "course id==>",context['course_id']
        # html = self.resource_string("static/html/paragraphxblock.html")
        # frag = Fragment(html.format(self=self))
        # frag.add_css(self.resource_string("static/css/paragraphxblock.css"))
        # frag.add_javascript(self.resource_string("static/js/src/paragraphxblock.js"))
        # frag.initialize_js('ParagraphXBlock')
        # return frag
        
        fragment = Fragment(loader.render_template("static/html/paragraphxblock.html", context))
        fragment.add_css(self.resource_string("static/css/paragraphxblock.css"))
        fragment.add_javascript(
        self.resource_string("static/js/src/paragraphxblock.js"))
        fragment.initialize_js("ParagraphXBlock")
        return fragment


    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

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
