#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

__author__ = "lmr"

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True

    # psql初始化 begin
    SQLALCHEMY_DATABASE_URI = 'postgresql://tron:tron0909@172.16.100.4:5432/tron?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 若设为True，SQLAlchemy将追踪对象的修改和发送信号；默认是None；
    # psql初始化 end

    SECRET_KEY = ''


# 系统数据库配置 begin
# postgresql 数据库主库配置
SQLDB_DSN_MASTER1 = {
    'w': 'dbname=tron user=tron password=tron0909 host=172.16.100.4',
    'r': 'dbname=tron user=tron password=tron0909 host=172.16.100.4',
}
SQLDB_DSN_MASTER = {
    "database": "tron",
    "user": "tron",
    "password": "tron0909",
    "host": "172.16.100.4",
    "port": "5432"
}
# 系统数据库配置 end

# Log 配置 begin
LOGGING_LEVEL = 'debug'
LOGGING_LOOP_CHECK_TIME = 60
CURRENT_LOGGING_LEVEL = None
# Log 配置 end

