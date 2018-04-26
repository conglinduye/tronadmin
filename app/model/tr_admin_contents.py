# !/usr/bin/env python
# *-* coding:utf-8 *-*
# date:2018/04/26
import random
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from app import db

__author__ = "lmr"


class TRAdminContents(db.Model):
    __tablename__ = 'tr_admin_contents'

    id = db.Column(db.Integer, primary_key=True)
    # tid = db.Column(db.Integer, nullable=False)                  # 内容ID
    name = db.Column(db.String())                                  # 内容名称
    content = db.Column(db.Text)                                   # 内容详情
    create_by = db.Column(db.String())
    status = db.Column(db.Integer, default=0, nullable=False)      # 0未上线，1上线中，2上线过
    delete = db.Column(db.Integer, default=0, nullable=False)      # 0未删除 1已删除
    online_time = db.Cloumn(TIMESTAMP)                             # 上线时间
    downline_time = db.Cloumn(TIMESTAMP)                           # 下线时间
    update_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)     # 更新时间
    create_time = db.Column(TIMESTAMP, server_default=func.now(), nullable=False)     # 创建时间
