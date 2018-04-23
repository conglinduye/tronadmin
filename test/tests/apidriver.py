#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import json
import urllib
import urllib2
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class APIDriver(object):
    def __init__(self, url, params=None, method='get'):
        self.url = url
        self.method = method
        self.params = params
        # 处理中文参数
        self.encode_params()

    def encode_params(self):
        if not self.params:
            return

        for key, value in self.params.items():
            if isinstance(value, unicode):
                self.params[key] = value.encode('utf-8')

    def run(self, timeout=10):
        if self.method and self.method.lower() == 'post':
            return self._run_post(timeout)
        elif self.method and self.method.lower() == 'put':
            return self._run_put(timeout)
        else:
            return self._run_get(timeout)

    def _run_post(self, timeout):
        try:
            data = urllib.urlencode(self.params)
            resp_data = urllib2.urlopen(
                self.url, data=data, timeout=timeout).read()
            return json.loads(resp_data)
        except Exception, e:
            print '%s. POST %s with %s' % (e, self.url, self.params)
            return None

    def _run_get(self, timeout):
        try:
            query = urllib.urlencode(self.params)
            request = urllib2.Request('%s?%s' % (self.url, query))
            data = urllib2.urlopen(request, timeout=timeout).read()
            print 'resp_data:%s' % data
            return json.loads(data)
        except Exception, e:
            print '%s. GET %s with %s' % (e, self.url, self.params)
            return None

    def _run_put(self, timeout):
        try:

            data = urllib.urlencode(self.params)
            '''
            resp_data = urllib2.urlopen(
                self.url, data=data, timeout=timeout).read()
            '''

            '''
                        # data = json.dumps(self.params)
            request = urllib2.Request(url=self.url, data=data)
            request.add_header('Content-Type', 'application/json')
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.get_method = lambda: 'PUT'
            resp = urllib2.urlopen(request)

            return json.loads(resp.read())
            '''

            # print data

            header = {'Content-Type': 'application/x-www-form-urlencoded'}
            resp = requests.put(url=self.url, data=data, headers=header, timeout=timeout)
            return json.loads(resp.content)

        except Exception, e:
            print '%s. PUT %s with %s' % (e, self.url, self.params)
            return None
