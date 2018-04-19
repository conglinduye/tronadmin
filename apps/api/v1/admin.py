# !/usr/bin/env python
# *-* coding:utf-8 *-*
from flask_restful import Resource
import logging


class Main(Resource):

    def get(self):
        logging.info("log rizhi")
        return "hello world"
