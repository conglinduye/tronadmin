#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lmr

from default import *

ENV_TEST = True

OFFICIAL_WEB_URL = 'https://debug.tronlab.com'
SESSION_TIMEOUT = 900


# 系统数据库配置 begin
# postgresql 数据库主库配置
SQLALCHEMY_DATABASE = ''
# 系统数据库配置 end

# 七牛配置
ACCESS_KEY = 'J_O99Ra1HgkY4nKD2dMSJbox1Kc1_f80EMhbBxjX'    # 个人中心->密匙管理->AK

SECRET_KEY = 'oTgFRU46xVuHgHpEEiY6w6XRfdarWogQgihbheog'    # 个人中心->密匙管理->SK

BUCKET_NAME = 'app-image'      # 七牛空间名

DOMAIN_PREFIX = "http://p7476x5w6.bkt.clouddn.com/"   # 域名
# END
COOKIE_NAME = 'dapp_accounts_token' #token名字
TLL = 30*60 #token过期时间

