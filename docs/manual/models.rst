.. _fields:

Fields
=====

Creating a model in model.py (Don't change the file's name! The connection is named with file's name and model's name)

.. code-block:: python

    >>> class Fruit(models.Model):
    >>>     name = models.CharField(default='mongo')
    >>>     num = models.IntegerField(default=88)
    >>>     price = models.FloatField(default=10.5)
    >>>     buy_date = models.DateTimeField(default=datetime.datetime.now())
    >>>     online = models.BooleanField(default=True)
    >>>     colors = models.ArrayField(default=['green', 'yellow'])

Creating a connection in test.py and running it with 'python test.py': 

.. code-block:: python

    >>> from lawes.db import models
    >>> conf_dict = {'mongo_uri': 'mongodb://127.0.0.1:27017/', 'db_name': 'testindex'}
    >>> models.setup(conf=conf_dict)
    >>> from model import Fruit
    >>> if __name__ == '__main__':
    >>>     obj = Fruit()
    >>>     obj.save()

Finding the data in MongoDB:
    
.. code-block:: sh

    $ mongo --port 27017
    $ use testindex
    $ db.model_fruit.find()
    > { "_id" : ObjectId("58fecad31d41c839e6db0373"), "num" : 88, "name" : "mongo", "price" : 10.5, "colors" : [  "green",  "yellow" ], "buy_date" : ISODate("2017-04-25T12:04:35.673Z"), "online" : true }


