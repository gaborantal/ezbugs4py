class SurrealNumber(object):

    def __init__(self, left, right):
        if isinstance(left, set) == False or isinstance(right, set) == False:
            raise TypeError()
        else:
            self._left = left
            self._right = right

    @property
    def left(self):
        return tuple(self._left)

    @property
    def right(self):
        return tuple(self._right)

    def __str__(self):
        array = []
        text = ''

        for i in self._left:
            array.append(str(i))
        array.append('|')
        for i in self._right:
            array.append(str(i))
        text = ','.join(array)

        text = '{' + text + '}'

        return text

    def __le__(self, b):
        if isinstance(self, SurrealNumber) and isinstance(b, SurrealNumber):
            for left in self._left:
                for right in self._right:
                    if left <= right:
                        return True

            for right in self.right:
                for left in self.left:
                    if right <= left:
                        return True

            return True
        else:
            return False

    def __lt__(self, b):
        if isinstance(self, SurrealNumber) and isinstance(b, SurrealNumber):
            if not (b <= self):
                return True
            else:
                return False
        else:
            return False

    def check(self):
        for left in self._left:
            for right in self._right:
                if left >= right:
                    return False

        return True
