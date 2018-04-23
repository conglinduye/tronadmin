#!/usr/bin/env python
# -*- coding: utf-8 -*-


PRODUCTION = True
ENV_TEST = False

OFFICIAL_WEB_URL = 'https://tron.network'
APP_VERSION_DEFAULT = 100
API_SLOW_LOG_TIME = 1.0  # SECONDS
PROJECT_BEGIN_TIME = '2018-04-18 00:00:00'

# 系统数据库配置 begin
# postgresql 数据库主库配置
SQLALCHEMY_DATABASE = 'postgresql://tron:tron0909@172.16.100.4:5432/tron'
SQLDB_DSN_MASTER = {
    "database": "tron",
    "user": "tron",
    "password": "tron0909",
    "host": "172.16.100.4",
    "port": "5432"
}
# 系统数据库配置 end

# 七牛配置
ACCESS_KEY = 'J_O99Ra1HgkY4nKD2dMSJbox1Kc1_f80EMhbBxjX'    # 个人中心->密匙管理->AK

SECRET_KEY = 'oTgFRU46xVuHgHpEEiY6w6XRfdarWogQgihbheog'    # 个人中心->密匙管理->SK

BUCKET_NAME = 'app-image'      # 七牛空间名

DOMAIN_PREFIX = "http://p7476x5w6.bkt.clouddn.com/"   # 域名
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'gif'}
# END

FLASKY_POSTS_PER_PAGE = 20   # 分页：每页条数