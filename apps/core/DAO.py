#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:
import psycopg2
from apps import config

conn = psycopg2.connect(database=config.SQLDB_DSN_MASTER["database"], user=config.SQLDB_DSN_MASTER["user"],
                        password=config.SQLDB_DSN_MASTER["password"], host=config.SQLDB_DSN_MASTER["host"],
                        port=config.SQLDB_DSN_MASTER["port"])


class DAO(object):
    TABLE = ''

    @classmethod
    def get_filter(cls, conditions):
        return ' AND '.join(conditions) if conditions else ' 1=1 '
    # 数据库查询语句
    @classmethod
    def get_query_sql(cls, columns=None, orderby=None, extra=None, limit=0, offset=0, groupby=None,
                      table_name=None, **kwargs):
        fields = '*'
        if columns:
            fields = ','.join(columns)
        filters = []
        values = []
        if kwargs:
            for field, value in kwargs.iteritems():
                filters.append('%s=%s' % (field, value))
                values.append(value)

        if extra:
            for key, value in extra.iteritems():
                if value is None:
                    filters.append('%s' % key)
                else:
                    filters.append('%s %%s' % key)
                    values.append(value)
        query_sql = 'SELECT %s FROM %s WHERE %s' % (
            fields, table_name or cls.TABLE, cls.get_filter(filters))  # 数据库查询语句 2018／4／16
        if orderby:
            query_sql += ' ORDER BY %s' % orderby
        if limit:
            query_sql += ' LIMIT %s' % limit
        if offset:
            query_sql += ' OFFSET %s' % offset
        if groupby:
            query_sql += ' GROUP BY %s' % groupby
        return query_sql, values

    @classmethod
    def select(cls, columns=None, master=False, fetchone=True, orderby=None, extra=None, limit=0, offset=0, groupby=None, table_name=None, **kwargs):

        query, values = cls.get_query_sql(columns=columns, extra=extra, orderby=orderby, limit=limit,
                                          offset=offset, groupby=groupby, table_name=table_name, **kwargs)

        cur = conn.cursor()

        cur.execute(query)
        rows = cur.fetchall()
        print rows
        '''
        for row in rows:
            print "ID = ", row[0]
            print "NAME = ", row[1]
            print "ADDRESS = ", row[2]
            print "SALARY = ", row[3], "\n"
        '''

        print "Operation done successfully"
        conn.close()


