# !/usr/bin/env python
# *-* coding:utf-8 *-*
import traceback


import logging

from apps import config
from qiniu import Auth, put_data

from apps.util.httputil import urlopen


class QiniuCloud(object):
    INSTANCE = None

    @classmethod
    def get_token(cls, key, bucket, policy=None):
        if not cls.INSTANCE:
            cls.INSTANCE = Auth(config.QINIU_KEY, config.QINIU_SECRET)

        return cls.INSTANCE.upload_token(bucket, key, 3600, policy=policy)

    @classmethod
    def upload_file(cls, url, key, bucket, timeout=5):
        token = cls.get_token(key, bucket)
        if not cls.INSTANCE:
            cls.INSTANCE = Auth(config.QINIU_KEY, config.QINIU_SECRET)
        try:
            # data = urllib2.urlopen(url, timeout=timeout).read()
            data = urlopen(url, timeout=timeout)
            ret, info = put_data(token, key, data)
        except:
            logging.error('WEIXIN URL: %s download failed.\n%s' % (url, traceback.format_exc()))