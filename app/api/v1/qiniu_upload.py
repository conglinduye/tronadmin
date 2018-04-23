# *-* coding:utf-8 *-*
# date:2018/04/19

import logging
import uuid
from flask import request

from app.api import api
from app.model import types
from app.util.qiniu_cloud import qiniu_upload_file

__author__ = "lmr"


@api.route('/upload/', methods={'post'})
def upload():
    files = request.files['file']
    file_ext = ''
    if files.filename.find('.') > 0:
        file_ext = files.filename.rsplit('.', 1)[1].strip().lower()
    if file_ext in api.config['ALLOWED_EXT']:
        file_name = str(uuid.uuid1()).replace('-', '') + '.' + file_ext
        # url=save_to_local(file,file_name)
        url = qiniu_upload_file(file, file_name)
        if url != None:
            logging.info("qiniu generated url address is {}".format(url))
            pass
            # db.session.add(Image(url, current_user.id))  数据库保存url
            # db.session.commit()
