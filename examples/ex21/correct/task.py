class Course:
    def __init__(self, name, course_code='UNKNOWN'):
        self._name = name
        self.course_code = course_code
        self.students = []

    @property
    def course_code(self):
        return self._course_code.upper()

    @course_code.setter
    def course_code(self, value):
        self._course_code = value.upper() if isinstance(value, str) and value != '' else 'SOMETHING'

    def __str__(self):
        return f"{self._name} (code: {self.course_code})"

    def list_students(self):
        if len(self.students) == 0:
            return 'No one has enrolled in this course!'

        return ', '.join(self.students)

    def __iadd__(self, neptun_codes):
        if len(neptun_codes) == 0:
            raise ValueError('Empty list!')

        if len([n for n in neptun_codes if isinstance(n, str) and len(n) == 6]) != len(neptun_codes):
            raise ValueError('Incorrect Neptun code list!')

        for neptun in neptun_codes:
            if neptun not in self.students:
                self.students.append(neptun)

        return self

    def __eq__(self, other):
        return isinstance(other, Course) and self.__dict__ == other.__dict__
