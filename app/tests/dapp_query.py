# coding=utf-8
import json
import urllib2
import urllib

__author__ = 'lmr'


class TronData(object):


    def send_msg(self):
        # self.SMS_URL = 'https://tron.network/api/v1/dapp_event/review_submit'
        self.SMS_URL = 'http://localhost:5000/api/v1/query_search'  # 线上
        # self.SMS_URL = 'http://172.16.100.1:8990/api/admin/dapp_update_date/update_dapp'  # 测试
        self.params = {}
        self.params['did'] = 27695316
        self.data = urllib.urlencode(self.params)
        resp = urllib2.urlopen(self.SMS_URL, self.data)
        print resp.read()


if __name__ == '__main__':
    tron = TronData()
    tron.send_msg()
    print "success"
