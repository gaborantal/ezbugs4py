class Film:
    def __init__(self, title, length=60):
        self._title = title
        self.length = length
        self.ratings = []

    def title(self, title):
        if isinstance(title, str):
            self._title = title

    def title(self):
        return self._title

    def add_rating(self, rating):
        if 1.0 <= rating <= 10.0:
            self.ratings.append(rating)
        else:
            raise Exception("Invalid rating")

    def __gt__(self, other):
        if isinstance(other, Film):
            return self.length > other.length
        return None

    def __str__(self):
        return f"{self.title()}, {self.length} minutes long film, with {len(self.ratings)} ratings."

    def __eq__(self, other):
        if isinstance(other, Film):
            if self.length == other.length and self.ratings == other.ratings and self.title() == other.title():
                return True
        return False
