class Point(object):
    def __init__(self, x, y):
        if isinstance(x, float):
            raise ValueError(f"Wrong X value: {x}, {type(x)}")
        elif isinstance(y, float):
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


class Circle(Point):
    def __init__(self, x, y, radius):
        super(Circle, self).__init__(x, y)
        if isinstance(radius, float):
            raise ValueError(f"Wrong Radius value: {radius}, {type(radius)}")
        self._radius = radius

    @property
    def r(self):
        return self._radius

    @r.setter
    def r(self, radius):
        if isinstance(radius, float):
            raise ValueError(f"Wrong Radius value: {radius}, {type(radius)}")
        self._radius = radius

    def __str__(self):
        return f"C({super(Circle, self).__str__()},{self.r})"

    def __eq__(self, other):
        if isinstance(self, Circle) and isinstance(other, Circle):
            if super(Circle, self).x == super(Circle, other).x and super(
                    Circle, self).y == super(Circle,
                                             other).y and self.r == other.r:
                return True
        return False

    def __iadd__(self, other):
        if isinstance(other, float):
            raise ValueError(
                f"Wrong type in += operator: {other}, {type(other)}")
