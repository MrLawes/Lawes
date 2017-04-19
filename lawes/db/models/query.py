# -*- coding:utf-8 -*-

from pymongo import MongoClient

CONF_RAESE = """
from lawes.db import models
models.setup(conf={'mongo_uri': 'mongodb://127.0.0.1:27017/test', 'conn_index': 'testindex'})
"""

class ConfigQuerySet(object):


    def __init__(self):
        self.mongo = None
        self.conn_index = ''


    def _setup(self, conf):
        """ 设置mongodb的连接方式
        """
        if self.mongo:
            return
        if self.conn_index:
            return
        if not 'conn_index' in conf:
            raise CONF_RAESE
        if not 'mongo_uri' in conf:
            raise CONF_RAESE
        self.mongo = MongoClient(conf['mongo_uri'])
        self.conn_index = conf['conn_index'].lower()

# init the MongoClient
configqueryset = ConfigQuerySet()


class QuerySet(object):


    def __init__(self, model=None):
        self._model = model
        self._mongo = configqueryset.mongo
        self._db = configqueryset.conn_index        # the name of the db
        self.app_label = model._meta.app_label      # the name of the collection
        if not self._mongo or not self._db:
            raise CONF_RAESE
        self._collection = getattr(self._mongo[self._db], self.app_label)
        self.filter_query = {}                      # using for Model.objects.filter(filter_query)


    def filter(self, **query):
        self.filter_query.update(query)
        return self


    def _fetch_all(self):
        """ run the sql actually
        :return:
        """
        multi_data = self._collection.find(self.filter_query)
        for data in multi_data:
            obj = self._model()
            for field in obj._meta.local_fields:
                if field in data:
                    value = data[field]
                else:
                    value = obj._meta.local_fields[field].value
                setattr(obj, field, value)
            obj._id = data['_id']
            yield obj


    def __iter__(self):
        for data in self._fetch_all():
            yield data


    def _insert(self, obj):
        """
        Inserts a new record for the given model. This provides an interface to
        the InsertQuery class and is how Model.save() is implemented.
        """
        return self._collection.insert(obj.to_dict())


    def _update(self, obj):
        """
        Inserts a new record for the given model. This provides an interface to
        the InsertQuery class and is how Model.save() is implemented.
        """
        update_dict = obj.to_dict(fields='save_fields')
        update_dict.pop('_id')
        return self._collection.update({'_id': obj._id}, {'$set': update_dict}, upsert=True)
    #
    # def to_dict(self, fields=''):
    #     """ fields： save_fields 显示仅修改的部分
    #     """
    #     if fields == 'save_fields':
    #         fields_type = self.save_fields
    #     else:
    #         fields_type = self.local_fields
    #     result = { field: getattr(self, field) for field in fields_type if hasattr(self, field) }
    #     if hasattr(self, '_id'):
    #         result['_id'] = self._id
    #     return result
    #


    #
    # def get_collection(self, obj_class):
    #     # TODO
    #     db = self.conn_index
    #     db = db.lower()
    #     db = self.mongo[db]
    #     collection_name = self._get_collection_name(obj_class=obj_class)
    #     collection = getattr(db, collection_name)
    #     return collection
    #

    #

    #
    # def _get_collection_name(self, obj_class):
    #     # TODO
    #     return obj_class.__module__.split('.')[-1] + '_' + obj_class.__name__.lower()
    #
    # def init_index(self, module_name, class_name, attr, unique=False):
    #     """ create the index_1
    #     """
    #     # TODO
    #     db = self.conn_index
    #     db = db.lower()
    #     db = self.mongo[db]
    #     collection_name = module_name + '_' + class_name.lower()
    #     collection = getattr(db, collection_name)
    #     try:
    #         old_index = collection.index_information()
    #     except:
    #         return
    #     if not attr + '_1' in old_index:
    #         if unique is True:
    #             collection.ensure_index(attr, unique=True)
    #         else:
    #             collection.ensure_index(attr)
    #     elif unique is True:
    #         if not 'unique' in old_index[attr + '_1']:
    #             collection.ensure_index(attr, unique=True)
    #
    # def get_multi(self, obj_class, **query):
    #     """ 获得多个数据
    #     """
    #     # TODO
    #     collection = self.get_collection(obj_class=obj_class)
    #     multi_data = collection.find(query)
    #     return multi_data
