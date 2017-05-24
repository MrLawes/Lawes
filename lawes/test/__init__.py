
from lawes.db import models
import os
from lawes.conf import ENVIRONMENT_VARIABLE
os.environ.setdefault(ENVIRONMENT_VARIABLE, 'settings')


class Fruit(models.Model):
    class Meta:
        db_table = 'fruit'

    name = models.CharField(default='')
    color = models.CharField(default='')
    sid = models.AutoField()
    nid = models.AutoField(start=1000000000)