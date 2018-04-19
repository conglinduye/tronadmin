# !/usr/bin/env python
# *-* coding:utf-8 *-*
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.config import log

app, db = create_app()

if __name__ == '__main__':
    log.init_log()
    app.run()
