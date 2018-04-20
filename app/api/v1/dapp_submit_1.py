# *-* coding:utf-8 *-*
# date:2018/04/19

import logging

import flask
from flask_restful import Resource
from flask import request

from app.model import types
from app.models import TRDapp

__author__ = "lmr"


class DappSubmit1(Resource):

    def post(self):
        '''
        dapp_name = request.headers["dapp_name"]
        author = request.headers["author"]
        brief = request.headers["brief"]
        status = request.headers["status"]
        '''

        dapp_name = request.form.get('dapp_name')
        author = request.form.get("author")
        brief = request.form.get("brief")
        status = request.form.get('status')  # 必填

        logging.info("dapp_name:{}".format(dapp_name))
        if not (dapp_name and author and brief and status):
            return flask.jsonify({
                'code': types.RESPONSE_CODE.PARAMETER_ERROR,
                'msg': '参数错误1'
            })

        dapp = TRDapp.query_filter_one(dapp_name=dapp_name)
        if dapp:
            return flask.jsonify({
                'code': types.RESPONSE_CODE.DATA_ALREADY_EXIST,
                'msg': 'Dapp name 已存在，换一个吧'
            })
        dapp_id = TRDapp.generate_id()
        TRDapp.save(dapp_id=dapp_id, dapp_name=dapp_name, author=author, brief=brief)
        logging.info("dapp submit: {} dapp submitted by ()".format(dapp_name, author))
        return flask.jsonify({
            'code': types.RESPONSE_CODE.SUCCESS,
            'msg': '提交成功'
        })