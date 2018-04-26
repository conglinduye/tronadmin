# -*- coding: utf-8 -*-
import re

__author__ = "lmr"


class Email(object):
    R = re.compile(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){1,2}$')

    @staticmethod
    def verify(email):
        return True if Email.R.match(email) else False  # 正则表达式判断邮箱是否合法