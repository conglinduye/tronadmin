# *-* coding:utf-8 *-*
# date:2018/04/19

from flask import Blueprint, render_template, redirect, request
from app.api import api
from app.models import TRDapp
import json

__author__ = "lmr"


@api.route('/dapp_submit', methods=['GET','POST'])
class DappSubmit(object):

    pass