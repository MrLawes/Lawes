
import unittest
from lawes.db import models

conf_dict = {'mongo_uri': 'mongodb://127.0.0.1:27017/', 'db_name': 'testindex'}
models.setup(conf=conf_dict)

class Test(models.Model):
    class Meta:
        db_table = 'test'

    name = models.CharField(default='')
    address = models.CharField(default='')

class TestBdModels(unittest.TestCase):

    def setUp(self):
        self.clearall()

    def tearDown(self):
        self.clearall()

    def test_delete(self):
        self.clearall()
        for test_obj in Test.objects.filter():
            self.fail('delete does not work!')

    def clearall(self):
        for test_obj in Test.objects.filter():
            test_obj.delete()

    # TODO all of them

