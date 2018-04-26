#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import base64
import hashlib

import pyDes

from app import config


def md5(data):
    return hashlib.md5(data).hexdigest().lower()


def base64_encode(data):
    return base64.b64encode(data)


def simple_xor(data, key):
    arr = []
    data_length = len(data)
    key_length = len(key)
    for i in xrange(data_length):
        j = i % key_length
        arr.append(chr(ord(data[i]) ^ ord(key[j])))
    return ''.join(arr)


def des_3_encrpy(data, key=None):
    # 3des 加密
    if not key:
        key = config.TRIPLE_DES_KEY
    iv = key[0:8]

    des = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    s = des.encrypt(data)
    return base64.b64encode(s)


def des_3_decrypt(data, key=None):
    if not key:
        key = config.TRIPLE_DES_KEY
    if not data:
        return ''
    iv = key[0:8]

    des = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    data_b64decode = base64.b64decode(data)
    s = des.decrypt(data_b64decode)
    return s


if __name__ == '__main__':
    # from btcutil import BtcUtil
    # import encrypt_util
    # private_key, public_key, address = BtcUtil.get_all()
    # private_key_encrypt = encrypt_util.des_3_encrpy(private_key)
    # print 'private_key:', private_key
    # print 'public_key:', public_key
    # print 'address:', address
    # print 'private_key_encrypt:', private_key_encrypt
    # private_key_decrypt = des_3_decrypt(private_key_encrypt)
    # print 'private_key_decrypt:', private_key_decrypt

    # a = 'aJk9e3OINEJo/m2ic6OZ1OgomujvR259YzfT0oyNB7df5FbiCczG9LqyJCs7m5AexUKHy1WfSRc='
    # a = 'atz6k0uIVzCz2GbnlR0pqhLNSHHAAktL27wWKVHK5bisHYLdiSCw3P5IbsXogea7EltUJ4JpsL4='
    # b = des_3_decrypt(a)
    # c = BtcUtil.get_address_from_private(b)
    # print a
    # print b
    # print c

    address = '0x8d6bfe1558506e2246cb5d7f31220a1fba4cffc9'
    private_key = 'c332c780e8465fb6ab5244866534256b62c9ec1997c0fedc25c98ae1eee77254'
    private_key_en = des_3_encrpy(private_key, key='Ts9nUGskSvp17hQBi0jPwtQm')
    private_key_de = des_3_decrypt(private_key_en, key='Ts9nUGskSvp17hQBi0jPwtQm')

    print address, private_key, private_key_en, private_key_de

    #
    # import os
    #
    # cwd = os.getcwd()
    # print cwd

    pass
