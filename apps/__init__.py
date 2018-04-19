# !/usr/bin/env python
# *-* coding:utf-8 *-*

from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from apps import models


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)   # 通过配置文件进行配置，好处在于将配置信息集中处理
    from apps.api.views import blueprint
    app.register_blueprint(blueprint)
    db = SQLAlchemy(app)
    return app, db


