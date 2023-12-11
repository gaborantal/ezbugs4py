import unittest
from inspect import signature

from task import Triangle


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(Triangle.__init__).parameters), 4)

    def test_init(self):
        obj = Triangle(2, 3, 4)
        self.assertEqual(obj._a, 2)
        self.assertEqual(obj.b, 3)
        self.assertEqual(obj.c, 4)

    def test_init_default(self):
        obj = Triangle(2, 3)
        self.assertEqual(obj._a, 2)
        self.assertEqual(obj.b, 3)
        self.assertEqual(obj.c, 2)

    def test_init_single_param(self):
        obj = Triangle(5)
        self.assertEqual(obj._a, 5)
        self.assertEqual(obj.b, 5)
        self.assertEqual(obj.c, 5)

    def test_a_property(self):
        obj = Triangle(10, 45, 23)
        self.assertEqual(obj.a, 10)
        self.assertEqual(obj.a_values, [10])
        obj.a = 15
        self.assertEqual(obj._a, 15)
        self.assertEqual(obj.a_values, [10, 15])
        obj.a = 33
        self.assertEqual(obj.a_values, [10, 15, 33])

    def test_a_property_invalid_type(self):
        obj = Triangle(11, 45, 23)
        with self.assertRaises(Exception) as context:
            obj.a = '69'
        self.assertTrue('Invalid value' in str(context.exception))
        with self.assertRaises(Exception) as context:
            obj.a = 2.0
        self.assertEqual(obj.a, 11)

    def test_perimeter(self):
        obj = Triangle(2, 3, 5)
        self.assertEqual(obj.perimeter(), 10)
        obj = Triangle(24, 42, 32)
        self.assertEqual(obj.perimeter(), 98)

    def test_area(self):
        obj = Triangle(3, 4, 5)
        self.assertEqual(obj.area(), 6)
        obj = Triangle(13, 5, 12)
        self.assertEqual(obj.area(), 30)

    def test_eq(self):
        obj = Triangle(5, 4, 3)
        other = Triangle(3, 4, 5)
        self.assertEqual(obj, other)
        obj.a = 10
        other.a = 15
        self.assertNotEqual(obj, other)

    def test_str(self):
        obj = Triangle(3, 4, 5)
        self.assertEqual(str(obj), "The changes in the a values, 1")
        obj.a = 15
        self.assertEqual(str(obj), "The changes in the a values, 2")
        obj.a = 15
        self.assertEqual(str(obj), "The changes in the a values, 3")


if __name__ == "__main__":
    unittest.main()
