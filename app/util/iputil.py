# *-* coding:utf-8 *-*
# date:2018/04/19
import logging
import traceback

__author__ = "lmr"



def get_http_real_ip(request):
    try:
        http_header = request.requestHeaders
        real_ip_list = http_header.getRawHeaders(u'x-forwarded-for')
        if real_ip_list and len(real_ip_list) >= 1:
            return real_ip_list[0].split(',')[0]
        else:
            return ''
    except:
        logging.error(traceback.format_exc())
        return ''