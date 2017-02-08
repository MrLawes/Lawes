* # -*- coding:utf-8 -*-
* from lawes.db import models
* from pymongo import MongoClient
* # conn_index:每个项目唯一
* conf_dict = {'mongo_uri': 'mongodb://127.0.0.1:27017/', 'conn_index': 'testindex'}
* models.setup(conf=conf_dict)
* # "D:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" --dbpath d:\test\mongodb\data
* class Test(models.Model):
*     name = models.CharField(default='')
*     address = models.CharField(default='11')
* a = Test()
* a.name = 'lawes'
* a.save()
* conn = MongoClient(conf_dict['mongo_uri'])
* mongo_db = conn[conf_dict['conn_index']]
* for i in mongo_db.run_test.find():
*     print i
