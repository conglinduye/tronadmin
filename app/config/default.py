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
SQLDB_DSN_MASTER1 = {
    'w': 'dbname= user= password=0909 host=172.16.100.4',
    'r': 'dbname= user= password=0909 host=172.16.100.4',
}
SQLDB_DSN_MASTER = {
    "database": "",
    "user": "",
    "password": "0909",
    "host": "172.16.100.4",
    "port": "5432"
}
# 系统数据库配置 end

# Log 配置 begin
LOGGING_LEVEL = 'debug'
LOGGING_LOOP_CHECK_TIME = 60
CURRENT_LOGGING_LEVEL = None
# Log 配置 end