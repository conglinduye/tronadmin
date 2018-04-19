# *-* coding:utf-8 *-*
# date:2018/04/19

from flask import Blueprint, render_template, redirect, request
from flask_restful import Resource

from app.models import TRDapp

__author__ = "lmr"


class DappQuery(Resource):

    def post(self):
        dapp_id = request.headers['dapp_id']
        users = TRDapp.query.filter_by(dapp_id=int(dapp_id)).all()
        print users
        return users