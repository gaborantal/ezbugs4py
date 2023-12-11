class Hypercube:
    def __init__(self, dimension, length):
        self._dimension = dimension
        self._length = length

        if dimension < 0 or length < 0:
            raise Exception("Wrong Hypercube!")

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        if dimension < 0:
            raise Exception("Wrong Hypercube!")
        self._dimension = dimension

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length < 0:
            raise Exception("Wrong Hypercube!")
        self._length = length

    def get_no_vertex(self):
        return 2 ** self._dimension

    def get_no_edge(self):
        if self._dimension < 1:
            return 0
        return self._dimension * 2 ** (self._dimension - 1)

    def get_no_face(self):
        def factorial(n):
            s = 1
            for i in range(1, n + 1):
                s *= i
            return s

        if self._dimension < 2:
            return 0

        return 2 ** (self._dimension - 2) * factorial(self._dimension) / (2 * factorial(self._dimension - 2))

    def get_area(self):
        return self._length ** self._dimension

    def __str__(self):
        return f"Dim: {self._dimension}, Len: {self._length}, Area: {self.get_area()}"

    def __eq__(self, other):
        if not isinstance(other, Hypercube):
            return False
        return self._dimension == other._dimension and self._length == other._length
