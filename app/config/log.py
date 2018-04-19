# !/usr/bin/env python
# *-* coding:utf-8 *-*

import logging

import time

__author__ = "lmr"


def init_log():
    file_name = "tronlab_admin"
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s',
                        filename='{}_{}.log'.format(file_name, time.strftime('%Y-%m-%d')),
                        filemode='w')
    logging.info("logging start...")