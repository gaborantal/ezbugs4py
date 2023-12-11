class Point(object):
    def __init__(self, x, y):
        if not isinstance(x, float):
            raise ValueError(f"Wrong X value: {x}, {type(x)}")
        elif not isinstance(y, float):
            raise ValueError(f"Wrong Y value: {y}, {type(y)}")
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"P({self.x},{self.y})"

    def __eq__(self, other):
        if isinstance(self, Point) and isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
        return False
