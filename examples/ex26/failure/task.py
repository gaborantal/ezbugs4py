class Mathematician:
    def __init__(self, _name, favorite_length=3):
        self._name = _name
        self.favorite_length = favorite_length
        self.studies = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    def add_study(self, numbers):
        favorite_counter = 0
        first_length = len(str(numbers[0]))
        same = True
        for num in numbers:
            if len(str(num)) == self.favorite_length:
                favorite_counter = 1
            if len(str(num)) != first_length:
                same = False
        if favorite_counter == len(numbers) and same and first_length == self.favorite_length:
            self.studies[self.favorite_length] = numbers
            return
        if same and first_length != self.favorite_length:
            self.favorite_length = first_length
            return
        raise ValueError("Ugly numbers")

    def __lt__(self, mathematician) -> bool:
        if self.favorite_length < mathematician.favorite_length:
            return True
        return False

    def __str__(self):
        return f"The mathematician named {self._name} has a favorite number length of {self.favorite_length}, and participated in {len(self.studies)} studies."
