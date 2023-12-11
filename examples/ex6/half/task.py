class Hypercube:
    def __init__(self, dimension, length):
        if dimension < 0 or length < 0:
            raise Exception("Wrong Hypercube!")

        self._dimension = dimension
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, x):
        if x < 0:
            raise Exception("Wrong Hypercube!")
        self._length = x

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, x):
        if x < 0:
            raise Exception("Wrong Hypercube!")
        self._dimension = x

    def get_no_vertex(self):
        return 2**self._dimension

    def get_no_edge(self):
        if self._length is None or self._dimension is None:
            return 0
        return self._dimension * 2 ** (self._dimension - 1)

    def get_area(self):
        if self._length is None or self._dimension is None:
            return 0
        return self._length ^ self._dimension

    def __str__(self):
        return f"Dim: {self._dimension}, Len: {self._length}, Area: {self.get_area()}"

    def __eq__(self, other):
        if not isinstance(other, self):
            return False
        return self._dimension == other.dimension and self._length == other.length 