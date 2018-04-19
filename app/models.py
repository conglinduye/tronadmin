# !/usr/bin/env python
# *-* coding:utf-8 *-*

from app import db


class TRDapp(db.Model):
    __tablename__ = 'tr_dapp'
    id = db.Column(db.Integer, primary_key=True)
    dapp_id = db.Column(db.Integer)
    dapp_name = db.Column(db.String(), unique=True)
    author = db.Column(db.String())
    dapp_email = db.Column(db.String())
    brief = db.Column(db.Text)
    description = db.Column(db.Text)
    wallet_address = db.Column(db.String())
    license = db.Column(db.String())
    status = db.Column(db.Integer)
    social_link1 = db.Column(db.String())
    social_link2 = db.Column(db.String())
    pv = db.Column(db.Integer)
    web_url = db.Column(db.String())
    dapp_url = db.Column(db.String())
    logo_url = db.Column(db.String())
    tags = db.Column(db.String())
    review = db.Column(db.Integer)
    delete = db.Column(db.Boolean)
    extra = db.Column(db.String())
    update_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime)
