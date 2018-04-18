# !/usr/bin/env python
# *-* coding:utf-8 *-*
from flask_restful import Resource
import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

class Main(Resource):

    def get(self):
        logging.info("log rizhi")
        return "hello world"
