#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: lmr


class DAO(object):
    __tablename__ = ''

    @classmethod
    def query(cls, **kwargs):
        filters = []
        if kwargs:
            for field, value in kwargs.iteritems():
                filters.append('%s=%s' % (field, value))

