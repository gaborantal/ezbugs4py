class Triangle(object):
    a_values = []

    def __init__(self, a, b=None, c=None):
        self._a = a
        if b is None:
            self.b = a
        else:
            self.b = b
        if c is None:
            self.c = a
        else:
            self.c = c

        self.a_values.append(a)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, newA):
        if newA % 2 != 0:
            raise Exception("Invalid value")
        else:
            self._a = newA
            self.a_values.append(newA)

    def area(self):
        s = (self._a + self.b + self.c)
        T = (s * (s - self._a) * (s - self.b) * (s - self.c)) ^ (1 / 2)
        return T

    def perimeter(self):
        return self._a + self.b + self.c

    def __eq__(self, other):
        return (self.area() == other.terulet() and self.perimeter() == other.keruket())

    def __str__(self):
        return "The changes in the a values, " + str(len(a.a_values))
