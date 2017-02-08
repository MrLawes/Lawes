# -*- coding:utf-8 -*-

from lawes.db.models.query import queryset

class ModelBase(object):

    pk_attname = '_id'
    queryset = queryset

class Model(ModelBase):

    def save(self):
        self.save_base()

    def save_base(self):
        cls = self.__class__
        self._save_table(cls=cls)

    def _save_table(self, cls=None):
        pk_val = self._get_pk_val()
        # true: UPDATE; false: INSERT
        pk_set = pk_val is not None
        if pk_set:
            self._do_update()
        else:
            result = self._do_insert(fields=[])
            setattr(self, self.pk_attname, result)

    def _get_pk_val(self):
        """ 获得 _id: None: INSERT; not None: UPDATE
        """
        if not hasattr(self, self.pk_attname):
            return None
        else:
            return getattr(self, self.pk_attname)

    @classmethod
    def _do_insert(cls, fields):
        """ 向 mongodb 插入数据
        """
        return cls.queryset._insert(objs=cls, fields=fields)