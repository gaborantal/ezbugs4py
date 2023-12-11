class Cemetery(object):
    def __init__(self, name, _number_of_graves=10):
        self.name = name
        if _number_of_graves >= 10:
            self._number_of_graves = _number_of_graves
        else:
            self._number_of_graves = 10
        self.ghosts = []

    @property
    def number_of_graves(self):
        return self._number_of_graves

    @number_of_graves.setter
    def number_of_graves(self, x):
        if x >= 10:
            self._number_of_graves = x
        else:
            self._number_of_graves = 10

    def __str__(self):
        if len(self.ghosts) == 0:
            return f"In the {self.name} cemetery, there are {self._number_of_graves} graves, and no ghosts haunt it"
        return f"In the {self.name} cemetery, there are {self._number_of_graves} graves, and {len(self.ghosts)} ghosts haunt it"

    def __iadd__(self, other):
        if not isinstance(other, str):
            raise ValueError("Not a ghost")

        if other not in self.ghosts:
            self.ghosts.append(other)
        else:
            for s, i in enumerate(self.ghosts):
                if s == other:
                    self.ghosts[i] = (s + "1")
            self.ghosts.append(other + "2")

        return self

    def __eq__(self, other):
        return self.name == other.name and self._number_of_graves == other.number_of_graves
