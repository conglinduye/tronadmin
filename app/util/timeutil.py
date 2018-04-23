#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from datetime import date, timedelta, datetime
import calendar
import time
from app import config
import traceback

format_str = '%Y-%m-%d %H:%M:%S'

format_str_style_2 = '%Y%m%d%H%M%S'

date_key = 'statistics_date'


# dt is short for datetime

def dt_to_str(dt):
    if not isinstance(dt, (datetime, date)):
        return
    try:
        return dt.strftime(format_str)
    except:
        pass


def dt_to_str_2(dt):
    if not isinstance(dt, (datetime, date)):
        return
    try:
        return dt.strftime(format_str_style_2)
    except:
        pass


def now():
    return dt_to_str(datetime.now())


def str_to_dt(dt_str):
    if not dt_str:
        return
    if isinstance(dt_str, datetime):
        return dt_str
    elif isinstance(dt_str, date):
        return datetime(dt_str.year, dt_str.month, dt_str.day)
    try:
        return datetime.strptime(dt_str, format_str)
    except:
        pass


def str_to_dt_style_2(dt_str):
    if not dt_str:
        return
    if isinstance(dt_str, datetime):
        return dt_str
    elif isinstance(dt_str, date):
        return datetime(dt_str.year, dt_str.month, dt_str.day)
    try:
        return datetime.strptime(dt_str, format_str_style_2)
    except:
        traceback.print_exc()
        pass


def dt_str_to_dt(dt_str):
    if not dt_str:
        return
    try:
        return datetime.strptime(dt_str, '%Y-%m-%d')
    except:
        pass


def dt_diff(dt1, dt2):
    delta = dt2 - dt1
    return delta.seconds


def millisecond_from_begin(dt=None):
    dt = dt or datetime.now()
    begin_dt = str_to_dt(config.PROJECT_BEGIN_TIME)
    delta = dt - begin_dt
    return int(delta.total_seconds() * 1000)


def timestamp_to_dt(timestamp):
    return datetime.fromtimestamp(timestamp)


def timestamp_to_str(timstamp):
    return time.strftime(format_str, time.localtime(timstamp))


def str_to_timestamp(dt_str):
    return time.mktime(datetime.strptime(dt_str, format_str).timetuple())


def dt_to_timestamp(dt):
    return time.mktime(dt.timetuple())


def duration_str(duration, zh=True):
    if zh:
        s = time.strftime('%H时%M分%S秒', time.gmtime(duration))
        s = s.lstrip('00时')
        s = s.lstrip('00分')
    else:
        s = time.strftime('%H:%M:%S', time.gmtime(duration))
        if s.startswith('00:'):
            s = s[3:]

    return s


def yesterday():
    return (date.today() + timedelta(days=-1)).isoformat()


def today():
    return date.today().isoformat()


def weekago():
    return (date.today() + timedelta(days=-7)).isoformat()


def dt_years_ago(years):
    dt = datetime.now()
    if dt.month == 2 and dt.day == 29:
        dt = dt.replace(year=dt.year - years, day=28)
    else:
        dt = dt.replace(year=dt.year - years)
    return dt


def format_from_second(second, f_type='H'):
    if f_type == 'H' or f_type == 'h':
        return '%s小时' % (second / 3600)
    elif f_type == 'M' or f_type == 'm':
        return '%s分钟' % (second / 60)
    elif f_type == 'S' or f_type == 's':
        return '%s秒' % second
    else:
        return None


def timestamp_days_ago(d):
    day = (date.today() + timedelta(days=-d)).isoformat() + ' 06:00:00'
    stamp = time.mktime(datetime.strptime(day, "%Y-%m-%d %H:%M:%S").timetuple())
    return stamp


def get_day(days=0, now_date=None):
    if not now_date:
        now_date = datetime.now()
    now = now_date + timedelta(days=days)
    return int(now.strftime('%Y%m%d'))


def get_day_str(day=0):
    if not day:
        day = get_day()
    return datetime.strptime(str(day), "%Y%m%d").date().isoformat()


def days_ago(day=0):
    _today = date.today()
    return (_today - timedelta(days=day)).isoformat()


def get_day_after(s_date, day=0):
    target_date = datetime.strptime(str(s_date), "%Y%m%d").date() + timedelta(day)
    return int(target_date.strftime('%Y%m%d'))


def first_of_next_month(dt=None):
    """
    下月第一天
    :return:
    """
    if dt is None:
        dt = date.today()
    if dt.month < 12:
        return dt.replace(month=dt.month + 1, day=1)
    else:
        return dt.replace(year=dt.year + 1, month=1, day=1)


def first_of_last_month(dt=None):
    """
    上月第一天
    :return:
    """
    if dt is None:
        dt = date.today()
    if dt.month > 1:
        return dt.replace(month=dt.month - 1, day=1)
    else:
        return dt.replace(year=dt.year - 1, month=12, day=1)


def first_of_month(dt=None):
    """
    本月第一天
    :return:
    """
    if dt is None:
        dt = date.today()
    return dt.replace(day=1)


def last_of_month(dt=None):
    """
    本月最后一天
    :return:
    """
    if dt is None:
        dt = date.today()
    _, day = calendar.monthrange(dt.year, dt.month)
    return dt.replace(day=day)


def last_of_last_week():
    """
    上周最后一天
    :return:
    """
    dt = last_of_week()
    return date_add(dt, -7)


def last_week():
    """
    上周当天
    :return:
    """
    dt = date.today()
    return date_add(dt, -7)


def first_of_last_week():
    """
    上周第一天
    :return:
    """
    dt = first_of_week()
    return date_add(dt, -7)


def last_of_week(dt=None):
    """
    本周最后一天
    """
    if dt is None:
        dt = date.today()
    return date_add(dt, 6 - dt.weekday())


def date_add(dt, days):
    """
    加天数
    :param dt:
    :param days:
    :return:
    """
    return dt + timedelta(days=days)


def first_of_week(dt=None):
    """
    本周第一天
    :return:
    """
    if dt is None:
        dt = date.today()
    return date_add(dt, -dt.weekday())
