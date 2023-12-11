class Teacher:
    def __init__(self, name, _retirement_year=2062):
        self._name = name
        self._retirement_year = _retirement_year
        self.teaches = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def retirement_year(self):
        return self._retirement_year

    @retirement_year.setter
    def retirement_year(self, value):
        if isinstance(value, int):
            if value >= 1970:
                self._retirement_year = value

    def teaches_new_class(self, class_name, num):
        if not isinstance(class_name, str) and not isinstance(num, int):
            raise ValueError("Incorrect parameters!")

        # if self.tanit == 0:

    def __gt__(self, otherteacher):
        if isinstance(otherteacher, Teacher):
            if len(self.teaches) > len(otherteacher.teaches):
                return True

    def __str__(self):
        return f"The teacher named {self._name} will retire in {str(self._retirement_year)}."
