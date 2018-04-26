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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String())
    ip = db.Column(db.String())
    permission = db.Column(db.Integer, default=0, nullable=False)
    createby = db.Column(db.String())
    delete = db.Column(db.Integer, default=0, nullable=False)
    signin_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)
    # extra = db.Column(db.String())
    create_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)

