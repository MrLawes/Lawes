# -*- coding:utf-8 -*-

from pymongo import MongoClient

CONF_RAESE = """
from lawes.db import models
models.setup(conf={'mongo_uri': 'mongodb://127.0.0.1:27017/test', 'conn_index': 'testindex'})
"""

class QuerySet(object):

    def __init__(self):
        self._mongo = None
        self.conn_index = ''

    def _insert(self, objs, fields):
        """ 数据库中插入数据，到这里 Model.save() 才算真正完成
            return _id
        """
        collection = self.get_collection(objs=objs)
        # TODO dict
        insert_dict = {
            'name': 'name1',
            'address': 'address2',
        }
        return collection.insert(insert_dict)

    def _get_collection_name(self, objs):
        return objs.__module__.split('.')[-1] + '_' + objs.__name__.lower()

    @property
    def mongo(self):
        if not self._mongo or not self.conn_index:
            raise CONF_RAESE
        return self._mongo

    def get_collection(self, objs):
        db = self.conn_index
        db = db.lower()
        db = self.mongo[db]
        collection_name = self._get_collection_name(objs=objs)
        collection = getattr(db, collection_name)
        return collection

    def _setup(self, conf):
        """ 设置mongodb的连接方式
        """
        if self._mongo:
            return
        if self.conn_index:
            return
        if not 'conn_index' in conf:
            raise CONF_RAESE
        if not 'mongo_uri' in conf:
            raise CONF_RAESE
        self._mongo = MongoClient(conf['mongo_uri'])
        self.conn_index = conf['conn_index']

queryset = QuerySet()