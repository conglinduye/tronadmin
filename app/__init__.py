# !/usr/bin/env python
# *-* coding:utf-8 *-*

from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from app.api.views import blueprint
    app.register_blueprint(blueprint)
    return app
