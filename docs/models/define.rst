.. _queryset_reference:

Model define reference
=====

to_dict()
--------------------------------------
A helper function to show all of values for key with dictionary.

.. code-block:: python

    >>> from model import Fruit
    >>> fruit = Fruit()
    >>> print(fruit.to_dict())
    >>> {'num': 88, 'name': 'mongo', 'price': 10.5, 'colors': ['green', 'yellow'], 'buy_date': datetime.datetime(2017, 4, 27, 9, 36, 45, 459484), 'online': True}


to_dict_format()
--------------------------------------
A helper function to show all of values for key with 'indent=4' dumped dictionary. The datetime will be string.

.. code-block:: python

    >>> from model import Fruit
    >>> fruit = Fruit()
    >>> print(fruit.to_dict_format())
    >>> {
            "name": "mongo",
            "buy_date": "2017-04-27 09:38:01.919688",
            "colors": [
                "green",
                "yellow"
            ],
            "num": 88,
            "price": 10.5,
            "online": true
         }

