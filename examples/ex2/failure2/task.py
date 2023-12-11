class Triangle(object):
    a_value = list()

    def __init__(self, a, b=None, c=None):
        self._a = a
        if b is None:
            self._b = self._a
        if c is None:
            self._c = self._a
        self.a_value.append(a)
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, uj):
        if isinstance(uj, int):
            self._a = uj
            self.a_value.append(uj)
        else:
            raise Exception("Invalid value")

    def area(self):
        area = 0
        s = 0
        s = (self.a + self._b + self._c) / 2
        area = ((s * (s - self.a)(s - self._b)(s - self._c)) ** (1 / 2))
        return area

    def perimeter(self):
        k = 0
        k = self.a + self._b + self._c
        return k

    def __eq__(self, other):
        if (self.perimeter() == other.perimeter()) and (self.area() == other.area()):
            return True
        else:
            return False

    def __str__(self):
        changes_of_a_values = len(self.a_value)
        return f"The changes in the a values, {changes_of_a_values}"
