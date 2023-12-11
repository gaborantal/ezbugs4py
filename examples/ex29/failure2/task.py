class HauntedHouse():
    def __init__(self, address, ghosts, _number_of_cats=10):
        self.address = address
        self.ghosts = []
        self._number_of_cats = _number_of_cats

    @property
    def number_of_cats(self):
        return self._number_of_cats

    @number_of_cats.setter
    def number_of_cats(self, value):
        if value > 10:
            self._number_of_cats = value
        else:
            self._number_of_cats = 10

    def __str__(self):
        if (len(self.ghosts) == 0):
            return f"The haunted house at {self.address} has {self._number_of_cats} cats, and {len(self.ghosts)} ghosts haunt it"
        else:
            return f"The haunted house at {self.address} has {self._number_of_cats} cats, and no ghost haunts it"

    def __iadd__(self, other):
        if type(other) != "":
            raise ValueError("Not a ghost")
        else:
            for sor in self.ghosts:
                if other not in self.ghosts:
                    self.ghosts.append(other)

    def __eq__(self, other):
        if isinstance(self, other):
            return False
        else:
            return self._number_of_cats == other._number_of_cats and self.ghosts == other.ghost and self.address == other.address
