import unittest
from inspect import signature
from task import Teacher


class TestRobot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            Teacher("Aladar", 2022)
        except AttributeError:
            cls.fail("Missing class!")
        except TypeError:
            cls.fail("Incorrect constructor!")
        except RecursionError:
            cls.fail("Infinite loop!")
        except BaseException as e:
            cls.fail(f"Something went wrong: {e}")

    def test_init_param_count(self):
        self.assertEqual(len(signature(Teacher.__init__).parameters), 3)

    def test_init(self):
        t = Teacher("Aladar", 2022)
        self.assertEqual(t.name, "Aladar")
        self.assertEqual(t._retirement_year, 2022)
        self.assertEqual(t.teaches, {})

    def test_init_default_parameter(self):
        t = Teacher("Aladar")
        self.assertEqual(t.name, "Aladar")
        self.assertEqual(t._retirement_year, 2062)
        self.assertEqual(t.teaches, {})

    def test_getter(self):
        t = Teacher("Aladar", 2022)
        self.assertEqual(t.retirement_year, 2022)

    def test_setter_correct_parameter(self):
        t = Teacher("Aladar", 2022)
        t.retirement_year = 2100
        self.assertEqual(t.retirement_year, 2100)
        t.retirement_year = 1970
        self.assertEqual(t.retirement_year, 1970)

    def test_setter_incorrect_parameter(self):
        t = Teacher("Aladar", 2022)
        t.retirement_year = 1900
        self.assertEqual(t.retirement_year, 2022)
        t.retirement_year = 1969
        self.assertEqual(t.retirement_year, 2022)
        t.retirement_year = "apple"
        self.assertEqual(t.retirement_year, 2022)

    def test_teaches_new_class_incorrect_parameter_1(self):
        t = Teacher("Aladar", 2022)
        with self.assertRaises(ValueError, msg="Incorrect error type"):
            t.teaches_new_class("apple", "pear")
        try:
            t.teaches_new_class("apple", "pear")
        except ValueError as e:
            self.assertEqual(str(e), "Incorrect parameters!")
        except BaseException:
            self.fail("Incorrect error type")

    def test_teaches_new_class_incorrect_parameter_2(self):
        t = Teacher("Aladar", 2022)
        with self.assertRaises(ValueError, msg="Incorrect error type"):
            t.teaches_new_class("apple", "pear")
        try:
            t.teaches_new_class(42, 12)
        except ValueError as e:
            self.assertEqual(str(e), "Incorrect parameters!")
        except BaseException:
            self.fail("Incorrect error type")

    def test_teaches_new_class_incorrect_parameter_3(self):
        t = Teacher("Aladar", 2022)
        with self.assertRaises(ValueError, msg="Incorrect error type"):
            t.teaches_new_class("apple", "pear")
        try:
            t.teaches_new_class("5.a", 0)
        except ValueError as e:
            self.assertEqual(str(e), "Incorrect parameters!")
        except BaseException:
            self.fail("Incorrect error type")

    def test_teaches_new_class_correct_parameter(self):
        t = Teacher("Aladar", 2022)
        t.teaches_new_class("5.a", 10)
        t.teaches_new_class("6.b", 20)
        t.teaches_new_class("5.a", 30)
        self.assertEqual(t.teaches, {"5.a": 30, "6.b": 20})

    def test_gt_operator(self):
        t1 = Teacher("Aladar", 2100)
        t2 = Teacher("Bela", 2200)
        t1.teaches_new_class("5.a", 10)
        t1.teaches_new_class("6.b", 20)
        t2.teaches_new_class("5.a", 20)
        t2.teaches_new_class("6.b", 10)
        self.assertFalse(t1 > t2)
        t2.teaches_new_class("7.a", 1)
        self.assertFalse(t1 > t2)
        t1.teaches_new_class("7.b", 2)
        self.assertTrue(t1 > t2)

    def test_str_operator(self):
        t = Teacher("Aladar", 2022)
        self.assertEqual(str(t), "The teacher named Aladar will retire in 2022.")


if __name__ == '__main__':
    unittest.main()
