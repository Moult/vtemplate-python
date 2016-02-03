import pystache
import vtemplate.tool
import vtemplate.view
import vtemplate.controller


class Core:

    def __init__(self):
        self.layout = 'layout'
        self.template = None
        self.view = None

    def render(self):
        renderer = pystache.Renderer(
            search_dirs='vtemplate/ui',
            partials=vtemplate.tool.PartialLoader(self.template)
        )
        return renderer.render_name(self.layout, self.view)
