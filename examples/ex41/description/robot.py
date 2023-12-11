import unittest
from inspect import signature
from task import average


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(average).parameters), 1)

    def test_function_on_empty_string(self):
        self.assertEqual(average(""), -1)

    def test_function_on_invalid_input(self):
        self.assertEqual(average("7;a;2"), -1)
        self.assertEqual(average(523), -1)
        self.assertEqual(average(['4;5']), -1)

    def test_function_on_zero_average(self):
        self.assertEqual(average("1;1;1"), 0)
        self.assertEqual(average("1"), 0)

    def test_function_on_numerous_valid_inputs(self):
        self.assertEqual(average("2;1;4;3"), 3.0)
        self.assertEqual(average("5;4"), 4.5)
        self.assertEqual(average("4"), 4)
        self.assertEqual(average("1;1;5;4;3;4;3;8;7;5;6;2"),
                         3.7142857142857144)
        self.assertEqual(average("4;5;3;2;7;1;1;2;2;5;4;4;2;6;1"), 3.3)

    def test_function_on_valid_input_invalid_interval(self):
        self.assertEqual(average("5;1"), 5.0)

    def test_function_on_zero_division(self):
        self.assertEqual(average("1;6;0;7"), 0)


if __name__ == "__main__":
    unittest.main()
