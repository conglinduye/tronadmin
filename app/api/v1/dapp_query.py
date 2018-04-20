# *-* coding:utf-8 *-*
# date:2018/04/19
import flask
from flask import request
from app.api import api
from app.models import TRDapp
import json

__author__ = "lmr"


@api.route('/dapp_search', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':

        dapp_id = request.form.get("did", 0)
        delete = request.form.get("delete", 0)
        dapp_name = request.form.get("dapp_name")
        dapps = TRDapp.query_filter(dapp_id=dapp_id, delete=delete, dapp_name=dapp_name)
        content = great_date(dapps)
        # return json.dumps({"data": content}, ensure_ascii=False)
        return flask.jsonify({"data": content})


def great_date(dapps):
    dapp_list = []  # 返回的数据
    for dapp in dapps:
        dapp_dict = {}  # 数据列表中的值
        dapp_dict["dapp_id"] = dapp.dapp_id
        dapp_dict["dapp_name"] = dapp.dapp_name
        dapp_dict["author"] = dapp.author
        dapp_dict["dapp_email"] = dapp.dapp_email
        dapp_dict["brief"] = dapp.brief
        dapp_dict["description"] = dapp.description
        dapp_dict["wallet_address"] = dapp.wallet_address
        dapp_dict["license"] = dapp.license
        dapp_dict["status"] = dapp.status
        dapp_dict["social_link1"] = dapp.social_link1
        dapp_dict["social_link2"] = dapp.social_link2
        dapp_dict["pv"] = dapp.pv
        dapp_dict["web_url"] = dapp.web_url
        dapp_dict["dapp_url"] = dapp.dapp_url
        dapp_dict["logo_url"] = dapp.logo_url
        dapp_dict["update_time"] = dapp.update_time.strftime("%Y-%m-%d %H:%M:%S")
        dapp_dict["create_time"] = dapp.create_time.strftime("%Y-%m-%d %H:%M:%S")
        dapp_dict["review"] = dapp.review

        dapp_list.append(dapp_dict)
    return dapp_list
