import falcon
from falcon_handlers.ping import PingHandler
from falcon_handlers.image import ImageHandler
from falcon_handlers.jsonbody import JsonBodyHandler

app = falcon.API()

app.add_route('/ping', PingHandler())
app.add_route('/image', ImageHandler(storage_path="/Users/mickeyshaughnessy/Downloads/"))
app.add_route('/jsonbody', JsonBodyHandler())

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 8010, app)
    httpd.serve_forever()
