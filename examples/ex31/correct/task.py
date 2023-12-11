class Basket:

    def __init__(self, material, size=10):
        self.material = material
        self._size = size
        self.candies = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, m):
        self._size = m
        if len(self.candies) > m:
            self.candies = self.candies[:m]

    def __str__(self):
        return f"The {self.material} basket size is {self.size}, currently there are {len(self.candies)} candies in it"

    def add_candy(self, candy):
        if len(self.candies) == self.size:
            raise ValueError("The basket is full")

        if candy not in self.candies:
            self.candies.append(candy)
        else:
            raise ValueError("This candy is already in the basket")

    def __add__(self, other):
        k = Basket("mixed material", self.size + other.size)
        k.candies = self.candies + other.candies
        return k

    def __eq__(self, other):
        return self.material == other.material and self.size == other.size
