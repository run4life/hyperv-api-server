import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload
import tornado.web

from tornado.options import define, options
from urls import url

LOG = logging.getLogger(__name__)


def getApplication():
    app_settings = dict(
            login_url='/login'
    )
    application = tornado.web.Application(
            handlers=url,
            **app_settings
    )
    return application

def main():
    application = getApplication()
    app = tornado.httpserver.HTTPServer(application)
    app.bind('8080', '127.0.0.1')
    app.start(1)
    print "server is running at http://127.0.0.1:8080"
    print "Quit the server with Control-C"
    LOG.info("Tornado server is running")
    loop = tornado.ioloop.IOLoop.instance()
    #tornado.autoreload.start(loop)
    loop.start()


if __name__ == "__main__":
    main()

