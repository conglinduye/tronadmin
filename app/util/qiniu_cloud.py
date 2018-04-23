# -*- coding: utf-8 -*-
# date:2018/04/20

import os
import sys
from qiniu import Auth, put_file, put_data

from app.config import ACCESS_KEY, SECRET_KEY, BUCKET_NAME, DOMAIN_PREFIX

__author__ = "lmr"

if 3 != len(sys.argv):
    print('[Usage] %s [dir_set] [filepath]' % os.path.basename(sys.argv[0]))
    sys.exit(0)
else:
    # dir_set 的格式为 image/upload-qiniu/ ，注意末尾带反斜杠/
    dir_set = sys.argv[1]  # 域名下的文件夹
    file_path = sys.argv[2]

# 个人中心->密匙管理->AK
access_key = ACCESS_KEY
# 个人中心->密匙管理->SK
secret_key = SECRET_KEY
# 七牛空间名
bucket_name = BUCKET_NAME
domain_prefix = DOMAIN_PREFIX  # 域名

qiniu_auth = Auth(access_key, secret_key)


def upload_qiniu(input_path):
    # upload single file to qiniu
    filename = os.path.basename(input_path)
    key = '%s%s' % (dir_set, filename)

    token = qiniu_auth.upload_token(bucket_name, key)
    ret, info = put_file(token, key, input_path, check_crc=True)
    if ret and ret['key'] == key:
        url = 'http://p7476x5w6.bkt.clouddn.com/' + dir_set + filename
        print('%s done' % ('http://p7476x5w6.bkt.clouddn.com/' + dir_set + filename))
    else:
        print('%s error' % ('http://p7476x5w6.bkt.clouddn.com/' + dir_set + filename))


def upload_all_files(input_path):
    if os.path.isfile(input_path):
        upload_qiniu(input_path)
    elif os.path.isdir(input_path):
        dirlist = os.walk(input_path)
        for root, dirs, files in dirlist:
            for filename in files:
                upload_qiniu(os.path.join(root, filename))
    else:
        print('Please input the exists file path!')


# api调用
def qiniu_upload_file(source_file, save_file_name):
    # 生成上传 Token，可以指定过期时间等
    token = qiniu_auth.upload_token(bucket_name, save_file_name)

    ret, info = put_data(token, save_file_name, source_file.stream)

    print(type(info.status_code), info)
    if info.status_code == 200:
        return domain_prefix + save_file_name
    return None


# python qiniu_cloud.py image/  /Users/troncoin/Desktop/sr.png
if __name__ == "__main__":
    upload_all_files(file_path)
