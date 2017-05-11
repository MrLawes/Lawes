
from django.db.models.query_utils import Q

class Query(object):
    """
    A single SQL query.
    """
    def __init__(self, model):
        self.model = model
        self.q_object = None
        self.order_by_query = ()                    # using for Model.objects.order_by(filter_query)
        self.skip = None                            # using for Model.objects.skip(skip)#
        self.limit = None                           # using for Model.objects.limit(limit)#

    def add_q(self, q_object):
        if self.q_object is None:
            self.q_object = q_object
        else:
            self.q_object = self.q_object & q_object

    def filter_comparsion(self, query):
        """ if found __gt, __gte, __lt, __lte, __ne in query, change to "$gt", "$gte", "$lt", "$lte", "$ne"
        :param query: { 'key' : {$gt : 2000} }
        :return:
        """
        c_query = {}
        match_dict = {
            '__gt': '$gt',
            '__gte': '$gte',
            '__lt': '$lt',
            '__lte': '$lte',
            '__ne': '$ne',
        }
        for qkey in query:
            if '__' in  qkey:
                startwith, endwith = qkey.split('__')
                if '__' + endwith in match_dict:
                    c_query[startwith] = { match_dict['__' + endwith ] :query[qkey]}
            else:
                c_query[qkey] = query[qkey]
        return c_query

    def _as_sql(self, q_object):
        filter_query = {}
        if q_object.q_right is None and q_object.q_left is None:
            if q_object.values:
                filter_query = self.filter_comparsion(dict(q_object.values))
        else:
            filter_query[q_object.connector] = [self._as_sql(q_object.q_left), self._as_sql(q_object.q_right) ]
        return filter_query

    def as_sql(self):
        filter_query = self._as_sql(self.q_object)
        import json
        print('filter_query:', json.dumps(filter_query, indent=4))# TODO delete
        return filter_query

    def execute_sql(self, collection):
        filter_query = self.as_sql()
        multi_data = collection.find(filter_query)
        # order by query
        if self.order_by_query:
            multi_data = multi_data.sort(*self.order_by_query)
        if not self.skip is None:
            multi_data = multi_data.skip(self.skip)
        if not self.limit is None:
            multi_data = multi_data.limit(self.limit)
        return multi_data