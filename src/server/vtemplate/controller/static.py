import vtemplate.view
from vtemplate.controller.core import Core


class Static(Core):

    def homepage(self):
        self.template = 'static/homepage'
        self.view = vtemplate.view.Homepage()
