# !/usr/bin/env python
# *-* coding:utf-8 *-*
# date:2018/04/23
import random
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from app import db

__author__ = "lmr"


class TRAdminToken(db.Model):
    __tablename__ = 'tr_admin_token'

    id = db.Column(db.Integer, primary_key=True)         # id
    token = db.Column(db.String())  # token
    expires = db.Column(db.Integer)  # token过期时间
    admin_uid = db.Column(db.Integer)    # user id
