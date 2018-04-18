#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lmr

from default import *

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = ''
