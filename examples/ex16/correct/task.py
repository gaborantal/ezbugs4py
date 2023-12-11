class Film(object):

    def __init__(self, title, length=60):
        self._title = title
        self.length = length
        self.ratings = list()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, titlev):
        if isinstance(titlev, str):
            self._title = titlev

    def add_rating(self, rating):
        if isinstance(rating, float) and 1.0 <= rating <= 10.0:
            self.ratings.append(rating)
        else:
            raise Exception("Invalid rating")

    def __gt__(self, other):
        if isinstance(other, Film):
            return self.length > other.length
        else:
            return False

    def __str__(self):
        return f"{self.title}, {self.length} minutes long film, with {len(self.ratings)} ratings."

    def __eq__(self, other):
        if isinstance(other, Film):
            return self.__dict__ == other.__dict__
        else:
            return False
