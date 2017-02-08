# -*- coding:utf-8 -*-

from lawes.db.models.query import queryset
from lawes.db.models.fields import Field

class ModelBase(type):

    def __new__(cls, name, bases, attrs):
        """ 将 Field 转换成对于真实的数据
        """
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        attrs['local_fields'] = {}
        for attr in attrs:
            if hasattr(attrs[attr], 'contribute_to_class'):
                attrs['local_fields'][attr] = attrs[attr]
            if isinstance(attrs[attr], Field):
                attrs[attr] = attrs[attr].value
        return type.__new__(cls, name, bases, attrs)

class Model(object):

    __metaclass__ = ModelBase
    pk_attname = '_id'
    queryset = queryset

    def save(self):
        self._save_table(cls=self.__class__)

    def _save_table(self, cls=None):
        pk_val = self._get_pk_val()
        # true: UPDATE; false: INSERT
        pk_set = pk_val is not None
        if pk_set:
            self._do_update()# TODO
        else:
            result = self._do_insert(obj=self, fields=self.local_fields)
            setattr(self, self.pk_attname, result)

    def _get_pk_val(self):
        """ 获得 _id: None: INSERT; not None: UPDATE
        """
        if not hasattr(self, self.pk_attname):
            return None
        else:
            return getattr(self, self.pk_attname)

    @classmethod
    def _do_insert(cls, obj, fields):
        """ 向 mongodb 插入数据
        """
        return cls.queryset._insert(obj_class=cls, obj=obj, fields=fields)

    @classmethod
    def filter(cls, **query):
        objs = []
        for record in cls.queryset.get_multi(obj_class=cls, **query):
            obj = cls()
            for field in cls.local_fields:
                if field in record:
                    value = record[field]
                else:
                    value = cls.local_fields[field].value
                setattr(obj, field, value)
            obj._id = record['_id']
            objs.append(obj)
        return objs

    @classmethod
    def get(cls, **query):
        obj = cls.filter(**query)
        if len(obj) >= 2:
            raise 'The len > 2!'
        elif len(obj) == 0:
            raise 'The len is 0!'
        return obj[0]