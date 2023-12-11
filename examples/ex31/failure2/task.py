class Basket:
    def __init__(self, material, _size=10):
        self.material = material
        self._size = _size
        self.candies = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, other):
        self._size = other
        if len(self.candies) > self._size:
            pass

    def __str__(self):
        return "The " + self.material + " basket size is " + str(self._size) + ", currently there are " + str(
            len(self.candies)) + " candies in it"

    def add_candy(self, candy):
        if len(self.candies) >= self._size:
            raise ValueError("The basket is full")
        for i in self.candies:
            if i == candy:
                raise ValueError("This candy is already in the basket")
            else:
                self.candies.append(candy)
        return self

    def __add__(self, basket):
        if isinstance(basket, Basket):
            basket.material = "mixed material"
            basket._size = self._size + basket._size
            basket.candies.append(self.candies)
        return basket

    def __eq__(self, other):
        return isinstance(other, Basket) and other.material == self.material and other._size == self._size
