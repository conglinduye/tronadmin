# *-* coding:utf-8 *-*
# date:2018/04/24

import flask
import logging
from flask import request
from app.api import api
from app import db
from app.config.base import GreenResource
from app.func.password import Password
from app.model import types
from app.model.tr_admin_users import TRAdminUsers

__author__ = "lmr"


@api.route('/accounts/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        create_name = request.form.get("create_name")
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        promission = request.form.get("promission")

        if create_name != "admin":
            return flask.jsonify({
                'code': types.RESPONSE_CODE.PERMISSION_ERROR,
                'msg': "您没有此权限"
            })

        result, password_new = Password.get_password(password)  # 返回加密后的密码 2017／8／10
        if not result:
            return flask.jsonify({
                'code': types.RESPONSE_CODE.PARAMETER_ERROR,
                'msg': '参数错误',
            })

        user = TRAdminUsers.query.filter_by(email=email).first()
        if user:
            return flask.jsonify({
                'code': types.RESPONSE_CODE.DATA_ALREADY_EXIST,
                'msg': "邮箱已存在"
            })
        newobj = TRAdminUsers(name=name, email=email, password=password_new,
                              permission=int(promission), createby=create_name)
        db.session.add(newobj)
        db.session.commit()

        logging.info("{} added manager:{}".format(create_name, name))

        return flask.jsonify({
            'code': types.RESPONSE_CODE.SUCCESS,
            'msg': "添加成员成功"
        })
