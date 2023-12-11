class Mathematician:

    def __init__(self, name, favorite_length=3):
        self._name = name
        self.favorite_length = favorite_length
        self.studies = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        if isinstance(new, str):
            self._name = new

    def add_study(self, nums):
        same = False
        size = 0
        for i in range(len(nums)):
            if i < len(nums) and len(nums[i]) == len(nums[i + 1]):
                size = len(nums[i])
                same = True
            else:
                same = False
                raise ValueError("Ugly numbers")

        if same == True and self.favorite_length == size:
            self.studies[self.favorite_length] = nums
        else:
            self.studies[self.favorite_length] = size

    def __lt__(self, other):
        if self.favorite_length < other.favorite_length:
            return True
        else:
            return False

    def __str__(self):
        return f'The mathematician named {self.name} has a favorite number length of {self.favorite_length}, and participated in {len(self.studies)} studies.'
