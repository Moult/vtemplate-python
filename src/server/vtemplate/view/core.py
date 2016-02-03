import werkzeug.urls

class Core:

    def baseurl(self):
        return werkzeug.urls.Href('/')
