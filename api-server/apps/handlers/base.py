#
# -*- coding: utf-8 -*-
#
import json
import base64
import logging
import requests
import tornado.web
import tornado.escape

class BaseHandler(tornado.web.RequestHandler):
    """
        Base基类
    """
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def head(self, *args, **kwargs):
        self.feedback()

    def get(self, *args, **kwargs):
        # self.write_error(404)  # 自定义错误页面
        self.feedback()

    def post(self, *args, **kwargs):
        self.feedback()

    def delete(self, *args, **kwargs):
        self.feedback()

    def patch(self, *args, **kwargs):
        self.feedback()

    def put(self, *args, **kwargs):
        self.feedback()

    def options(self, *args, **kwargs):
        self.feedback()