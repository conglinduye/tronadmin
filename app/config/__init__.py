#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lmr

from default import *

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True

    # psql初始化 begin
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 若设为True，SQLAlchemy将追踪对象的修改和发送信号；默认是None；
    # psql初始化 end

    SECRET_KEY = ''
