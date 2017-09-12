"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('testxblock', 'static/html'))

class TestXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    # count = Integer(
    #     default=0, scope=Scope.user_state,
    #     help="A simple counter, to show something happening",
    # )
    eassy_title = String(display_name="Question Title",
        default="demo",
        scope=Scope.settings,
        help="eassy question title")
    eassy_text = String(
        default="demo", scope=Scope.content,
        help="Contents of eassy",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TestXBlock, shown to students
        when viewing courses.
        """
        context = {
            'eassy_title': self.eassy_title,
            'eassy_text': self.eassy_text,
        }        
        frag = Fragment()
        template = env.get_template('testxblock.html')
        frag.add_content(template.render(**context))
        frag.add_css(self.resource_string("static/css/testxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/testxblock.js"))
        frag.initialize_js('TestXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The primary view of the TestXBlock, shown to students
        when viewing courses.
        """
        context = {
            'eassy_title': self.eassy_title
            # 'eassy_text': self.eassy_text,
        }        
        frag = Fragment()
        template = env.get_template('testxblock_edit.html')
        frag.add_content(template.render(**context))
        frag.add_css(self.resource_string("static/css/testxblock_edit.css"))
        frag.add_javascript(self.resource_string("static/js/src/testxblock_edit.js"))
        frag.initialize_js('TestXBlockEdit')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    # @XBlock.json_handler
    # def increment_count(self, data, suffix=''):
    #     """
    #     An example handler, which increments the data.
    #     """
    #     # Just to show data coming in...
    #     assert data['hello'] == 'world'

    #     self.count += 1
    #     return {"count": self.count}

    @XBlock.json_handler
    def student_submit(self, data, suffix=''):
        """Called when submitting the form in Studio."""
       
        self.eassy_title=data['eassy_title']
        self.eassy_text = data['eassy_text']
        return {'result':'success'}

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """Called when submitting the form in Studio."""
       
        self.eassy_title=data['question']
        return {'result':'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TestXBlock",
             """<testxblock/>
             """),
            ("Multiple TestXBlock",
             """<vertical_demo>
                <testxblock/>
                <testxblock/>
                <testxblock/>
                </vertical_demo>
             """),
        ]
