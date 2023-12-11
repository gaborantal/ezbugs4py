class Exam:
    def __init__(self, subject):
        self.subject = subject
        self.questions = []
        self.points = []

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if not isinstance(subject, str) or len(subject) < 3:
            raise ValueError("The subject must be a string at least 3 characters long!")
        self._subject = subject

    def add_question(self, question, point_value):
        if not isinstance(question, str) or not isinstance(point_value, int):
            return
        self.questions.append(question)
        self.points.append(point_value)

    def total_points(self):
        return sum(self.points)

    def __iadd__(self, other):
        if not isinstance(other, Exam):
            raise TypeError()

        for i in range(len(other.questions)):
            if not other.questions[i] in self.questions:
                self.questions.append(other.questions[i])
                self.points.append(other.points[i])

        return self

    def __str__(self):
        ret = self._subject + '\n'
        for i in range(len(self.questions)):
            ret += f"{self.questions[i]} ({self.points[i]} points)\n"
        ret += f"Total: {self.total_points()} points"
        return ret

    def __eq__(self, other):
        return isinstance(other, Exam) and self.__dict__ == other.__dict__
