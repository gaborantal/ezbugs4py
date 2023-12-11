class Exam(object):
    def __init__(self, subject):
        self.subject = subject
        self.questions = list()
        self.points = list()

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("The subject must be a string at least 3 characters long!")
        else:
            self._subject = value

    def add_question(self, question, point_value):
        if isinstance(question, str) and isinstance(point_value, int):
            self.questions.append(question)
            self.points.append(point_value)

    def total_points(self):
        total = 0
        for value in self.points:
            total += value
        return total

    def __iadd__(self, other):
        if not isinstance(other, Exam):
            raise TypeError("Not an Exam type")
        else:
            for value in range(0, len(self.questions)):
                if self.questions.__contains__(other.questions[value]):
                    pass
                else:
                    self.questions.append(other.questions[value])
                    self.points.append(other.points[value])

        return self

    def __str__(self):
        return f"{self._subject}\n,{self.questions}({self.points})\n,Total:{self.questions},{self.total_points()}"

    def __eq__(self, other):
        if isinstance(other, Exam):
            if self.__dict__ == other.__dict__:
                return True
            else:
                return False
        else:
            return False
