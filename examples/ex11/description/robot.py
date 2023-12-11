import unittest
import random
from inspect import signature
from task import is_happy


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(is_happy).parameters), 2)

    def test_function_on_string_parameter(self):
        self.assertEqual(is_happy("apple", []), None)
        self.assertEqual(is_happy("apple", "pear"), None)

    def test_function_on_decimal_parameter(self):
        self.assertEqual(is_happy(1.2, []), None)
        self.assertEqual(is_happy(6.21, 8.33), None)

    def test_function_on_empty_list_first_parameter(self):
        self.assertEqual(is_happy([], []), None)
        self.assertEqual(is_happy([], ["apple", "pear"]), None)

    def test_function_on_numerous_correct_parameters(self):
        happy_numbers = [
            1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79,
            82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139,
            167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230,
            236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313,
            319, 320, 326, 329, 331, 338
        ]
        for i in range(32):
            number = random.randint(1, 338)
            self.assertEqual(is_happy(number, []), number in happy_numbers)


if __name__ == "__main__":
    unittest.main()
