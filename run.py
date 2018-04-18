# !/usr/bin/env python
# *-* coding:utf-8 *-*

from app import create_app
from app.config import log

app = create_app()

if __name__ == '__main__':
    log.init_log()
    app.run()
