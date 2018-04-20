# !/usr/bin/env python
# *-* coding:utf-8 *-*
import datetime
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app import db


class TRDapp(db.Model):
    __tablename__ = 'tr_dapp'
    id = db.Column(db.Integer, primary_key=True)
    dapp_id = db.Column(db.Integer, nullable=False)
    dapp_name = db.Column(db.String(), unique=True, nullable=False)
    author = db.Column(db.String(), nullable=False)
    dapp_email = db.Column(db.String())
    brief = db.Column(db.Text)
    description = db.Column(db.Text)
    wallet_address = db.Column(db.String())
    license = db.Column(db.String())
    status = db.Column(db.Integer, nullable=False)
    social_link1 = db.Column(db.String())
    social_link2 = db.Column(db.String())
    pv = db.Column(db.Integer, default=0, nullable=False)
    web_url = db.Column(db.String())
    dapp_url = db.Column(db.String())
    logo_url = db.Column(db.String())
    tags = db.Column(db.String())
    review = db.Column(db.Integer, default=0)
    delete = db.Column(db.Boolean, default=0)
    extra = db.Column(db.String())
    update_time = db.Column(TIMESTAMP, default=datetime.datetime, nullable=False)
    create_time = db.Column(TIMESTAMP, default=datetime.datetime, nullable=False)  # 这种方法其实这种方法根本就没有在数据库里面设置默认值，
# 只是使用了SQLAlchemy Model类提交数据时添加上去的值，并不适合需要取数据库所有服务器时间的场合。