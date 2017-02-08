# -*- coding:utf-8 -*-

from lawes.db.models.lookups import RegisterLookupMixin

class NOT_PROVIDED:
    pass

class Field(RegisterLookupMixin):
    # 用于标识是否需要转换和存储的字段
    contribute_to_class = None

    def __init__(self, default=NOT_PROVIDED, ):
        self.default = default
        self.value = default

class CharField(Field):

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)
        if not isinstance(self.default, str):
            raise "CharField default error"
        self.value = self.default
