import unittest
import task


class TestExam(unittest.TestCase):

    def setUp(self):
        self.obj = task.Exam("Script Languages")

    def test_init_and_attributes(self):
        """Test the __init__ method and attributes."""
        self.assertEqual(self.obj._subject, "Script Languages", "_subject is set correctly")
        self.assertEqual(self.obj.questions, [], "questions is set correctly")
        self.assertEqual(self.obj.points, [], "points is set correctly")

        with self.assertRaises(ValueError):
            task.Exam(3)  # Should raise ValueError

        with self.assertRaises(ValueError):
            task.Exam("Sz")  # Should raise ValueError

    def test_subject_getter(self):
        self.assertEqual(self.obj.subject, "Script Languages", "get subject property")

    def test_subject_setter(self):
        self.obj.subject = "Programming I."
        self.assertEqual(self.obj._subject, "Programming I.", "setter sets good value (basic scenario)")

    def test_subject_setter_exception(self):
        with self.assertRaises(ValueError) as context:
            self.obj.subject = None
        self.assertEqual(str(context.exception), "The subject must be a string at least 3 characters long!")

    def test_subject_setter_short_value_exception(self):
        with self.assertRaises(ValueError) as context:
            self.obj.subject = "No"
        self.assertEqual(str(context.exception), "The subject must be a string at least 3 characters long!")

    def test_add_question(self):
        self.obj.add_question("When is your birthday?", 5)
        self.assertEqual(self.obj.questions, ["When is your birthday?"])
        self.assertEqual(self.obj.points, [5])

        self.obj.add_question("What is your name?", 1)
        self.assertEqual(self.obj.questions, ["When is your birthday?", "What is your name?"])
        self.assertEqual(self.obj.points, [5, 1])

        self.obj.add_question("What is the name of the lecturer? (tricky)", 15)
        self.assertEqual(self.obj.questions, ["When is your birthday?", "What is your name?", "What is the name of the lecturer? (tricky)"])
        self.assertEqual(self.obj.points, [5, 1, 15])

    def test_total_points(self):
        self.obj.questions = ["Good question"] * 3
        self.obj.points = [16, 42, 95]
        self.assertEqual(self.obj.total_points(), 153)

        self.obj.questions = ["Good question"] * 6
        self.obj.points = [6, 15, 20, 8, 7, 4]
        self.assertEqual(self.obj.total_points(), 60)

    def test_iadd(self):
        self.obj1 = task.Exam("Something")
        self.obj2 = task.Exam("Else")
        self.obj1.questions = ["Good question", "Another great question"]
        self.obj1.points = [2, 3]
        self.obj2.questions = ["What is the purpose of life?", "Is Java dead?"]
        self.obj2.points = [5, 10]

        self.obj1 += self.obj2
        self.assertEqual(self.obj1.questions, ["Good question", "Another great question", "What is the purpose of life?", "Is Java dead?"])
        self.assertEqual(self.obj1.points, [2, 3, 5, 10])

        self.obj2.questions = ["What is the purpose of life?", "42?"]
        self.obj2.points = [5, 7]

        self.obj1 += self.obj2
        self.assertEqual(self.obj1.questions, ["Good question", "Another great question", "What is the purpose of life?", "Is Java dead?", "42?"])
        self.assertEqual(self.obj1.points, [2, 3, 5, 10, 7])

    def test_iadd_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.obj += None

    def test_str_empty(self):
        exam = task.Exam("Script Languages")
        self.assertEqual(str(exam), "Script Languages\nTotal: 0 points")

    def test_str_with_data(self):
        exam = task.Exam("Script Languages")
        exam.questions.append("Good question")
        exam.questions.append("Another great question")
        exam.points = [2, 3]
        self.assertEqual(str(exam), "Script Languages\nGood question (2 points)\nAnother great question (3 points)\nTotal: 5 points")

    def test_eq_different_subject(self):
        exam1 = task.Exam("Appdev")
        exam2 = task.Exam("Script")
        self.assertNotEqual(exam1, exam2)

    def test_eq_same_data(self):
        exam1 = task.Exam("Appdev")
        exam1.questions = ["How?", "Is?", "This?"]
        exam1.points = [4, 2, 3]
        exam2 = task.Exam("Appdev")
        exam2.questions = ["How?", "Is?", "This?"]
        exam2.points = [4, 2, 3]
        self.assertEqual(exam1, exam2)

    def test_eq_different_questions(self):
        exam1 = task.Exam("Appdev")
        exam1.questions = ["How?", "Is?", "This?"]
        exam1.points = [4, 2, 3]
        exam2 = task.Exam("Appdev")
        exam2.questions = ["What?", "Is?", "That?"]
        exam2.points = [4, 2, 3]
        self.assertNotEqual(exam1, exam2)

    def test_eq_different_points(self):
        exam1 = task.Exam("Appdev")
        exam1.questions = ["How?", "Is?", "This?"]
        exam1.points = [4, 2, 3]
        exam2 = task.Exam("Appdev")
        exam2.questions = ["How?", "Is?", "This?"]
        exam2.points = [4, 1, 3]
        self.assertNotEqual(exam1, exam2)


if __name__ == "__main__":
    unittest.main()
