class Film(object):
    def __init__(self, title, length=60):
        self._title = title
        self.length = length
        self.ratings = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        return self

    def add_rating(self, rating):
        if 1.0 < rating < 10.0:
            self.ratings.append(rating)
        else:
            # raise Exception("Invalid rating")
            pass

    def __gt__(self, other):
        if self.length > other.length:
            return True
        return False

    def __str__(self):
        return "{}, {} minutes long film, with {} ratings.".format(self._title, self.length, len(self.ratings))

    def __eq__(self, other):
        if self._title == other._title and self.length == other.length and self.ratings == other.ratings:
            return True
        else:
            return False
