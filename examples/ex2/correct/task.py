class Triangle:
    def __init__(self, a, b=False, c=False):
        self._a = a
        if not b:
            self.b = a
        else:
            self.b = b
        if not c:
            self.c = a
        else:
            self.c = c
        self.a_values = []
        self.a_values.append(a)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, values):
        if isinstance(values, int):
            self.a_values.append(values)
            self._a = values
        else:
            raise Exception("Invalid value")

    def area(self):
        s = (self._a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self._a + self.b + self.c

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return self.area() == other.area() and self.perimeter() == other.perimeter()

    def __str__(self):
        return f"The changes in the a values, {len(self.a_values)}"
