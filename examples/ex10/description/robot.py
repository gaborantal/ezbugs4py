import unittest
from inspect import signature

from task import k_combination


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(k_combination).parameters), 2)

    def test_function_on_empty_text_parameter(self):
        self.assertEqual(k_combination("", ""), 0)
        self.assertEqual(k_combination(5, ""), 0)
        self.assertEqual(k_combination("", 7.3), 0)

    def test_function_on_None_parameter(self):
        self.assertEqual(k_combination(None, None), 0)

    def test_function_on_zero_parameter(self):
        self.assertEqual(k_combination(1, 0), 0)

    def test_function_on_smaller_first_parameter(self):
        self.assertEqual(k_combination(1, 2), 0)

    def test_function_on_negative_parameter(self):
        self.assertEqual(k_combination(-10, 5), 0)
        self.assertEqual(k_combination(5, -1), 0)
        self.assertEqual(k_combination(-7, -12), 0)

    def test_function_on_string_input(self):
        self.assertEqual(k_combination(5, "abc"), 0)
        self.assertEqual(k_combination("asd", 7), 0)
        self.assertEqual(k_combination("apple", "pear"), 0)

    def test_function_on_numerous_correct_parameters(self):
        tests = [
            (10, 4, 210),
            (95, 3, 138415),
            (77, 2, 2926),
            (62, 2, 1891),
            (17, 6, 12376),
        ]
        for n, k, res in tests:
            self.assertEqual(k_combination(n, k), res)


if __name__ == "__main__":
    unittest.main()
