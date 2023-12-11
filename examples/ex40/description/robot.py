import unittest
from inspect import signature
import sys
from task import get_seat


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(get_seat).parameters), 1)

    def test_function_on_zero_as_parameter(self):
        self.assertEqual(get_seat(0), "0. row, left 7. seat")

    def test_function_on_negative_parameter(self):
        self.assertEqual(get_seat(-5), "0. row, left 2. seat")

    def test_function_middle_seat(self):
        self.assertEqual(get_seat(50), "4. row, left 1. seat")

    def test_function_on_max_value(self):
        self.assertEqual(get_seat(sys.maxsize),
                         "658812288346769701. row, right 1. seat")

    def test_function_on_normal_params(self):
        self.assertEqual(get_seat(1), "1. row, right 7. seat")
        self.assertEqual(get_seat(7), "1. row, right 1. seat")
        self.assertEqual(get_seat(8), "1. row, left 1. seat")
        self.assertEqual(get_seat(14), "1. row, left 7. seat")

    def test_function_on_border_values(self):
        self.assertEqual(get_seat(15), "2. row, right 7. seat")
        self.assertEqual(get_seat(21), "2. row, right 1. seat")
        self.assertEqual(get_seat(22), "2. row, left 1. seat")
        self.assertEqual(get_seat(28), "2. row, left 7. seat")

        self.assertEqual(get_seat(57), "5. row, right 7. seat")
        self.assertEqual(get_seat(91), "7. row, right 1. seat")
        self.assertEqual(get_seat(50), "4. row, left 1. seat")
        self.assertEqual(get_seat(84), "6. row, left 7. seat")

    def test_function_values_in_each_row(self):
        self.assertEqual(get_seat(4), "1. row, right 4. seat")
        self.assertEqual(get_seat(18), "2. row, right 4. seat")
        self.assertEqual(get_seat(30), "3. row, right 6. seat")
        self.assertEqual(get_seat(38), "3. row, left 3. seat")

    def test_function_on_large_values(self):
        self.assertEqual(get_seat(175), "13. row, right 1. seat")
        self.assertEqual(get_seat(126), "9. row, left 7. seat")
        self.assertEqual(get_seat(200), "15. row, right 4. seat")
        self.assertEqual(get_seat(959), "69. row, right 1. seat")
        self.assertEqual(get_seat(365), "27. row, right 7. seat")
        self.assertEqual(get_seat(624), "45. row, left 1. seat")
        self.assertEqual(get_seat(1975), "142. row, right 7. seat")


if __name__ == '__main__':
    unittest.main()
