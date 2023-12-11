import unittest
from inspect import signature
from task import Point


class TestRobot(unittest.TestCase):

    def test_point_init_param_count(self):
        self.assertEqual(len(signature(Point.__init__).parameters), 3)

    def test_point_creation_on_wrong_params(self):
        with self.assertRaises(ValueError) as context:
            p = Point(1, 1)
        self.assertEqual(str(context.exception),
                         "Wrong X value: 1, <class 'int'>")

        with self.assertRaises(Exception) as context:
            p = Point(1.2, 1)
        self.assertEqual(str(context.exception),
                         "Wrong Y value: 1, <class 'int'>")

        with self.assertRaises(Exception) as context:
            p = Point(None, 1.2)
        self.assertEqual(str(context.exception),
                         "Wrong X value: None, <class 'NoneType'>")

        with self.assertRaises(Exception) as context:
            p = Point("1.2", "3.3")
        self.assertEqual(str(context.exception),
                         "Wrong X value: 1.2, <class 'str'>")

    def test_point_function_str(self):
        p = Point(1.2, 3.3)
        self.assertEqual(str(p), "P(1.2,3.3)")
        p = Point(33.3, 10.0)
        self.assertEqual(str(p), "P(33.3,10.0)")
        p = Point(10., 100.0)
        self.assertEqual(str(p), "P(10.0,100.0)")

    def test_point_function_eq(self):
        p1 = Point(6.0, 6.0)
        self.assertFalse(p1 == 6.0)
        self.assertFalse(p1 == "P(6.0,6.0)")
        p2 = Point(6.0, 6.0)
        self.assertTrue(p1 == p2)
        p2 = Point(6.0, 6.1)
        self.assertFalse(p1 == p2)


if __name__ == "__main__":
    unittest.main()
