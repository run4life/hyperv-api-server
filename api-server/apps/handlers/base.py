#
# -*- coding: utf-8 -*-
#
import json
import base64
import logging
import tornado.web
import tornado.escape

class BaseHandler(tornado.web.RequestHandler):
    """
        Base基类
    """
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        #self.params = ''
        self.dict_headers = {'Content-Type':'application/json', 'Accept':'application/json'}