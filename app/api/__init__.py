# !/usr/bin/env python
# *-* coding:utf-8 *-*

from flask import Blueprint
from flask_restful import Api
api = Blueprint('api', __name__, url_prefix='/api/v1')

API = Api(api)
from app.api.v1.admin import Index1
from app.api.v1.dapp_submit_1 import DappSubmit1
from app.api.v1.accounts.signup import SignUp

API.add_resource(Index1, '/aaaa')
API.add_resource(DappSubmit1, '/dapp_submit1')
API.add_resource(SignUp, '/accounts/signup')

from app.api.v1 import admin
from app.api.v1 import dapp_query
from app.api.v1 import dapp_submit
from app.api.v1.accounts import login
