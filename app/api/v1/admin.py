# !/usr/bin/env python
# *-* coding:utf-8 *-*
from flask_restful import Resource


class Main(Resource):

    def index(self):
        return "hello world"
