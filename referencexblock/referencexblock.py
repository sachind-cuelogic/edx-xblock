"""TO-DO: Write a description of what this XBlock is."""

import os
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Dict
from xblock.fragment import Fragment
from mako.template import Template
from .utils import loader, AttrDict
from xblockutils.studio_editable import StudioEditableXBlockMixin

class ReferenceXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    display_name = String(
      help="The display name of this component.",
      scope=Scope.settings,
      default="",
      display_name="The display name of this component")
    ref_name = String(display_name = "Reference Name", default=None, scope=Scope.content)
    ref_link = String(display_name = "Reference Link", help="Reference link", default=None, scope=Scope.content)
    ref_description = String(display_name = "Reference Description", help="Reference Description", default=None, scope=Scope.content)
    ref_type = String(display_name = "Reference Type", default=None, scope=Scope.content)
    ref_status = String(display_name = "Reference Status", help="Reference Name", default=None, scope=Scope.content)


    def get_display_name(self, ref_name):
      """
      This method generates a string that is usable as the display name
      for the component, using the module title (such as "Lines and Rays").
      By default, we just return the module title, but subclasses might
      want to do something more specific.
      """
      return ref_name


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


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
        'ref_status': self.ref_status,
        'title':self.ref_name
        }
        fragment = Fragment()
        fragment.add_content(loader.render_template('static/html/referenceview.html', context))
        fragment.add_css(self.resource_string("static/css/referencexblock.css"))
        return fragment   


        # fragment = Fragment(loader.render_template("static/html/referencexblock.html", context))
        # fragment.add_css(self.resource_string("static/css/referencexblock.css"))
        # fragment.add_javascript(
        # self.resource_string("static/js/src/referencexblock.js"))
        # fragment.initialize_js("ReferenceXBlock")
        # return fragment


    """
    In studio view staff can able to edit reference form
    """
    def studio_view(self, context=None):
        """
        This is the view that reference content will see when they click on the
        "Edit" button in Studio.
        """

        context = {
        'ref_name': self.ref_name,
        'ref_link': self.ref_link,
        'ref_type': self.ref_type,
        'ref_description': self.ref_description,
        'ref_status': self.ref_status,
        'title':self.ref_name
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
        An example handler, gets data from template.
        """
        # Just to show data coming in...
 
        self.ref_name = data['ref_name']
        self.ref_link = data['ref_link']
        self.ref_type = data['ref_type']
        self.ref_description = data['ref_description']
        self.ref_status = data['ref_status']
        self.display_name = self.get_display_name(self.ref_name)

        return {"result": "success"}
        
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
