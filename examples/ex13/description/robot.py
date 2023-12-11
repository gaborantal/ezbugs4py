import unittest
from inspect import signature
from task import groupby


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(groupby).parameters), 1)

    def test_function_on_string_parameter_exception(self):
        with self.assertRaises(TypeError):
            groupby('apple')

    def test_function_on_decimal_parameter_exception(self):
        with self.assertRaises(TypeError):
            groupby(1.2)

    def test_function_on_empty_list_parameter_exception(self):
        with self.assertRaises(TypeError):
            groupby([])

    def test_function_on_empty_dict_parameter_exception(self):
        with self.assertRaises(TypeError):
            groupby({'apple': []})
            groupby({})

    def test_function_on_incorrect_dict_parameter_exception(self):
        with self.assertRaises(TypeError):
            groupby({TypeError(): 12})

    def test_function_on_numerous_correct_parameters(self):
        cases = [
            ({
                 'apple': 'fruit',
                 'plum': 'fruit',
                 1: 12,
                 3: 23,
                 5: 23,
                 4: True,
                 3.14: 'number',
                 6.42: True
             }, {
                 'fruit': ['apple', 'plum'],
                 12: [1],
                 23: [3, 5],
                 True: [4, 6.42],
                 'number': [3.14]
             }),
            ({
                 'apple': 'fruit',
                 'plum': 'fruit',
                 1: 12,
                 9: 23,
                 5: 23,
                 4: True,
                 3.14: 'number',
                 6.42: True
             }, {
                 'fruit': ['apple', 'plum'],
                 12: [1],
                 23: [9, 5],
                 True: [4, 6.42],
                 'number': [3.14]
             }),
            ({
                 'apple': 'fruit',
                 'plum': 'fruit',
                 1: 12,
                 9: 23,
                 2: 23,
                 4: True,
                 3.14: 'number',
                 6.42: True
             }, {
                 'fruit': ['apple', 'plum'],
                 12: [1],
                 23: [9, 2],
                 True: [4, 6.42],
                 'number': [3.14]
             }),
            ({
                 'apple': 'fruit',
                 'plum': 'fruit',
                 1: 12,
                 5: 23,
                 4: True,
                 3.14: 'number',
             }, {
                 'fruit': ['apple', 'plum'],
                 12: [1],
                 23: [5],
                 True: [4],
                 'number': [3.14]
             }),
            ({
                 'apple': 'fruit',
                 'plum': 'fruit',
                 1: 12,
                 9: 23,
                 5: 23,
                 4: False,
                 3.14: 'number',
                 6.42: False
             }, {
                 'fruit': ['apple', 'plum'],
                 12: [1],
                 23: [9, 5],
                 False: [4, 6.42],
                 'number': [3.14]
             })
        ]

        for param, output in cases:
            self.assertEqual(groupby(param), output)


if __name__ == "__main__":
    unittest.main()
