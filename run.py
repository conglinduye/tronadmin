# !/usr/bin/env python
# *-* coding:utf-8 *-*
import sys
import getopt
import shutil

from app import create_app

app = create_app()


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
Description: 各服务启动脚本

Usage:
    python %s [options]

OPTIONS:
   -h    查看帮助文档
   -t    类型
   -e    环境(对于与config下的py文件, 必填)
   -p    端口(option)
   -q    队列名(option)
   -a    admin服务,启动admin服务

参数t(服务类型)种类:
-- api: web服务
   参数: -p api服务监听的端口

-- event: 事件处理模块


1) 启动admin
python run.py -p 5000 -e production_test

''' % __file__
    sys.exit(1)


if __name__ == '__main__':
    myopts = hashopts('hat:p:q:c:i:l:m:f:e:')
    env = myopts.get('-e') or usage()
    print env
    shutil.copy('app/config/%s.py' % env, 'app/config/configure.py')

    from app.config import log

    log.init_log()

    port = myopts.get('-p') or usage()   # 🈯️指定端口号

    app.run(host='0.0.0.0', port=int(port))
