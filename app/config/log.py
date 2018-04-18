# !/usr/bin/env python
# *-* coding:utf-8 *-*
import os

import sys

import logging

import time


def init_log():
    file_name = "tronlab_admin"
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctlsime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s',
                        filename='{}_{}.log'.format(file_name, time.strftime('%Y-%m-%d')))
    logging.info("logging start...")