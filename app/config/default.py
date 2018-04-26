#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lmr

PRODUCTION = True
ENV_TEST = False
SERVER_NAME = ''

OFFICIAL_WEB_URL = 'https://debug.tronlab.com'
SESSION_TIMEOUT = 900

APP_VERSION_DEFAULT = 100
API_SLOW_LOG_TIME = 1.0  # SECONDS
PROJECT_BEGIN_TIME = '2018-04-18 00:00:00'

# 系统数据库配置 begin
# postgresql 数据库主库配置
SQLALCHEMY_DATABASE = 'postgresql://tron:tron0909@172.16.100.4:5432/tron'
# 系统数据库配置 end

# 七牛配置
ACCESS_KEY = 'J_O99Ra1HgkY4nKD2dMSJbox1Kc1_f80EMhbBxjX'    # 个人中心->密匙管理->AK

SECRET_KEY = 'oTgFRU46xVuHgHpEEiY6w6XRfdarWogQgihbheog'    # 个人中心->密匙管理->SK

BUCKET_NAME = 'app-image'      # 七牛空间名

DOMAIN_PREFIX = "http://p7476x5w6.bkt.clouddn.com/"   # 域名
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'gif', 'txt', 'pdf'}
UPLOAD_FOLDER = '/path/to/the/uploads'   # 储存上传的文件的地方
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 上传文件限制为最大 16 MB

# END

PASSWORD_SALT = 'tron_salt'   # 密码，是否需要修改？
RSA_PRIVATE_KEY = 'data/rsa/private_key.pem'
RSA_PUBLIC_KEY = 'data/rsa/public_key.pem'
RSA_PRIVATE_KEY_2 = 'data/rsa/private_key_2.pem'
RSA_PUBLIC_KEY_2 = 'data/rsa/public_key_2.pem'

FLASKY_POSTS_PER_PAGE = 20   # 分页：每页条数

# KEY BEGIN

TRIPLE_DES_KEY = 'Ts9nUGskSvp17hQBi0jPwtQm'

# END

SQLDB_DSN_MASTER = {
    "database": "tron",
    "user": "tron",
    "password": "tron0909",
    "host": "172.16.100.4",
    "port": "5432"
}
