# -*- coding: utf-8 -*-
import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from app import config
import os

__author__ = 'keelson'


def get_file_name(file_name):
    cwd = os.getcwd()
    if cwd.endswith('util'):
        return '../' + file_name
    else:
        return file_name


class RSAUtil(object):

    FAIL_RESULT = '_FAIL_'

    cipher_priv, cipher_pub = None, None

    @classmethod
    def init(cls):
        try:
            cls.private_key = RSA.importKey(open(get_file_name(config.RSA_PRIVATE_KEY)).read())
            cls.cipher_priv = PKCS1_v1_5.new(cls.private_key)
        except:
            pass

        try:
            cls.public_key = RSA.importKey(open(get_file_name(config.RSA_PUBLIC_KEY)).read())
            cls.cipher_pub = PKCS1_v1_5.new(cls.public_key)
        except:
            pass

    @classmethod
    def decrypt(cls, data):
        data_b64decode = base64.b64decode(data)
        result = cls.cipher_priv.decrypt(data_b64decode, RSAUtil.FAIL_RESULT)
        return result

    @classmethod
    def encrypt(cls, data):
        result = cls.cipher_pub.encrypt(data)
        return base64.b64encode(result)

    @classmethod
    def sign(cls, data):
        h = SHA256.new(data)
        signature = cls.cipher_priv.sign(h)
        return signature

    @classmethod
    def verify(cls, data, signature):
        h = SHA256.new(data)
        result = cls.cipher_pub.verify(h, signature)
        return result

RSAUtil.init()


class RSAEncrypt(object):
    cipher = None

    @classmethod
    def init(cls):
        try:
            public_key = RSA.importKey(open(get_file_name(config.RSA_PUBLIC_KEY_2)).read())
            cls.cipher = PKCS1_v1_5.new(public_key)
        except:
            pass

    @classmethod
    def encrypt(cls, data):
        result = cls.cipher.encrypt(data)
        return base64.b64encode(result)

    @classmethod
    def verify(cls, data, signature):
        h = SHA256.new(data)
        result = cls.cipher.verify(h, signature)
        return result


RSAEncrypt.init()


class RSADecrypt(object):
    cipher = None

    @classmethod
    def init(cls):
        try:
            private_key = RSA.importKey(open(get_file_name(config.RSA_PRIVATE_KEY_2)).read())
            cls.cipher = PKCS1_v1_5.new(private_key)
        except:
            pass

    @classmethod
    def decrypt(cls, data):
        data_b64decode = base64.b64decode(data)
        result = cls.cipher.decrypt(data_b64decode, RSAUtil.FAIL_RESULT)
        return result

    @classmethod
    def sign(cls, data):
        h = SHA256.new(data)
        signature = cls.cipher.sign(h)
        return signature

RSADecrypt.init()


if __name__ == '__main__':
    # a = '123'
    # print a
    # b = RSAEncrypt.encrypt(a)
    # print len(b), b
    # c = RSADecrypt.decrypt(b)
    # print c

    # a = '123'
    # print a
    # b = RSAUtil.encrypt(a)
    # print len(b), b
    # c = RSAUtil.decrypt(b)
    # print c

    # p = '1FyfPyzvuT7riBB4T4zA5nL9jjnHuUCt1W'
    # a = 'UzmncpcgpItu6Oqvf2TsBBZkbghV5HaHqkHOVuM4MU8RR4KYtosa90Ntiq5KlNg5hyrjoJJ+0o+AEMmvoEJMQ1kDUTrj+Jj2BXAUxfjC2yh0mxg/VLBn3TlwMaLO5A8QJ8kkFRRVn2mUCaGZ4Q4zM1b6xO1LmGdcu22J1fy+kP8='
    # b = RSADecrypt.decrypt(a)
    # print b
    # from btcutil import BtcUtil
    # c = BtcUtil.get_address_from_private(b)
    # print c, c == p

    # from util.eth_util import EthUtil
    p = '0x57aaf952dcd4c7dec42ec11e84489845ce3d2df9'
    a = 'Izo8H8mOHI/xfRIQ5J0v32LXkx8FIi0uuLr/0N0cS/87YDoWZLOG8kRitKIHU2ku6LNDu1HbkyEuh3wI94MXx+Tbwq78HPnp2J6tAhCUqCSAsmCiHY3nMf1ewkBGwJ0y4Sm4cKKGQPpPdpE1pfpugZMRTL1Gtb/yuBuZVh7oYEY='
    b = RSADecrypt.decrypt(a)
    print b
    # c = EthUtil.get_address_from_private(b)
    # print c, c == p

    pass
