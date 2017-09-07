"""TO-DO: Write a description of what this XBlock is."""

import os
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Dict
from xblock.fragment import Fragment
from mako.template import Template
from .utils import loader, AttrDict

class ReferenceXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.

    ref_name = String(help="Reference Name", default=None, scope=Scope.content)
    ref_link = String(help="Reference link", default=None, scope=Scope.content)
    ref_description = String(help="Reference Description", default=None, scope=Scope.content)
    ref_type = String(help="Reference Name", default=None, scope=Scope.content)
    ref_status = String(help="Reference Name", default=None, scope=Scope.content)


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # def render_template(self, template_name, context={}):
    #   """Another handy helper for rendering Mako templates from our kit."""

    #   template = Template(self.resource_string(os.path.join("static/html/",
    #                                                         template_name)))
    #   return template.render_unicode(**context)

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ReferenceXBlock, shown to students
        when viewing courses.
        """

        context = {
        'ref_name': self.ref_name,
        'ref_link': self.ref_link,
        'ref_type': self.ref_type,
        'ref_description': self.ref_description,
        'ref_status': self.ref_status
        }
        fragment = Fragment()
        fragment.add_content(loader.render_template('static/html/referenceview.html', context))
        return fragment   


        # fragment = Fragment(loader.render_template("static/html/referencexblock.html", context))
        # fragment.add_css(self.resource_string("static/css/referencexblock.css"))
        # fragment.add_javascript(
        # self.resource_string("static/js/src/referencexblock.js"))
        # fragment.initialize_js("ReferenceXBlock")
        # return fragment


    def studio_view(self, context=None):
        """
        This is the view that content authors will see when they click on the
        "Edit" button in Studio. It is a form that lets them type in two fields:
        module ID and player type. This is the same for both lessons and
        reviews.
        """

        context = {
        'ref_name': self.ref_name,
        'ref_link': self.ref_link,
        'ref_type': self.ref_type,
        'ref_description': self.ref_description,
        'ref_status': self.ref_status
        }
        # fragment = Fragment()
        # fragment.add_content(loader.render_template('referencexblock.html', context))
        # return fragment   

        fragment = Fragment(loader.render_template("static/html/referencexblock.html", context))
        fragment.add_css(self.resource_string("static/css/referencexblock.css"))
        fragment.add_javascript(
        self.resource_string("static/js/src/referencexblock.js"))
        fragment.initialize_js("ReferenceXBlock")
        return fragment

    @XBlock.json_handler
    def reference_data(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
 
        self.ref_name = data['ref_name']
        self.ref_link = data['ref_link']
        self.ref_type = data['ref_type']
        self.ref_description = data['ref_description']
        self.ref_status = data['ref_status']


        return { "ref_name": self.ref_name,
                "ref_link": self.ref_link,
                "ref_type": self.ref_type,
                "ref_description": self.ref_description,
                "ref_status": self.ref_status
                }
        
        # return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ReferenceXBlock",
             """<referencexblock/>
             """),
            ("Multiple ReferenceXBlock",
             """<vertical_demo>
                <referencexblock/>
                <referencexblock/>
                <referencexblock/>
                </vertical_demo>
             """),
        ]