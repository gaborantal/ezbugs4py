import unittest
from inspect import signature
from task import is_triangle


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(is_triangle).parameters), 3)

    def test_function_on_valid_values(self):
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(6, 8, 10))
        self.assertFalse(is_triangle(41, 40, 9))
        self.assertFalse(is_triangle(40, 50, 30))

    def test_function_on_invalid_values(self):
        self.assertFalse(is_triangle(3, 4, 6))
        self.assertFalse(is_triangle(2, 5, 10))

    def test_on_negative_parameter(self):
        self.assertFalse(is_triangle(-3, 4, 5))
        self.assertFalse(is_triangle(3, -4, 5))

    def test_function_on_zero_parameters(self):
        self.assertFalse(is_triangle(0, 4, 5))
        self.assertFalse(is_triangle(0, 0, 0))

    def test_function_on_non_integer_parameter(self):
        self.assertFalse(is_triangle(3, 4.5, 5))
        self.assertFalse(is_triangle(1.2, 5.6, 4))

    def test_function_on_invalid_parameter_type(self):
        self.assertFalse(is_triangle(3, '4', 5))
        self.assertFalse(is_triangle('2', 3, 4))
        self.assertFalse(is_triangle(4, 5, ''))


if __name__ == "__main__":
    unittest.main()
