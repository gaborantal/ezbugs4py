class SurrealNumber(object):
    def __init__(self, left, right):
        self._left = set([item for item in left if isinstance(item, SurrealNumber)])
        self._right = set([item for item in right if isinstance(item, SurrealNumber)])


    @property
    def left(self):
        return tuple(self._left)

    @property
    def right(self):
        return tuple(self._right)

    def __str__(self):
        return '{' + ','.join(map(str, self._left)) + '|' + ','.join(map(str, self._right)) + '}'

    def __le__(self, other):
        if isinstance(other, SurrealNumber):
            for item in self._left:
                if other <= item:
                    return False
            for item in other._right:
                if item <= self:
                    return False
            return True
        else:
            return None

    def __lt__(self, other):
        return not other <= self

    def check(self):
        for l in self._left:
            for r in self._right:
                if r <= l:
                    return False
        return True
