import unittest
from inspect import signature
from task import mode


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(mode).parameters), 1)

    def test_function_on_not_string_param(self):
        self.assertEqual(mode(12345), -99)
        self.assertEqual(mode(1.1), -99)
        self.assertEqual(mode(False), -99)
        self.assertEqual(mode([]), -99)

    def test_function_on_empty_string_parameter(self):
        self.assertEqual(mode(""), -99)
        with self.assertRaises(Exception) as context:
            self.assertEqual(mode(" "), 1)
        self.assertEqual(str(context.exception),
                         "invalid literal for int() with base 10: ' '")

    def test_function_on_only_one_kind_of_number(self):
        self.assertEqual(mode("42;42;42;42;42"), 42)
        self.assertEqual(mode("100"), 100)

    def test_function_on_every_number_appear_exactly_once(self):
        self.assertEqual(mode("7;4;1;2;5;8;9;3"), 7)
        self.assertEqual(mode("3;2"), 3)

    def test_function_no_multiple_modes(self):
        self.assertEqual(mode("0;1;1;2;3;5;8;13;21;34;55;89;144"), 1)
        self.assertEqual(mode("32;2;1024;128;1024;128;2;8;1024"), 1024)
        self.assertEqual(mode("18;36;-3;18;-3;-3;18;36;-3;99"), -3)

    def test_function_multiple_modes_appear(self):
        self.assertEqual(mode("34;23;23;12;12;12;12;23;23;34;34;34"), 34)
        self.assertEqual(mode("111;333;555;777;999;777;555;1111"), 555)
        self.assertEqual(mode("-10;-1;-2;-3;0;0;-1;-5;0;-1;-6;-7;0;"
                              "-1;-8;-9;-10;-1;0"), -1)


if __name__ == "__main__":
    unittest.main()
