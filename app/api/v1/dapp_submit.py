# *-* coding:utf-8 *-*
# date:2018/04/19

import logging

import flask
from flask import request

from app.api import api
from app.model import types
from app.model.tr_dapp import TRDapp

__author__ = "lmr"


@api.route('/dapp_submit', methods=['GET', 'POST'])
def dappsubmit():
    if request.method == 'POST':

        dapp_name = request.form.get('dapp_name')
        author = request.form.get("author")
        dapp_email = request.form.get("dapp_email")
        brief = request.form.get("brief")
        description = request.form.get("description")
        wallet_address = request.form.get("wallet_address")
        license = request.form.get("license")

        status = request.form.get('status')  # 必填
        social_link1 = request.form.get('social_link1')  # 必填
        social_link2 = request.form.get('social_link2')  # 选填
        web_url = request.form.get('web_url')  # 选填
        dapp_url = request.form.get('dapp_url')  # 选填
        logo_url = request.form.get('logo_url')

        if not (dapp_name and author and brief and status):
            return flask.jsonify({
                'code': types.RESPONSE_CODE.PARAMETER_ERROR,
                'msg': '参数错误'
            })

        dapp = TRDapp.query_filter_one(dapp_name=dapp_name)
        if dapp:
            return flask.jsonify({
                'code': types.RESPONSE_CODE.DATA_ALREADY_EXIST,
                'msg': 'Dapp name 已存在，换一个吧'
            })
        dapp_id = TRDapp.generate_id()
        TRDapp.save(dapp_id=dapp_id, dapp_name=dapp_name, author=author, dapp_email=dapp_email, brief=brief,
                    description=description, wallet_address=wallet_address, license=license, status=status,
                    social_link1=social_link1, social_link2=social_link2, web_url=web_url, dapp_url=dapp_url,
                    logo_url=logo_url)
        logging.info("dapp submit: {} dapp submitted by ()".format(dapp_name, author))
        return flask.jsonify({
            'code': types.RESPONSE_CODE.SUCCESS,
            'msg': '提交成功'
        })



