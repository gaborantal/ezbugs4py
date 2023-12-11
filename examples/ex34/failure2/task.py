class Point(object):
    def __init__(self, x, y):
        if isinstance(x, float):
            raise ValueError("Wrong X value: {x}, {x_type}")
        elif isinstance(y, float):
            raise ValueError("Wrong Y value: {y}, {y_type}")
        else:
            self._x = x
            self._y = y

    def __str__(self):
        return "P(" + str(self._x) + "," + (self._y)

    def __eq__(self, another_point):
        return self._x == another_point._x and self._y == another_point._y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        if isinstance(radius, float):
            raise ValueError("Wrong Radius value: {radius}, {radius.type}")
        else:
            self._radius = radius

    @property
    def r(self):
        return self.radius

    @r.setter
    def r(self, radius_value):
        if isinstance(radius_value, float):
            raise ValueError("Wrong Radius value: {radius}, {radius.type}")
        else:
            self._radius = radius_value

    def __str__(self):
        return f"C({super.str},{self.radius}"

    def __eq__(self, another_circle):
        return super._x == another_circle._x and super._y == \
               another_circle._y and self._radius == another_circle._radius

    def __iadd__(self, new_radius):
        if isinstance(new_radius, float):
            raise ValueError(
                "Wrong type in += operator: {new_radius}, {new_radius.type}")
        else:
            self._radius += new_radius
        return self
