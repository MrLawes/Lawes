# -*- coding:utf-8 -*-

# TODO delete

from lawes.db import models
models.setup(conf={'mongo_uri': 'mongodb://61.155.215.36:27017/test', 'conn_index': 'testindex'})

class Test(models.Model):

    name = models.CharField(default='')
    address = models.CharField(default='')

a = Test()
a.name = 'name1'
a.save()