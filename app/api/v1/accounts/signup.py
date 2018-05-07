# *-* coding:utf-8 *-*
# date:2018/04/24
import datetime
import flask
from flask import request

from app import db
from app.config.base import GreenResource, deco
from app.func.password import Password
from app.model import types
from app.model.tr_admin_users import TRAdminUsers
from app.util.iputil import get_http_real_ip
from app.util.token_util import generate, COOKIE_NAME

__author__ = "lmr"


class SignUp(GreenResource):

    def post(self):
        email = request.form.get("email")
        password = request.form.get("password")
        ip = get_http_real_ip(request)

        if not (email and password):
            return flask.jsonify({
                'code': types.RESPONSE_CODE.PARAMETER_ERROR,
                'msg': '参数错误',
            })

        result, password_new = Password.get_password(password)
        if not result:  # 若上一步返回false
            return flask.jsonify({
                'code': types.RESPONSE_CODE.PARAMETER_ERROR,
                'msg': '参数错误',
            })

        user = TRAdminUsers.query.filter_by(email=email, password=password).first()
        if not user:
            return flask.jsonify({
                'code': types.RESPONSE_CODE.DATA_NOT_EXIST,
                'msg': '邮箱或密码错误',
            })
        user.signin_time = datetime.datetime.now()
        user.ip = ip
        db.session.commit()
        token = generate(user)	
        resp = flask.jsonify(code=types.RESPONSE_CODE.SUCCESS, data=User.build_data(user))
        resp.set_cookie(COOKIE_NAME, value=token.token, expires=token.expires)
        return resp

class User(object):

    @staticmethod
    def build_data(user):
        if not isinstance(user, TRAdminUsers):
            return None

        return {
            'uid': user.uid,
            'name': user.name,
            'email': user.email,
            'ip': user.ip,
            'createby': user.createby,
            'signin_time': user.signin_time
        }
