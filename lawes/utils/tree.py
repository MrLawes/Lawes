
import copy

class Node(object):

    default = 'DEFAULT'

    def __init__(self, children=None, connector=None, negated=False, values=[]):
        self.children = children[:] if children else []         # [<Q: (AND: ('phone', '1'), ('name', 'lawes'))>]
        self.connector = connector or self.default               # AND
        self.negated = negated
        self.values = values[:] if values else []               # [('phone', '1'), ('name', 'lawes')]

    def __str__(self):
        return '<%s: %s, %s>' % (self.connector, self.values, ', '.join(str(c) for c in
                self.children))

    def add(self, other):
        if other in self.children:
            return other
        if other.connector == self.connector:
            self.values.extend(other.values)
        else:
            self.children.append(other)