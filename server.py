import falcon
from handlers import PingHandler, FilterHandler

app = falcon.API()

app.add_route('/ping', PingHandler())
app.add_route('/filter', FilterHandler())

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 8010, app)
    httpd.serve_forever()
