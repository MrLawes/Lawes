The Documentation in http://lawes.readthedocs.io/en/latest/

Simple demo:
Enviroment: pip install lawes
Install the mongodb, and start it: "D:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" --dbpath d:\test
```
from lawes.db import models
conf_dict = {'mongo_uri': 'mongodb://127.0.0.1:27017/', 'db_name': 'testindex'}
models.setup(conf=conf_dict)

class Test(models.Model):

    class Meta:
        db_table = 'test'

    name = models.CharField(default='')
    address = models.CharField(default='11')

test = Test()
test.name = 'lawes'
test.save()

results = Test.objects.filter()
for result in results:
    print(result.name)

```
