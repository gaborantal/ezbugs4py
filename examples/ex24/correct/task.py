class Teacher:
    def __init__(self, name, _retirement_year=2062):
        self.name = name
        self._retirement_year = _retirement_year
        self.teaches = {}

    @property
    def retirement_year(self):
        return self._retirement_year

    @retirement_year.setter
    def retirement_year(self, value):
        if isinstance(value, int) and value >= 1970:
            self._retirement_year = value

    def teaches_new_class(self, class_name, num_of_students):
        teaches = False
        if isinstance(class_name, str) and isinstance(num_of_students, int):
            for element in self.teaches.keys():
                if element == class_name:
                    teaches = True

            if self.teaches.get(class_name) is None and teaches == False:
                self.teaches[class_name] = num_of_students
            elif teaches:
                self.teaches[class_name] = num_of_students
        else:
            raise ValueError("Incorrect parameters!")

    def __gt__(self, other):
        teacher1 = 0
        teacher2 = 0
        for element in self.teaches.values():
            teacher1 += element
        for element in other.teaches.values():
            teacher2 += element

        if teacher1 > teacher2:
            return True
        else:
            return False

    def __str__(self):
        return "The teacher named " + self.name + " will retire in " + str(self._retirement_year) + "."
