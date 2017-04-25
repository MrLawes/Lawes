.. _overview:

Overview
============

Lawes is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. 
It looks like Django.
This documentation attempts to explain everything you need to know to use PyMongo.

.. _installation:

Installation
============

You can install Lawes either via the Python Package Index (PyPI)
or from source.

To install using `pip`:

.. code-block:: sh

    $ sudo pip install lawes

.. _installing-from-source:

Downloading and installing from source
--------------------------------------

Download the version |version| of Lawes from
https://pypi.python.org/pypi/Lawes

You can install it by doing the following,

.. code-block:: sh

    $ tar xvfz Lawes
    $ cd Lawes
    $ python setup.py install

.. _installing-from-git:

Using the development version
-----------------------------

You can clone the repository by doing the following

.. code-block:: sh

    $ git clone git@github.com:MrLawes/Lawes.git
    $ cd Lawes
    $ python setup.py install

To update:

.. code-block:: sh

    $ cd Lawes
    $ git pull origin master

The supports:
 
 You must start MongoDB Server first, you can visit https://www.mongodb.com/ and get started.
 Testing whether if it is running: 

.. code-block:: sh

    $ mongo
    >MongoDB shell version: 2.4.9
    >connecting to: test



