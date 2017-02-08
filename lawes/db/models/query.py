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

    def _insert(self, obj_class, obj, fields):
        """ 数据库中插入数据，到这里 Model.save() 才算真正完成
            return _id
        """
        collection = self.get_collection(obj_class=obj_class)
        insert_dict = { field: getattr(obj, field) for field in fields if hasattr(obj, field) }
        return collection.insert(insert_dict)

    def _get_collection_name(self, obj_class):
        return obj_class.__module__.split('.')[-1] + '_' + obj_class.__name__.lower()

    @property
    def mongo(self):
        if not self._mongo or not self.conn_index:
            raise CONF_RAESE
        return self._mongo

    def get_collection(self, obj_class):
        db = self.conn_index
        db = db.lower()
        db = self.mongo[db]
        collection_name = self._get_collection_name(obj_class=obj_class)
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