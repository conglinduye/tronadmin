# !/usr/bin/env python
# *-* coding:utf-8 *-*
# date:2018/04/20
from app import db
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

__author__ = "lmr"


class TREventType(db.Model):
    __tablename__ = 'tr_event_type'

    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer, nullable=False)
    conference = db.Column(db.Integer, default=0, nullable=False)
    hackathon = db.Column(db.Integer, default=0, nullable=False)
    token = db.Column(db.Integer, default=0, nullable=False)
    meetup = db.Column(db.Integer, default=0, nullable=False)
    release = db.Column(db.Integer, default=0, nullable=False)
    workshop = db.Column(db.Integer, default=0, nullable=False)
    ico = db.Column(db.Integer, default=0, nullable=False)
    submit = db.Column(db.Integer, default=0, nullable=False)
    delete = db.Column(db.Integer, default=0, nullable=False)
    update_time = db.Clumn(TIMESTAMP, server_default=func.now(), nullable=False)
    create_time = db.Clumn(TIMESTAMP, server_default=func.now(), nullable=False)  # #注意这里是server_default