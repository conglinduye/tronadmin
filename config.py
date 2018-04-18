# !/usr/bin/env python
# *-* coding:utf-8 *-*

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = ''
