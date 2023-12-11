class Exam(object):
    def __init__(self, subject: str):
        self._subject = subject
        self.questions = list()
        self.points = list()
    
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if not isinstance(value, str):
            raise ValueError("The subject must be a string at least 3 characters long!")
        elif len(value) < 3:
            raise ValueError("The subject must be a string at least 3 characters long!")
        else:
            self._subject = value
    
    def add_question(self, question: str, point_value: int):
        if isinstance(question, str) and isinstance(point_value, int):
            self.questions.append(question)
            self.points.append(point_value)
        
    def total_points(self):
        total = 0
        for points in self.points:
            total += points
        return total
    
    def __iadd__(self, exam):
        if not isinstance(exam, Exam):
            raise TypeError("Incorrect parameter!")
        else:
            index = 0
            for question in exam.questions:
                if question not in self.questions:
                    self.questions.append(question)
                    self.points.append(exam.points[index])
                index += 1
        return self

    #def __str__(self):
        #return self._subject + "\n" + 
    
    def __eq__(self, exam):
        questions_bool = True
        points_bool = True
        for question in exam.questions:
            if question not in self.questions:
                questions_bool = False
        if self._subject == exam._subject and questions_bool and points_bool:
            return True
        else:
            return False
