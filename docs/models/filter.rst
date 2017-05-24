.. _filter:

Filter
=====

=
--------------------------------------
Match the value provided for Model

.. code-block:: python

    >>> from lawes.test import Fruit
    >>> fruit = Fruit()
    >>> fruit.name = 'mongo'
    >>> fruit.save()
    >>> for fruit in Fruit.objects.filter(name='mongo'):
    >>>     print(fruit._id,':' ,fruit.name)

SQL equivalent:

.. code-block:: python

    >>> SELECT ... WHERE name='mongo';

gt, gte, lt, lte, ne
--------------------------------------
gt:  Greater than.
gte: Greater than or equal to.
lt:  Less than.
lte: Less than or equal to.
ne:  Not equal to.

.. code-block:: python

    >>> from lawes.test import Fruit
    >>> fruit = Fruit()
    >>> fruit.name = 'mongo'
    >>> fruit.save()
    >>> Fruit.objects.filter(name__gt='mongo')      # SQL equivalent: SELECT ... WHERE name>'mongo';
    >>> Fruit.objects.filter(name__gte='mongo')     # SQL equivalent: SELECT ... WHERE name>='mongo';
    >>> Fruit.objects.filter(name__lt='mongo')      # SQL equivalent: SELECT ... WHERE name<'mongo';
    >>> Fruit.objects.filter(name__lte='mongo')     # SQL equivalent: SELECT ... WHERE name<='mongo';
    >>> Fruit.objects.filter(name__ne='mongo')      # SQL equivalent: SELECT ... WHERE name<>'mongo';
    >>> for fruit in Fruit.objects.filter(name__gt='mongo'):
    >>>     print(fruit._id,':' ,fruit.name)

text__search
--------------------------------------
matches any number of characters

.. code-block:: python

    >>> from lawes.test import Fruit
    >>> fruit = Fruit()
    >>> fruit.name = 'mongo'
    >>> fruit.save()
    >>> Fruit.objects.filter(name_text__search='mongo')      # SQL equivalent: SELECT ... WHERE name like '%m%o%n%g%o%';
    >>> for fruit in Fruit.objects.filter(name_text__search='mongo'):
    >>>     print(fruit._id,':' ,fruit.name)

Q
--------------------------------------
Keyword argument queries – in filter(), etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.

For example, use AND

.. code-block:: python

    >>> from lawes.test import Fruit
    >>> from lawes.db.models import Q
    >>> fruit = Fruit()
    >>> fruit.name = 'mongo'
    >>> fruit.color = 'yellow
    >>> fruit.save()
    >>> query = Q(name='mongo') & Q(color='yellow')
    >>> Fruit.objects.filter(query)                         # SQL equivalent: SELECT ... WHERE name='mongo' and color='yellow';
    >>> query = Q(name='mongo') | Q(color='yellow')
    >>> Fruit.objects.filter(query)                         # SQL equivalent: SELECT ... WHERE name='mongo' or color='yellow';

