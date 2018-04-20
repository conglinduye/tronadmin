# !/usr/bin/env python
# *-* coding:utf-8 *-*
# date:2018/04/20

from app import db
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

__author__ = "lmr"


class TREvents(db.Model):
    __tablename__ = 'tr_events'

    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.string(), nullable=False)
    location = db.Column(db.string())
    start_date = db.Clumn(db.Timestamp)
    end_date = db.Clumn(db.Timestamp)
    author = db.Column(db.string(), nullable=False)
    email = db.Column(db.string())
    brief = db.Column(db.Text)
    description = db.Column(db.Text)
    highlights = db.Column(db.Text)
    web_url = db.Column(db.string())
    info = db.Column(db.Text)
    language = db.Column(db.string())
    social_link1 = db.Column(db.string())
    social_link2 = db.Column(db.string())
    sponsors = db.Column(db.string())
    review = db.Column(db.Integer, default=0)
    delete = db.Column(db.Boolean, default=0)
    extra = db.Column(db.string())
    update_time = db.Clumn(TIMESTAMP, server_default=func.now(), nullable=False)
    create_time = db.Clumn(TIMESTAMP, server_default=func.now(), nullable=False)  # #注意这里是server_default
