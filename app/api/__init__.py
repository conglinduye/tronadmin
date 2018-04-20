# !/usr/bin/env python
# *-* coding:utf-8 *-*

from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api/v1')

from app.api.v1 import admin
from app.api.v1 import dapp_query