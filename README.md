vim run.py 这里必须该文件,因为下面用到了 mongo_db.run_test.find()
Frist: pip install lawes==1.2.0
```
# -*- coding:utf-8 -*-

from lawes.db import models
from pymongo import MongoClient
# conn_index:每个项目唯一
conf_dict = {'mongo_uri': 'mongodb://127.0.0.1:27017/', 'conn_index': 'testindex'}
# 配置数据库连接方式
models.setup(conf=conf_dict)

# "D:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" --dbpath d:\test

class Test(models.Model):
    name = models.CharField(default='')
    address = models.CharField(default='11')
# 创建一条记录
a = Test()
a.name = 'lawes'
a.save()
# 查找多个记录
a = Test.filter(name='name1')
# 查找一个记录
a = Test.get(name='name1')
a.address = 'address'
a.save()

conn = MongoClient(conf_dict['mongo_uri'])
mongo_db = conn[conf_dict['conn_index']]
for i in mongo_db.run_test.find():
    print i

```
