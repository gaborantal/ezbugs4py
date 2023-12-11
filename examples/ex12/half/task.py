class SurrealNumber(object):
    def __init__(self, left, right):
        self._left = left
        self._right = right
        if not isinstance(left, set) or not isinstance(right, set):
            raise TypeError

    @property
    def left(self):
        return tuple(self._left)

    @property
    def right(self):
        return tuple(self._right)

    def __str__(self):
        left_side = ""
        return f"{self._left} | {self._right}"

    def __le__(self, b):
        if isinstance(b, SurrealNumber):
            if b <= self._left or b._right >= self:
                return False
            else:
                return True

    def __lt__(self, b):
        if isinstance(b, SurrealNumber):
            if self <= b:
                return True
            else:
                return False
            if self >= b:
                return True

    def check(self):
        pass
