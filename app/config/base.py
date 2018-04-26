# *-* coding:utf-8 *-*
# date:2018/04/19

import logging
import json
import time
import traceback

import ujson

from flask import request

from app import config
from flask_restful import Resource

from app.model import types
from app.util.iputil import get_http_real_ip

__author__ = "lmr"


def arg_named(request, arg_name, default=None):
    """return named arg in request

    the type of arg depends on the type of default value.
    """
    try:
        argument = request.args.get(arg_name)[0]
        if default is None:
            return argument
        # 如果传过来的是空, 而默认值是字符串, 需要给默认值
        elif isinstance(default, basestring):
            return argument or default
        elif isinstance(default, int):
            return int(argument)
        elif isinstance(default, float):
            return float(argument)
    except:
        return default


def list_params(params, int_value=False):
    if not params:
        return []
    if int_value:
        try:
            return [int(param.strip()) for param in params.split(',')]
        except:
            return
    else:
        return [param.strip() for param in params.split(',')]


class GreenResource(Resource):
    FREQUENTLY_CHECK_TIME = None
    FREQUENTLY_CHECK_KEYS = []

    def post(self):
        pass

    def handle_request(self, handler, request):
        try:
            start_time = time.time()
            '''
            # request.user = request_user

            # add client version to request
            
            cli_ver = arg_named(request, 'version', 0)
            if not cli_ver:
                cli_ver = config.APP_VERSION_DEFAULT
            request.cli_ver = cli_ver
            '''
            resp = handler(request)

            # response code
            resp_code = types.RESPONSE_CODE.SUCCESS

            # 添加时间戳
            if isinstance(resp, dict):
                resp['current_time'] = time.time()
                resp_code = resp.get('code', types.RESPONSE_CODE.SUCCESS)

            # 302
            if resp_code == types.RESPONSE_CODE.RESPONSE_FOUND:
                url = resp.get('msg') or config.OFFICIAL_WEB_URL
                # logging.info('302_redirect path:%s args:%s url:%s' % (request.path, request.args, url))
                request.redirect(url)
                request.finish()
                return

            # json打包
            if not isinstance(resp, basestring):
                try:
                    resp = ujson.dumps(resp)
                except:
                    try:
                        resp = json.dumps(resp)
                    except:
                        logging.info('dumps error! resp:%s' % resp)
                        resp = str(resp)

            cb = arg_named(request, 'callback')
            if cb:
                resp = '%s(%s)' % (cb, resp)

            request.setHeader('Content-Type', 'text/json; charset=utf-8')
            # request.setHeader('Access-Control-Allow-Origin', '*')    # 2018-
            request.write(resp)

            try:
                request.finish()
            except:
                pass

            end_time = time.time()
            cost_time = end_time - start_time
            if cost_time > config.API_SLOW_LOG_TIME:
                if request.path in ['/util/status']:
                    pass
                else:
                    if hasattr(config, 'API_LOG_ARGS_FLAG'):
                        logging.info(
                            'path:%s cost %.2f seconds args:%s, ip:%s, resp: %s',
                            request.path, cost_time, request.args, get_http_real_ip(request),  resp)
                    else:
                        logging.info(
                            'path:%s cost %.2f seconds args:%s ip:%s resp_code:%s, resp_size:%s',
                            request.path, cost_time, request.args, get_http_real_ip(request), resp_code, len(resp))
        except Exception, e:
            logging.info('api_error 2. path:%s args:%s e:%s',
                         request.path, request.args, e)
            logging.error(traceback.format_exc())

    def handle_request1(self, handler, request):
        try:
            start_time = time.time()
            '''
            # request.user = request_user

            # add client version to request

            cli_ver = arg_named(request, 'version', 0)
            if not cli_ver:
                cli_ver = config.APP_VERSION_DEFAULT
            request.cli_ver = cli_ver
            '''
            resp = handler(request)

            # response code
            resp_code = types.RESPONSE_CODE.SUCCESS

            # 添加时间戳
            if isinstance(resp, dict):
                resp['current_time'] = time.time()
                resp_code = resp.get('code', types.RESPONSE_CODE.SUCCESS)

            # 302
            if resp_code == types.RESPONSE_CODE.RESPONSE_FOUND:
                url = resp.get('msg') or config.OFFICIAL_WEB_URL
                # logging.info('302_redirect path:%s args:%s url:%s' % (request.path, request.args, url))
                request.redirect(url)
                request.finish()
                return

            # json打包
            if not isinstance(resp, basestring):
                try:
                    resp = ujson.dumps(resp)
                except:
                    try:
                        resp = json.dumps(resp)
                    except:
                        logging.info('dumps error! resp:%s' % resp)
                        resp = str(resp)

            cb = arg_named(request, 'callback')
            if cb:
                resp = '%s(%s)' % (cb, resp)

            request.setHeader('Content-Type', 'text/json; charset=utf-8')
            # request.setHeader('Access-Control-Allow-Origin', '*')    # 2018-
            request.write(resp)

            try:
                request.finish()
            except:
                pass

            end_time = time.time()
            cost_time = end_time - start_time
            if cost_time > config.API_SLOW_LOG_TIME:
                if request.path in ['/util/status']:
                    pass
                else:
                    if hasattr(config, 'API_LOG_ARGS_FLAG'):
                        logging.info(
                            'path:%s cost %.2f seconds args:%s, ip:%s, resp: %s',
                            request.path, cost_time, request.args, get_http_real_ip(request), resp)
                    else:
                        logging.info(
                            'path:%s cost %.2f seconds args:%s ip:%s resp_code:%s, resp_size:%s',
                            request.path, cost_time, request.args, get_http_real_ip(request), resp_code, len(resp))
        except Exception, e:
            logging.info('api_error 2. path:%s args:%s e:%s',
                         request.path, request.args, e)
            logging.error(traceback.format_exc())


