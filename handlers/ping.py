from json import dumps

class PingHandler(object):

    def on_get(self, request, response):
        response.body = dumps({"message": "hi"})
