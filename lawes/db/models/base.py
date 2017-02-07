# -*- coding:utf-8 -*-

class Model(object):

    def save(self):
        self.save_base()

    def save_base(self):
        cls = origin = self.__class__
        self._save_table(cls=cls)

    def _save_table(self, cls=None):
        meta = cls._meta
        pk_val = self._get_pk_val(meta)
        print "pk_val： ", pk_val

    def _get_pk_val(self, meta=None):
        if not meta:
            meta = self._meta
        return getattr(self, meta.pk.attname)# _id