# -*- coding:utf-8 -*-

from lawes.db.models.lookups import RegisterLookupMixin
import datetime
from lawes.core.exceptions import ValidationError
from lawes.core.exceptions import DefaultError
from lawes.conf import settings

class CheckTypeNone(object):
    pass

class Field(RegisterLookupMixin):
    """ 用于标识是否需要转换和存储的字段
    """
    contribute_to_class = None
    error_message = "{value} value has an invalid format. It must be in {value_type} format."
    # 可以不用设置 default, 获得设置成空
    default_can_set_null = False

    def __init__(self, default=None, db_index=False, unique=False):
        if not hasattr(self, 'default') and default is None:
            raise DefaultError('This Field needs default')
        if not default is None:
            self.default = default
        # self.value = default
        self.db_index = db_index
        self.unique = unique

    @property
    def value(self):
        if callable(self.default):
            default = self.default()
        else:
            default = self.default
        return default

    def check_type(self, value=CheckTypeNone()):
        """ 检测子类的类型是否正确
        """
        check_value = value if not isinstance(value, CheckTypeNone) else self.value
        if self.default_can_set_null is True and check_value is None:
            return True
        if not isinstance(check_value, self.field_type):
            raise ValidationError(message=self.error_message,params={'value': check_value, 'value_type': str(self.field_type)},)
        return True

class CharField(Field):

    field_type = str
    default = ''

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)

class IntegerField(Field):

    field_type = int
    default = 0

    def __init__(self, *args, **kwargs):
        super(IntegerField, self).__init__(*args, **kwargs)

class FloatField(Field):

    field_type = float
    default = 0.0

    def __init__(self, *args, **kwargs):
        super(FloatField, self).__init__(*args, **kwargs)

class DateTimeField(Field):

    field_type = datetime.datetime
    default_can_set_null = True
    default = None

    def __init__(self, *args, **kwargs):
        super(DateTimeField, self).__init__(*args, **kwargs)

class BooleanField(Field):

    field_type = bool
    default = False

    def __init__(self, *args, **kwargs):
        super(BooleanField, self).__init__(*args, **kwargs)


class ArrayField(Field):

    field_type = list
    default = []

    def __init__(self, *args, **kwargs):
        super(ArrayField, self).__init__(*args, **kwargs)


class HStoreField(Field):

    field_type = dict
    default = {}

    def __init__(self, *args, **kwargs):
        super(HStoreField, self).__init__(*args, **kwargs)


class AutoField(Field):

    field_type = int
    default_can_set_null = True
    default = None
    start = None

    def __init__(self, *args, **kwargs):
        if 'start' in kwargs:
            self.start = kwargs.pop('start')
        super(AutoField, self).__init__(*args, **kwargs)

class FileField(Field):

    field_type = str
    default = ''
    upload_to = ''

    def __init__(self, *args, **kwargs):
        if 'upload_to' in kwargs:
           self.upload_to = kwargs.pop('upload_to')
        super(FileField, self).__init__(*args, **kwargs)

    @property
    def value(self):
        if callable(self.default):
            default = self.default()
        else:
            default = self.default
        return default

    def get_upload_to(self):
        """
        >>> obj = FileField(upload_to='/var/www/example.com/media/')
        >>> obj.get_upload_to()
        '/var/www/example.com/media/'
        >>> obj = FileField(upload_to='mydir/')
        >>> obj.get_upload_to()
        'static/uploads/mydir/'
        >>> obj = FileField(upload_to='mydir')
        >>> obj.get_upload_to()
        'static/uploads/mydir/'
        >>> from lawes.conf import settings
        >>> settings.MEDIA_ROOT = 'mystatic/'
        >>> obj = FileField(upload_to='mydir')
        >>> obj.get_upload_to()
        'mystatic/mydir/'
        """
        if self.upload_to.startswith('/'):
            return self.upload_to
        upload_to = settings.MEDIA_ROOT
        if not upload_to.endswith('/'):
            upload_to += '/'
        if self.upload_to:
            upload_to += self.upload_to
        if not upload_to.endswith('/'):
            upload_to += '/'
        return upload_to