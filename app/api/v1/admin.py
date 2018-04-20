# !/usr/bin/env python
# *-* coding:utf-8 *-*
import flask

from app.api import api
from flask_restful import Resource


@api.route('/index')
def index():
    # return {"data": ['asdf', 'dsf']}
    d = {'data': ['maocai', '418']}
    return flask.jsonify(d)
    #return "hello world"


class Index1(Resource):
    def get(self):
        return {"data": ['asdf', 'dsf']}
