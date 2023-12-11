class HauntedHouse:

    def __init__(self, address, number_of_cats=10):
        self.address = address
        self._number_of_cats = number_of_cats if number_of_cats > 10 else 10
        self.ghosts = list()

    @property
    def number_of_cats(self):
        return self._number_of_cats

    @number_of_cats.setter
    def number_of_cats(self, x):
        self._number_of_cats = x if x > 10 else 10

    def __str__(self):
        if len(self.ghosts) > 0:
            return "The haunted house at " + self.address + " has " + str(self.number_of_cats) + " cats, and " + str(
                len(self.ghosts)) + " ghosts haunt it"
        return "The haunted house at " + self.address + " has " + str(
            self.number_of_cats) + " cats, and no ghost haunts it"

    def __iadd__(self, ghost_name):
        if not isinstance(ghost_name, str()):
            raise ValueError("Not a ghost")
        if ghost_name not in self.ghosts:
            self.ghosts.append(ghost_name)
        else:
            for i in range(len(self.ghosts)):
                if self.ghosts[i] == ghost_name:
                    self.ghosts[i] = ghost_name + "1"
            self.ghosts.append(ghost_name + "2")
        return self

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.number_of_cats == other.number_of_cats and self.address == other.address
