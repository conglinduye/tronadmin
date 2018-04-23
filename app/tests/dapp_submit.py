# coding=utf-8
import urllib
import urllib2

__author__ = 'lmr'


class TroData(object):
    def send_msg(self):
        # self.SMS_URL = 'https://tron.network/api/v1/dapp_event/review_submit'
        self.SMS_URL = 'http://localhost:5000/api/v1/dapp_submit1'  # 线上
        self.params = {}
        self.params['dapp_name'] = "flask"
        self.params['author'] = "linmaorong"
        # self.params['dapp_email'] = "123456@qq.com"
        self.params['brief'] = "this is a flask tests"
        # self.params['description'] = "this is a flask tests, holp success!!!"
        # self.params['wallet_address'] = "ox2sd34gfdg34tgdgf23gdft24fdsg3g2"
        # self.params['license'] = "Dr2Dsf34FFEA"
        self.params['status'] = 2
        # self.params['social_link1'] = "1wwse3@com.cn"
        # self.params['web_url'] = "www.baidu,com"
        self.data = urllib.urlencode(self.params)
        resp = urllib2.urlopen(self.SMS_URL, self.data)
        print resp.read()


if __name__ == '__main__':
    tron = TroData()
    tron.send_msg()
    print "success"
