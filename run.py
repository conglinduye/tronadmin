# !/usr/bin/env python
# *-* coding:utf-8 *-*
from flask_sqlalchemy import SQLAlchemy

from apps import create_app
from apps.config import log

app, db = create_app()

if __name__ == '__main__':
    log.init_log()
    app.run()
