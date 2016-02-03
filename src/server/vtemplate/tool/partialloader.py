class PartialLoader:

    def __init__(self, content):
        self.content = content

    def get(self, name):
        try:
            if (name == 'content'):
                name = self.content
            partial = open('vtemplate/ui/'+name+'.mustache')
            return partial.read()
        except FileNotFoundError:
            return None
