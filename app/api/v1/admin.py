# !/usr/bin/env python
# *-* coding:utf-8 *-*

from app.api import api


@api.route('/')
def index():
    return "hello world"
