# -*- coding:utf-8 -*-

from lawes.db.models.lookups import RegisterLookupMixin

class NOT_PROVIDED:
    pass

class Field(RegisterLookupMixin):

    def __init__(self, default=NOT_PROVIDED, ):
        self.default = default

class CharField(Field):

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)