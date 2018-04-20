#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "lmr"


class RESPONSE_CODE(object):  # 错误编码 2017／8／9
    # success
    SUCCESS = 0

    # http response code
    # /Library/Python/2.7/site-packages/twisted/web/_responses.py
    RESPONSE_FOUND = 302

    # system error
    PARAMETER_ERROR = 10001  # 参数错误 2017／8／9
    USER_AUTH_ERROR = 10002
    PERMISSION_ERROR = 10003  # 许可信息错误 2017／8／9
    SESSION_EXPIRED = 10004     # session过期
    # service error
    OPERATE_FREQUENTLY = 20001  # 操作频繁 2017／8／9
    OPERATE_ERROR = 20002  # 操作错误 2017／8／9
    DATA_NOT_AVAILABLE = 20003  # 没有获得数据 2017／8／9
    DATA_ALREADY_EXIST = 20004  # 数据已经存在 2017／8／9
    DATA_NOT_EXIST = 20005  # 数据不存在 2017／8／9
    APP_NEED_UPDATE = 20007  # app需要更新 2017／8／9
    FILE_UPLOADER_INVALID = 20008  # 文件上传的handler已经无法使用
    FILE_UPLOADER_ING = 20009  # 文件正在上传
    FILE_EXPIRE = 20010  # 文件过期
    CAPTCHA_LIMIT_COUNT = 20011  # 验证码次数超过上限
    CAPTCHA_LIMIT_INTERVAL = 20012  # 验证码间隔太短