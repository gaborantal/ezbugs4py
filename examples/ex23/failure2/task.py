class Cemetery:
    def __init__(self, name, number_of_graves=10):
        self.name = name
        if number_of_graves >= 10:
            self._number_of_graves = number_of_graves
        else:
            self._number_of_graves = 10
        self.ghosts = []

    @property
    def number_of_graves(self):
        return self._number_of_graves

    def set_number_of_graves(self, i):
        if i >= 10:
            self._number_of_graves = i
        else:
            self._number_of_graves = 10

    def __str__(self):
        if len(self.ghosts) == 0:
            return "In the " + str(self.name) + " cemetery, there are " + str(
                self.number_of_graves) + " graves, and no ghosts haunt it"

        return "In the " + (str(self.name) + " cemetery, there are " + str(self._number_of_graves) + " graves, and " +
                            str(len(self.ghosts)) + " ghosts haunt it")

    def __iadd__(self, other):
        contains = False
        if isinstance(other, str):
            for i in range(len(self.ghosts)):
                if self.ghosts[i] == other:
                    self.ghosts[i] = str(self.ghosts[i]) + "1"
                    self.ghosts.append(other + "2")
                    contains = True
                return self
            if contains == False:
                self.ghosts.append(other)
            return self
        else:
            raise ValueError("Not a ghost")

    def __eq__(self, other):
        if self.name == other.name and self.number_of_graves == other.number_of_graves:
            return True
        else:
            return False
