.. _fields:

Fields
=====

Creating a model in model.py (Don't change the file's name! The connection is named with file's name and model's name)

.. code-block:: python

    >>> from lawes.db import models
    >>> import datetime
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
    > use testindex
    > db.model_fruit.find()
    > { "_id" : ObjectId("58fecad31d41c839e6db0373"), "num" : 88, "name" : "mongo", "price" : 10.5, "colors" : [  "green",  "yellow" ], "buy_date" : ISODate("2017-04-25T12:04:35.673Z"), "online" : true }


.. _field_options:

Field options
=====

Each field takes a certain set of field-specific arguments. For example, CharField (and its subclasses) require a default argument which specifies the default value used to store the data.
There’s also a set of common arguments available to all field types. All are optional. Here’s a quick summary of the most often-used ones:

default
--------------------------------------
The default value for the field. This can be a value. If callable it will be called every time a new object is created.

db_index
--------------------------------------
If True, a database index will be created for this field.When only call Model.objects.init_index(), the database index does not be created by itself.

unique
--------------------------------------
If True, this field must be unique throughout the table.

This is enforced at the database level and by model validation. If you try to save a model with a duplicate value in a unique field, an Error will be raised by the model’s save() method.

This option is valid on all field types.

Note that when unique is True, you don’t need to specify db_index, because unique implies the creation of an index.

.. _field_type:

Field types
=====

CharField
--------------------------------------
A str field, the default value for this field is ''.

IntegerField
--------------------------------------
A int field, the default value for this field is 0.

FloatField
--------------------------------------
A float field, the default value for this field is 0.0.

DateTimeField
--------------------------------------
A Datetime field, the default value for this field is None.

BooleanField
--------------------------------------
A bool field, the default value for this field is False.

ArrayField
--------------------------------------
A list field, the default value for this field is [].

HStoreField
--------------------------------------
A dict field, the default value for this field is {}.

Automatic primary key fields
--------------------------------------
By default, Lawes gives each model the following field:

_id = str

This is a primary key that comes from mongodb's _id.

.. _meta_options:

Meta options
=====
Give your model metadata by using an inner class Meta, like so:

.. code-block:: python

    >>> class Fruit(models.Model):
    >>>     name = models.CharField(default='mongo')
    >>>     num = models.IntegerField(default=88)
    >>>     price = models.FloatField(default=10.5)
    >>>     buy_date = models.DateTimeField(default=datetime.datetime.now())
    >>>     online = models.BooleanField(default=True)
    >>>     colors = models.ArrayField(default=['green', 'yellow'])
    >>>     class Meta:
    >>>         db_table = 'my_fruit'

Model Meta options
--------------------------------------

db_table
--------------------------------------
The name of the collection in mongodb to use for the model:

Finding the data in MongoDB:

.. code-block:: sh

    $ mongo --port 27017
    > use testindex
     > db.my_fruit.find()


