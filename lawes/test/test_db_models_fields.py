
import unittest
from lawes.test import Fruit

class TestBdModelsFields(unittest.TestCase):

    def setUp(self):
        self.clearall()

    def tearDown(self):
        self.clearall()

    def clearall(self):
        for test_obj in Fruit.objects.filter():
            test_obj.delete()
        Fruit().clean_auto_field()

    def test_autofield(self):
        fruit = Fruit()
        fruit.save()
        self.assertEqual(fruit.nid, 1000000001)
        fruit.save()
        self.assertEqual(fruit.sid, 1)

    # TODO all of them

