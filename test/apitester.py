#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import copy
import hashlib
import json
import random
import time
import urllib

import jsonschema

from apidriver import APIDriver


class AUTH_LEVEL(object):
    NO_AUTH = 0
    NORMAL = 1
    STRICT = 2


class APITester(object):

    SIGNIN_URL = '/account/signin'

    def __init__(self):
        self.host = None
        self.env = {'app': 1}
        self.user = None
        self.tests = []
        self.reports = []
        self.fail_number = 0
        self.fails = []
        self.auth = 0

    def add_report(self, msg):
        self.reports.append(msg)

    def load(self, filename):
        try:
            db_file = file(filename)
            data = json.load(db_file)
            self.host = data.get('host')
            self.user = data.get('user')
            if self.user and self.user.get('password') and self.user.get('uid') != 1:
                self.user['password'] = hashlib.md5(
                    self.user.get('password')).hexdigest()
            self.env.update(data.get('env'))
            self.tests = data.get('tests')
            self.auth = data.get('auth', 0)

            if not self.host:
                self.add_report('MSG: no host in json')
            if not self.tests:
                self.add_report('MSG: no tests to run')

        except:
            self.add_report('MSG: File not found or json error')

    def run(self, sign=True):
        if not self.host:
            self.add_report('MSG: host not set')
            return

        for test in self.tests:
            url = self.host + test.get('api')
            params = test.get('params') or {}
            method = test.get('method') or 'get'
            self.add_report('MSG: request %s with %s' % (url, str(params)))
            params = self.prepare(params, method, test.get('api'))

            resp = APIDriver(url, params, test.get('method')).run()
            self.add_report('RESPONSE: \n %s' % json.dumps(resp, indent=2, ensure_ascii=False))

            if not self.validate(resp, test.get('except')):
                self.fail_number += 1
                self.fails.append('MSG: request %s with %s' %
                                  (url, str(params)))
                self.fails.append('RESPONSE: \n %s' %
                                  json.dumps(resp, indent=2, ensure_ascii=False))

    def prepare(self, params, method, path):
        def quote(_v):
            if isinstance(_v, unicode):
                _v = _v.encode('utf-8')
            return urllib.quote(str(_v), "!#$&'()*+,-./:;=?@_~")

        if self.auth == AUTH_LEVEL.NO_AUTH:
            extra_params = {}
        else:
            if self.auth == AUTH_LEVEL.STRICT:
                assert 'session_data' in params
            extra_params = {
                'nonce': str(random.randint(0, 1000000)),
                'timestamp': str(int(time.time())),
            }

        if path.startswith('/'):
            path = path[1:]
        method = method.upper()
        new_param = copy.deepcopy(params)
        new_param.update(extra_params)
        new_param.update(self.env)
        if self.user:
            new_param.update(self.user)

        params_tp = sorted(new_param.iteritems())
        params_str = '&'.join(['%s=%s' % (k, quote(v)) for k, v in params_tp])
        sign_src = ''.join((method, path, params_str))

        if 'sign' not in new_param:
            new_param['sign'] = hashlib.md5(sign_src).hexdigest().lower()

        # print 'params_str=%s, sign_src=%s, sign=%s' % (params_str, sign_src, new_param['sign'])

        return new_param

    def validate(self, resp, schema):
        try:
            jsonschema.validate(resp, schema)
            return True
        except:
            return False

    def summary(self):
        print "%s Test case, %s failed" % (len(self.tests), self.fail_number)
        if self.fail_number:
            print '\n\n'.join(self.fails)

    def report(self):
        print '\n\n'.join(self.reports)
