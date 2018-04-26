#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lmr

import os
from flask import redirect, url_for
from werkzeug import secure_filename

from app.config import ALLOWED_EXT, UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT


def upload_file(files):
    if files and allowed_file(files.filename):
        filename = secure_filename(files.filename)
        files.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))


if __name__ == '__main__':
    url = upload_file("files")
