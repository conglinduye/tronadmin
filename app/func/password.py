# -*- coding: utf-8 -*-

from app import config
from app.util import encrypt_util
from app.util.rsa_util import RSAUtil

__author__ = 'keelson'


class Password(object):

    @staticmethod
    def get_password(password, need_decrypt=False):  #need_decrypt  是否需要破译 2017／8／10
        password_new = password
        if need_decrypt:      #如果需要破译 2017／8／10
            decrypt_result = False
            try:
                password_new = RSAUtil.decrypt(password_new)  #破译密码返回值 2017／8／10
                if password_new != RSAUtil.FAIL_RESULT:   #如果返回值 != '_FAIL_' 2017／8／10
                    decrypt_result = True                 #破译成功 2017／8／10
            except:
                pass
            if not decrypt_result:         # 破译失败  2017／8／10
                return False, password
        password_new = encrypt_util.md5('%s_%s' % (config.PASSWORD_SALT, password_new))  #密码加密 2017／8／10
        return True, password_new    # 返回加密后的密码  2017／8／10
