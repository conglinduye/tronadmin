#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:

from app.model.tr_dapp import TRDapp


class DAPPTest(object):

    dapp_id = 93915706
    dapps = TRDapp.select(dapp_id=dapp_id)

    print dapps

if __name__ == '__main__':
    DAPPTest()