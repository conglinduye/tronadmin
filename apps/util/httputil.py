# !/usr/bin/env python
# *-* coding:utf-8 *-*
import traceback
from httplib import BadStatusLine
import logging
from eventlet.green import urllib2

def urlopen(url, timeout=5):
    try:
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)')
        response = urllib2.urlopen(request, timeout=timeout)
        data = response.read()
        return data
    except BadStatusLine:
        logging.info('ulropen error!url:%s BadStatusLine' % (url, ))
    except :
        logging.error('ulropen error!url:%s %s' % (url, traceback.format_exc()))