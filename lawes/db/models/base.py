# -*- coding:utf-8 -*-

class ModelBase(object):
    pass

class Model(ModelBase):

    pk_attname = '_id'

    def save(self):
        self.save_base()

    def save_base(self):
        cls = self.__class__
        self._save_table(cls=cls)

    def _save_table(self, cls=None):
        print dir(self)
        pk_val = self._get_pk_val()
        # true: UPDATE; false: INSERT
        pk_set = pk_val is not None
        if pk_set:
            self._do_update()
        else:
            result = self._do_insert()# TODO
            setattr(self, self.pk_attname, result)

    def _get_pk_val(self):
        """ 获得 _id: None: INSERT; not None: UPDATE
        """
        if not hasattr(self, self.pk_attname):
            return None
        else:
            return getattr(self, self.pk_attname)

    def _do_insert(self, manager, using, fields, update_pk, raw):
        """ 向 mongodb 插入数据 TODO
        """
        return manager._insert([self], fields=fields, return_id=update_pk,
                               using=using, raw=raw)