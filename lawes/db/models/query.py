# -*- coding:utf-8 -*-

from pymongo import MongoClient

class QuerySet(object):

    def __init__(self):
        mongo = MongoClient('xxxxx')# TODO only once
        self.conn_index = 'test' # TODO It's from configurtions

    def _insert(self, objs, fields):
        """ 数据库中插入数据，到这里 Model.save() 才算真正完成
            return _id
        """
        print 'objs:', objs
        print "objs.to_dict()"
        return '_id'
        return collection.insert(objs.to_dict())

    @classmethod
    def get_collection(cls):
        db = cls.conn_index
        db = db.lower()
        db = cls.mongo[db]
        collection_name = cls._get_collection_name()
        collection = getattr(db, collection_name)
        return collection

queryset = QuerySet()