# !/usr/bin/env python
# *-* coding:utf-8 *-*

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from app.api import api
    app.register_blueprint(api)
    db.init_app(app)
    return app
