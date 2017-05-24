Usage
=====

Creating a model in model.py (Don't change the file's name! The connection is named with file's name and model's name)

.. code-block:: python

    >>> from lawes.db import models
    >>> class Test(models.Model):
    >>>     name = models.CharField(default='')

Creating a connection in test.py: 

.. code-block:: python

    >>> from lawes.db import models
    >>> conf_dict = {'MONGO_URI': 'mongodb://127.0.0.1:27017/', 'DB_NAME': 'testindex'}
    >>> models.setup(conf=conf_dict)
    >>> from model import Test
    >>> if __name__ == '__main__':
    >>>     obj = Test()
    >>>     obj.name = 'yourname'
    >>>     obj.save()

Also you can use environ for creating a connection

.. code-block:: python

    >>> from lawes.db import models
    >>> import os
    >>> os.environ["LAWES_SETTINGS_MODULE"] = "lawes.conf.global_settings"
    >>> from model import Test
    >>> if __name__ == '__main__':
    >>>     obj = Test()
    >>>     obj.name = 'yourname'
    >>>     obj.save()

Finding the data in MongoDB:
    
.. code-block:: sh

    $ mongo --port 27017
    $ use testindex
    $ db.model_test.find()
    > { "_id" : ObjectId("58fec1221d41c83634580d87"), "name" : "yourname", }

