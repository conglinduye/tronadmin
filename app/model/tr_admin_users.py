# !/usr/bin/env python
# *-* coding:utf-8 *-*
# date:2018/04/23
import random
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from app import db

__author__ = "lmr"


class TRAdminUsers(db.Model):
    __tablename__ = 'tr_admin_users'
    id = db.Column(db.Integer, primary_key=True)         # id
    name = db.Column(db.String(), nullable=False)        # 账户名称
    email = db.Column(db.String())                       # 登陆邮箱
    password = db.Column(db.String())                    # 密码
    ip = db.Column(db.String())                          # 登陆ip
    permission = db.Column(db.Integer, default=0, nullable=False)   # 权限
    createby = db.Column(db.String())                    # 创建人
    delete = db.Column(db.Integer, default=0, nullable=False)       # 删除
    signin_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)   # 最近一次登陆时间
    remark = db.Column(db.String())                      # 备注信息
    extra = db.Column(db.String())                       # extra
    create_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)   # 创建时间

