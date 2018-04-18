# !/usr/bin/env python
# *-* coding:utf-8 *-*
from flask_restful import Resource


class Main(Resource):

    def get(self):
        return "hello world"
