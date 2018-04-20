# *-* coding:utf-8 *-*
# date:2018/04/19

from flask import request
__author__ = "lmr"


def arg_named(arg_name, default=None):
    """return named arg in request

    the type of arg depends on the type of default value.
    """
    try:
        # argument = request.args.get(arg_name)[0]
        argument = request.headers(arg_name)
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