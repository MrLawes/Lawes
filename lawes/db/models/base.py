# -*- coding:utf-8 -*-

from lawes.db.models.query import QuerySet
from lawes.utils import six
from lawes.db.models.options import Options

class ModelBase(type):

    def __new__(cls, name, bases, attrs):
        """  changed Field to true type
        """
        super_new = super(ModelBase, cls).__new__
        # if it is not the ModelBase , return
        parents = [b for b in bases if isinstance(b, ModelBase)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        # Create the class.
        # new_class = super_new(cls, name, bases, attrs)
        module = attrs.pop('__module__')
        new_class = super_new(cls, name, bases, {'__module__': module})
        meta = attrs.pop('Meta', None)
        if not meta:
            meta = getattr(new_class, 'Meta', None)
        # app_label is the collection name in mongodb
        app_label = new_class.__module__.split('.')[-1] + '_' + new_class.__name__.lower()
        kwargs = {"app_label": app_label}
        new_class._meta = Options(meta, **kwargs)

        # set the local_fields at Options: {'name': lawes.db.models.fields.CharField}
        for obj_name, obj in attrs.items():
            if hasattr(obj, 'contribute_to_class'):
                new_class._meta.add_field(obj_name=obj_name, obj=obj)

        # auto to create index, TODO rewrite it to other placese, does use it many more
        # attrs['local_fields'] = {}
        # new_class.local_fields = {}
        # for attr in attrs:
        #     if hasattr(attrs[attr], 'contribute_to_class'):
        #         new_class.local_fields[attr] = attrs[attr]
        #     if isinstance(attrs[attr], Field):
        #         if attrs[attr].db_index is True:
        #             queryset.init_index(module_name=attrs['__module__'], class_name=name, attr=attr, unique=attrs[attr].unique)
        #         # attrs[attr] = attrs[attr].value
        #         setattr(new_class, attr, attrs[attr].value)

        # create the objects
        new_class.objects = QuerySet(model=new_class)

        return new_class


class Model(six.with_metaclass(ModelBase)):

    pk_attname = '_id'
    save_fields = []


    def __init__(self, *args, **kwargs):
        # set the real value to the model
        for obj_name in self._meta.local_fields:
            obj = self._meta.local_fields[obj_name]
            setattr(self, obj_name, obj.value)
        super(Model, self).__init__()


    def __setattr__(self, key, value):
        super(Model, self).__setattr__(key, value)
        # if key in self._meta.local_fields:
        #     self._meta.local_fields[key].check_type(value=value)
        if hasattr(self, '_id'):
            self.save_fields.append(key)


    def check_type(self, result):
        for field in self._meta.local_fields:
            self._meta.local_fields[field].check_type()


    def save(self):
        self._save_table()


    def _save_table(self):
        pk_val = self._get_pk_val()
        # true: UPDATE; false: INSERT
        pk_set = pk_val is not None
        if pk_set:
            self._do_update(obj=self)
        else:
            result = self._do_insert(obj=self)
            setattr(self, self.pk_attname, result)


    def _get_pk_val(self):
        """ get _id: None: INSERT; not None: UPDATE
        """
        # TODO
        if not hasattr(self, self.pk_attname):
            return None
        else:
            return getattr(self, self.pk_attname)


    @classmethod
    def _do_insert(cls, obj):
        """ 向 mongodb 插入数据
        """
        return cls.objects._insert(obj=obj)


    @classmethod
    def _do_update(cls, obj):
        """ doing update in mongodb
        """
        return cls.objects._update(obj=obj)

    # @classmethod
    # def filter(cls, **query):
    #     objs = []
    #     for record in cls.queryset.get_multi(obj_class=cls, **query):
    #         obj = cls()
    #         for field in cls.local_fields:
    #             if field in record:
    #                 value = record[field]
    #             else:
    #                 value = cls.local_fields[field].value
    #             setattr(obj, field, value)
    #         obj._id = record['_id']
    #         objs.append(obj)
    #     return objs


    @classmethod
    def get(cls, **query):
        # TODO
        obj = cls.filter(**query)
        if len(obj) >= 2:
            raise 'The len > 2!'
        elif len(obj) == 0:
            raise 'The len is 0!'
        return obj[0]


    def to_dict(self, fields=''):
        """ fields： save_fields 显示仅修改的部分
        """
        # TODO check_type
        if fields == 'save_fields':
            fields_type = self.save_fields
        else:
            fields_type = self._meta.local_fields
        result = {}

        for field in fields_type:
            if hasattr(self, field):
                value = getattr(self, field)
                # fields_type[field].check_type(value=value)# TODO here
                result[field] = value

        if hasattr(self, '_id'):
            result['_id'] = self._id

        return result