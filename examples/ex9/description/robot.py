import random
import unittest
from inspect import signature

from task import word_count


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(word_count).parameters), 1)

    def test_function_on_empty_text_parameter(self):
        self.assertEqual(word_count(""), {})

    def test_function_on_None_parameter(self):
        self.assertEqual(word_count(None), {})

    def test_function_on_number_parameter(self):
        self.assertEqual(word_count(3), {})
        self.assertEqual(word_count(2.14), {})
        self.assertEqual(word_count(0), {})

    def test_function_on_dict_parameter(self):
        self.assertEqual(word_count({}), {})
        self.assertEqual(word_count({"one": "pear", "two": "lime"}), {})

    def test_function_some_words_normal_order(self):
        self.assertEqual(word_count("ja ja ja ye ye"), {"ja": 3, "ye": 2})
    
    def test_function_some_words_shuffle_order(self):
        self.assertEqual(word_count("ja ja ye ja ye sure"), {"ja": 3, "ye": 2, "sure": 1})

    def test_function_sentence1(self):
        self.assertEqual(word_count("so sorry but we didnt ask"), {"so": 1, "sorry": 1, "but": 1, "we": 1, "didnt": 1, "ask": 1})

    def test_function_sentence2(self):
        self.assertEqual(word_count("close call for a call"), {"close": 1, "call": 2, "for": 1, "a": 1})


if __name__ == "__main__":
    unittest.main()
