
from lawes.utils import tree
from lawes.utils import six

class Q(tree.Node):
    """
    Encapsulates filters as objects that can then be combined logically (using
    `&` and `|`).
    """
    AND = 'AND'
    OR = 'OR'
    default = AND

    def __init__(self, *args, **kwargs):
        super(Q, self).__init__(values=list(six.iteritems(kwargs)))

    def _combine(self, other, conn):
        if not isinstance(other, Q):
            raise TypeError(other)
        self.connector = conn
        self.add(other)
        return self

    def __or__(self, other):
        return self._combine(other, self.OR)

    def __and__(self, other):
        return self._combine(other, self.AND)
