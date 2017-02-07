# -*- coding:utf-8 -*-

# TODO delete

from lawes.db import models

class Test(models.Model):

    name = models.CharField(default='')

a = Test()
a.name = 'name1'
a.save()