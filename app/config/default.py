#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = ''


# 系统数据库配置 begin
# postgresql 数据库主库配置
SQLDB_DSN_MASTER = {
    "database": "",
    "user": "",
    "password": "",
    "host": "",
    "port": ""
}
