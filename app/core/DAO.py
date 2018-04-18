#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:

import psycopg2

from app import config

conn = psycopg2.connect(database=config.SQLDB_DSN_MASTER["database"], user=config.SQLDB_DSN_MASTER["user"],
                        password=config.SQLDB_DSN_MASTER["password"], host=config.SQLDB_DSN_MASTER["password"],
                        port=config.SQLDB_DSN_MASTER["port"])


class DAO(object):
    SHARD = False
    SHARD_KEY = 'uid'

    class OP_TYPE(object):
        ADD_OP = 0
        QUERY_OP = 1

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
                filters.append('%s=%%s' % field)
                values.append(value)

        if extra:
            for key, value in extra.iteritems():
                if value is None:
                    filters.append('%s' % key)
                else:
                    filters.append('%s %%s' % key)
                    values.append(value)
        query_sql = 'SELECT %s FROM %s WHERE %s' % (
            fields, table_name, cls.get_filter(filters))  # 数据库查询语句 2018／4／16
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
    def query(cls, master=False, columns=None, fetchone=True, orderby=None,
              extra=None, limit=0, offset=0, groupby=0, shard_key=None, table_name=None, shard_id=None, **kwargs):
        query, values = cls.get_query_sql(columns=columns, extra=extra, orderby=orderby, limit=limit,
                                          offset=offset, groupby=groupby, table_name=table_name, **kwargs)

        if fetchone:
            if master:
                func = 'run_query_fetch_one'
            else:
                func = 'run_query_fetch_one_slave'
        else:
            if master:
                func = 'run_query'
            else:
                func = 'run_query_slave'
        if cls.SHARD and not shard_key:
            shard_key = kwargs.get(cls.SHARD_KEY)
        db = cls.get_database(shard_id=shard_id, shard_key=shard_key, op_type=cls.OP_TYPE.QUERY_OP)

        # logging.debug('sql:%s values:%s' % (query, values))

        if not db:
            return None
        elif isinstance(db, list):
            if fetchone:
                for _db in db:
                    row = getattr(_db, func)(query, values)
                    if row:
                        return row
            else:
                result_array = []
                for _db in db:
                    result_array.extend(getattr(_db, func)(query, values) or [])
                return result_array
        else:
            return getattr(db, func)(query, values)