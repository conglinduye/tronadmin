#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import getopt
import os
import sys

from apitester import APITester


def hashopts(pattern):
    try:
        opts, args = getopt.getopt(sys.argv[1:], pattern)
        myopts = {}
        for key, value in opts:
            myopts[key] = value or True
        return myopts
    except Exception:
        usage()


def usage():
    print '''
Description: 跑测试用例

Usage:
    python %s [options]

OPTIONS:
   -h    查看帮助文档
   -i    输出请求详细（默认仅输出错误的用例）
   -f    文件路径(默认测试全部tests文件夹下的)
   -p    结果短信通知
''' % __file__
    sys.exit(1)


TESTPATH = 'test/tests'


def work():
    myopts = hashopts('hif:p:')
    myopts.get('-h') and usage()
    filename = myopts.get('-f')
    phones = myopts.get('-p')

    base = TESTPATH
    if filename:
        if filename.startswith(TESTPATH):
            filename = filename[len(TESTPATH):]
        if os.path.isfile(TESTPATH + '/' + filename):
            files = [filename]
        else:
            base = '%s/%s' % (base, filename)
            files = os.listdir(base)
    else:
        files = os.listdir(TESTPATH)

    fails = 0
    total = 0
    for each in files:
        full_path = base + '/' + each
        if os.path.isdir(full_path):
            continue
        print each, ':'
        tester = APITester()
        tester.load(full_path)
        tester.run()
        tester.summary()
        print '\n'

        if myopts.get('-i'):
            tester.report()
            print '\n'

        fails += tester.fail_number
        total += len(tester.tests)
    if phones:
        if fails:
            msg = "【失败- %s环境】: 共%s个测试, 其中%s个未通过" % (filename, total, fails)
        else:
            msg = "【成功- %s环境】: 共%s个测试, 全部通过" % (filename, total)
        os.system("curl -d 'password=hellokitty&phones=%s&msg=%s' https://api.raybo.com:2443/v1.0/report/warning" % (
        phones, msg))

        if fails:
            exit(1)


work()
