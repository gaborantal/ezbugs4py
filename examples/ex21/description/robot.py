import unittest
import task

class CourseTestCase(unittest.TestCase):

    def setUp(self):
        self.course = task.Course('Calculus III', 'CALC-EASY-123')

    def test_course_creation(self):
        self.assertEqual(self.course._name, "Calculus III")
        self.assertEqual(self.course._course_code, "CALC-EASY-123")
        self.assertEqual(self.course.students, [])

    def test_course_creation_without_course_code(self):
        course = task.Course('Discrete Mathematics')
        self.assertEqual(course._course_code, "UNKNOWN")

    def test_course_code_property_getter(self):
        self.assertEqual(self.course.course_code, 'CALC-EASY-123')
        self.course._course_code = 'calc-easy-123'
        self.assertEqual(self.course.course_code, 'CALC-EASY-123')

    def test_course_code_property_setter(self):
        self.course.course_code = 'easy-subject'
        self.assertEqual(self.course._course_code, 'EASY-SUBJECT')

    def test_course_string_representation(self):
        self.assertEqual(str(self.course), "Calculus III (code: CALC-EASY-123)")
        self.course._course_code = 'calc-easy-123'
        self.assertEqual(str(self.course), "Calculus III (code: CALC-EASY-123)")

    def test_list_students_method(self):
        self.assertEqual(self.course.list_students(), "No one has enrolled in this course!")
        self.course.students = ['NEP4LF']
        self.assertEqual(self.course.list_students(), "NEP4LF")
        self.course.students = ['NEP4LF', 'ASD123', 'F00B4R']
        self.assertEqual(self.course.list_students(), "NEP4LF, ASD123, F00B4R")

    def test_iadd_operator(self):
        with self.assertRaises(ValueError):
            self.course += []
        with self.assertRaises(ValueError):
            self.course += ['ABCDEF', 'B4R4CK', 123456, 'N3PTUN']
        with self.assertRaises(ValueError):
            self.course += ['ASD123', 'F00B4R', 'TOOLONG', 'NEP4LF']

        self.course.students = []
        self.course += ['NEP4LF']
        self.assertIn('NEP4LF', self.course.students)

        self.course.students = []
        self.course += ['NEP4LF', 'ASD123', 'F00B4R']
        self.assertCountEqual(self.course.students, ['NEP4LF', 'ASD123', 'F00B4R'])

        self.course.students = ['NEP4LF']
        self.course += ['ASD123', 'F00B4R', 'NEP4LF']
        self.assertCountEqual(self.course.students, ['NEP4LF', 'ASD123', 'F00B4R'])

    def test_eq_operator(self):
        other = task.Course('Calculus III', 'CALC-EASY-123')
        self.assertTrue(self.course == other)

        self.course.students = ['ABCXYZ', 'NEPTUN', 'CAT', 'ASDQWE', '123456']
        other.students = ['ABCXYZ', 'NEPTUN', 'CAT', 'ASDQWE', '123456']
        self.assertTrue(self.course == other)

        self.course.students = ['ABCXYZ', 'NEPTUN', 'CAT', 'ASDQWE', '123456']
        other.students = ['ABCXYZ', 'NEPTUN', 'CAT', 'ASDQWE']
        self.assertFalse(self.course == other)

        self.assertFalse(self.course == 'goat cheese')

if __name__ == "__main__":
    unittest.main()
