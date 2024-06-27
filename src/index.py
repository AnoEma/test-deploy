import flask
from gevent.pywsgi import WSGIServer


app = flask.Flask(__name__)


@app.route('/vamos')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
  http_server = WSGIServer(('191.252.201.52',8080), app)
  http_server.serve_forever()
