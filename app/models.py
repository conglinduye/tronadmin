# !/usr/bin/env python
# *-* coding:utf-8 *-*
# date:2018/04/20
import datetime
import random
import logging
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from app import db

__author__ = "lmr"


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
    delete = db.Column(db.Integer, default=0)
    extra = db.Column(db.String())
    update_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)
    create_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)  # 这种方法其实这种方法根本就没有在数据库里面设置默认值，
    # 只是使用了SQLAlchemy Model类提交数据时添加上去的值，并不适合需要取数据库所有服务器时间的场合。

    class STATUS(object):
        LIVE = 0        # 成熟稳定版本
        BETA = 1        # beta版本
        PROTOTYPE = 2   # 原型阶段
        PROGRESS = 3    # 进展中
        CONCEPT = 4     # 概念模型阶段
        ABANDONED = 5
        STEALTH = 6     # 暂时不展示

        ALL = {LIVE: "live", BETA: "beta", PROTOTYPE: "prototype", PROGRESS: "progress",
               CONCEPT: "concept", ABANDONED: "abandoned"}

        VALID = {LIVE, BETA, PROTOTYPE, PROGRESS, CONCEPT, ABANDONED}

        @classmethod
        def get_name(cls, dapp_id):
            if dapp_id not in cls.ALL:
                return None
            return cls.ALL[dapp_id]

    class TYPE(object):
        HOT = 'hot'
        NEW = 'new'

    class REVIEWTYPE(object):
        UNAUDITED = 0
        PAST = 1
        FAILURE = 2

        VALID = {UNAUDITED, PAST, FAILURE}

    class SORT(object):
        DAPP = 1
        EVENT = 2

    @classmethod
    def generate_id(cls):
        while True:
            dapp_id = random.randint(10000000, 99999999)
            # if NumberFilter.filter(uid):
            #    continue
            result = cls.query.filter_by(dapp_id=dapp_id).first()
            if not result:
                return dapp_id

    @classmethod
    def querys(cls):
        return cls.query.all()

    @classmethod
    def query_filter(cls, **kwargs):
        filters = {}
        if kwargs:
            for field, value in kwargs.iteritems():
                filters[field] = value

        return cls.query.filter_by(**filters).all()

    @classmethod
    def query_filter_one(cls, **kwargs):
        filters = {}
        if kwargs:
            for field, value in kwargs.iteritems():
                filters[field] = value
        return cls.query.filter_by(**filters).first()

    @classmethod
    def save(cls, **kwargs):
        filters = {}
        if kwargs:
            for field, value in kwargs.iteritems():
                filters[field] = value
        newobj = cls(**filters)
        db.session.add(newobj)
        db.session.commit()