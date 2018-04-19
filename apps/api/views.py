# !/usr/bin/env python
# *-* coding:utf-8 *-*

from flask import Blueprint
from flask_restful import Api

from apps.api.v1.admin import Main
from apps.api.v1.dapp_query import DappQuery

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(Main, '/index')
api.add_resource(DappQuery, '/query')
