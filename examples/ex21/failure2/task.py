class Course():
    def __init__(self, _name, _course_code = "UNKNOWN"):
        self._name = _name
        self.course_code = _course_code
        self.students = list()

    @property
    def course_code(self):
        return str(self._course_code.upper())

    @course_code.setter
    def course_code(self, ccode):
        if isinstance(ccode, str) and ccode != "":
            self._course_code = ccode.upper()
        else:
            self._course_code = "SOMETHING"

    def __str__(self):
        return str(self._name) + " (code: " + str(self.course_code) + ")"

    def list_students(self):
        if len(self.students) == 0:
            return "No one has enrolled in this course!"
        else:
            ret = ""
            for i in self.students:
                ret += str(i) + ", "
            return ret

    def __iadd__(self, ncode):
        try:
            if len(ncode) == 0:
                raise ValueError("Empty list!")
            elif len(ncode) != 0:
                for i in ncode:
                    if not isinstance(i, str) or len(i) != 6:
                        raise ValueError("Incorrect Neptun-code list!")
            else:
                for i in ncode:
                    if i not in self.students:
                        self.students.append(i)
        except ValueError as exc:
            print(exc)

    def __eq__(self, other):
        if isinstance(other, Course):
            if self._name == other._name and self.course_code == other.course_code and self.students == other.students:
                return True
            else:
                return False
        else:
            return False