def deco(func):
    def handle_request(*args, **kwargs):
        try:

            start_time = time.time()
            resp = {}
            func(*args, **kwargs)
            # response code
            resp_code = types.RESPONSE_CODE.SUCCESS

            # 添加时间戳
            if isinstance(resp, dict):
                resp['current_time'] = time.time()
                resp_code = resp.get('code', types.RESPONSE_CODE.SUCCESS)

            # 302
            if resp_code == types.RESPONSE_CODE.RESPONSE_FOUND:
                url = resp.get('msg') or config.OFFICIAL_WEB_URL
                # logging.info('302_redirect path:%s args:%s url:%s' % (request.path, request.args, url))
                request.redirect(url)
                request.finish()
                return

            # json打包
            if not isinstance(resp, basestring):
                try:
                    resp = ujson.dumps(resp)
                except:
                    try:
                        resp = json.dumps(resp)
                    except:
                        logging.info('dumps error! resp:%s' % resp)
                        resp = str(resp)

            cb = arg_named(request, 'callback')
            if cb:
                resp = '%s(%s)' % (cb, resp)

            request.setHeader('Content-Type', 'text/json; charset=utf-8')
            # request.setHeader('Access-Control-Allow-Origin', '*')    # 2018-
            request.write(resp)

            try:
                request.finish()
            except:
                pass

            end_time = time.time()
            cost_time = end_time - start_time
            if cost_time > config.API_SLOW_LOG_TIME:
                if request.path in ['/util/status']:
                    pass
                else:
                    if hasattr(config, 'API_LOG_ARGS_FLAG'):
                        logging.info(
                            'path:%s cost %.2f seconds args:%s, ip:%s, resp: %s',
                            request.path, cost_time, request.args, get_http_real_ip(request), resp)
                    else:
                        logging.info(
                            'path:%s cost %.2f seconds args:%s ip:%s resp_code:%s, resp_size:%s',
                            request.path, cost_time, request.args, get_http_real_ip(request), resp_code, len(resp))
        except Exception, e:
            logging.info('api_error 2. path:%s args:%s e:%s',
                         request.path, request.args, e)
            logging.error(traceback.format_exc())

    return handle_request