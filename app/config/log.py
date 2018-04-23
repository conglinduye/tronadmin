# !/usr/bin/env python
# *-* coding:utf-8 *-*

import logging

import time

__author__ = "lmr"


def init_log():
    file_name = "tronlab_admin"
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s',
                        filename='{}.log'.format(file_name),
                        filemode='w')
    logging.info("logging start...")
