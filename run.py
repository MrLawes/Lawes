# -*- coding:utf-8 -*-

# TODO delete

from lawes.db import models
from pymongo import MongoClient

models.setup(conf={'mongo_uri': 'mongodb://127.0.0.1:27017/', 'conn_index': 'testindex'})
# "D:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" --dbpath d:\test\mongodb\data

class Test(models.Model):

    name = models.CharField(default='')
    address = models.CharField(default='')

a = Test()
a.name = 'name1'
a.save()

conn = MongoClient('mongodb://127.0.0.1:27017/')
mongo_db = conn['testindex']
for i in mongo_db.run_test.find():
    print i