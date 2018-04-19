# -*- coding:utf8 -*-
# date:2018/04/08
import datetime
import random
import apps.config
from apps.core.DAO import DAO
__author__ = "lmr"


class TRDapp(DAO):

    TABLE = 'tr_dapp'
    COLUMNS = ['dapp_id', 'dapp_name', 'author', 'dapp_email', 'brief', 'description', 'wallet_address', 'license',
               'status', 'social_link1', 'social_link2', 'pv', 'web_url', 'dapp_url', 'logo_url', 'tags', 'update_time',
               'create_time', 'review']