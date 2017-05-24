.. _filter:

filter()
--------------------------------------
Returns a new QuerySet containing objects that match the given lookup parameters.Also you can find the _id in mongodb.

The lookup parameters (**kwargs) should be in the format described in Field lookups below. Multiple parameters are joined via AND in the underlying SQL statement.
The paramaters can with extra '__' like: __gt,__gte,__lt,__lte,__ne. They will find with comparsion: 'g' meas 'greater'; 't' means 'than'; e means 'equality'; 'n' means 'not';
query = {"1__gt": 1,"2__gte": 2,"3__lt": 3,"4__lte": 4,"5__ne": 5, '6': 6, '7_text__search': '77d' }
the query will change to {'1': {'$gt': 1}, '2': {'$gte': 2}, '3': {'$lt': 3}, '4': {'$lte': 4}, '5': {'$ne': 5}, '6': 6, '7': {'$regex': '7.*7.*d', '$options': 'si'}}

.. code-block:: python

    >>> from models import Fruit
    >>> fruits = Fruit.objects.filter(name='mongo')
    >>> for fruit in fruits:
    >>>     print fruit.name
    >>> fruits = Fruit.objects.filter(name__gt='mongo')
    >>> fruits = Fruit.objects.filter(_id='58f71dafd97f0e1b886b0d1c')
    >>> fruits = Fruit.objects.filter(name_text__search='ox')

