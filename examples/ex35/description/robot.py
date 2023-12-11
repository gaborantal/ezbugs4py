import unittest
from inspect import signature
from task import proportion


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(proportion).parameters), 2)

    def test_function_on_empty_string(self):
        self.assertEqual(proportion("", ""), -1)
        self.assertNotEqual(proportion("asd", ""), -1)
        self.assertEqual(proportion("", "531"), -1)

    def test_function_on_params_not_string(self):
        self.assertEqual(proportion(534, ""), -1)
        self.assertEqual(proportion("apple", 4.12), -1)
        self.assertEqual(proportion(True, 4.12), -1)
        self.assertEqual(proportion(['abc'], "s"), -1)
        self.assertEqual(proportion(['apple'], ["s"]), -1)

    def test_function_on_three_letter_long_first_param(self):
        self.assertEqual(proportion("bob", "b"), 0.6666666666666666)
        self.assertNotEqual(proportion("dad", "a"), 0.33)

    def test_function_on_two_letter_long_second_param(self):
        self.assertEqual(proportion("aac", "aa"), -1)
        self.assertEqual(proportion("this that", "a "), -1)

    def test_function_on_multiple_letter_first_param(self):
        self.assertEqual(proportion("aaasdvavaalkslaoaac", "a"),
                         0.47368421052631576)
        self.assertEqual(proportion("abvsd bbcx vncds", "a"), 0.0625)
        self.assertEqual(
            proportion("ajlsdgaljagdfadkljdkjjisofffjkgfahghiifsdjfsgsdg",
                       "f"), 0.14583333333333334)

    def test_function_on_zero_found_letters(self):
        self.assertEqual(proportion("bababab", "d"), 0)
        self.assertEqual(proportion("FRUITS", "s"), 0)
        self.assertEqual(proportion("fRUITS", "f"), 0.16666666666666666)

    def test_function_on_minimal_text_input(self):
        self.assertEqual(proportion("b", "b"), 1.0)
        self.assertEqual(proportion("a", "a"), 1)
        self.assertEqual(proportion("C", "c"), 0)
        self.assertEqual(proportion(" ", " "), 1)


if __name__ == "__main__":
    unittest.main()
