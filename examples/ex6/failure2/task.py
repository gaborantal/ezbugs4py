class Hypercube:
    def __init__(self, dimension, length):
        if dimension < 0 or length < 0:
            raise Exception("Wrong Hypercube!")
        self._dimension = dimension
        self._length = length

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        if value < 0:
            raise Exception("Wrong Hypercube!")
        self._dimension = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 0:
            raise Exception("Wrong Hypercube!")
        self._length = value

    def get_no_vertex(self):
        if self.dimension == -1:
            return 0
        return 2 ** self.dimension

    def get_no_edge(self):
        if self.dimension == -1:
            return 0
        return self.dimension * (2 ** (self.dimension - 1))

    def factorial(self, num):
        if num < 0:
            return -1
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial

    def fact(self, n):
        return 1 if n == 1 else (n * self.fact(n - 1))

    def get_no_face(self):
        if self.dimension < 0 or self.length < 0:
            return 0
        return float((2 ** (self.dimension - 2)) * (self.factorial(self.dimension) / (2.0 * self.factorial(self.dimension - 2))))

    def get_area(self):
        if self.dimension < 0 or self.length < 0:
            return 0
        return self.dimension * self.length

    def __eq__(self, other):
        if isinstance(other, Hypercube):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return f"Dim: {self.dimension}, Len: {self.length}, Area: {self.get_area()}"
