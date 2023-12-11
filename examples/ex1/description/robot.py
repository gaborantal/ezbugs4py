import unittest
from inspect import signature
from task import dict_complete


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(dict_complete).parameters), 1)

    def test_empty_dict(self):
        self.assertEqual(dict_complete({}), {})

    def test_no_missing_values(self):
        self.assertEqual(dict_complete({1: 2}), {1: 2})

    def test_first_key_missing(self):
        self.assertEqual(dict_complete({2: 10, 3: 5}), {1: 0, 2: 10, 3: 5})

    def test_one_missing_key_at_end(self):
        self.assertEqual(dict_complete({1: 2, 2: 10, 4: 15}), {1: 2, 2: 10, 3: 0, 4: 15})

    def test_multiple_missing_keys_at_end(self):
        self.assertEqual(dict_complete({1: 2, 2: 10, 6: 3}), {1: 2, 2: 10, 3: 0, 4: 0, 5: 0, 6: 3})

    def test_one_missing_key_random(self):
        self.assertEqual(dict_complete({4: 2, 2: 10, 5: 8, 1: 15}), {1: 15, 2: 10, 3: 0, 4: 2, 5: 8})

    def test_one_missing_key_random_max(self):
        self.assertEqual(dict_complete({7: 10, 6: 10, 5: 10, 4: 10, 3: 10, 2: 10}), {1: 0, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10})

    def test_multiple_missing_keys_random(self):
        self.assertEqual(dict_complete({8: 20, 10: 10, 1: 30, 5: 40, 7: 50}), {1: 30, 2: 0, 3: 0, 4: 0, 5: 40, 6: 0, 7: 50, 8: 20, 9: 0, 10: 10})

    def test_multiple_missing_keys_random_max(self):
        self.assertEqual(dict_complete({5: 2, 3: 7, 2: 8, 9: 10, 8: 0, 4: 4}), {1: 0, 2: 8, 3: 7, 4: 4, 5: 2, 6: 0, 7: 0, 8: 0, 9: 10})

    def test_multiple_missing_keys_random_max_2(self):
        self.assertEqual(dict_complete({20: 90, 1: 40, 15: 15}), {1: 40, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 15, 16: 0, 17: 0, 18: 0, 19: 0, 20: 90})


if __name__ == "__main__":
    unittest.main()
