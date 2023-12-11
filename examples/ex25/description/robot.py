import unittest
from inspect import signature
from task import n_grammer


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(n_grammer).parameters), 2)

    def test_no_slice_needed(self):
        self.assertEqual(n_grammer('29', 2), [29])
        self.assertEqual(n_grammer('55554', 5), [55554])
        self.assertEqual(n_grammer('5', 1), [5])

    def test_default_parameter(self):
        try:
            n_grammer('2222')
        except TypeError:
            self.fail("Number parameter must be optional")

    def test_exact_pieces(self):
        self.assertEqual(n_grammer('222222', 2), [22, 22, 22])
        self.assertEqual(n_grammer('12345671234567', 7), [1234567, 1234567])
        self.assertEqual(n_grammer('963852741', 1), [9, 6, 3, 8, 5, 2, 7, 4, 1])

    def test_needs_fill(self):
        self.assertEqual(n_grammer('12345612345', 6), [123456, 123450])
        self.assertEqual(n_grammer('1', 2), [10])
        self.assertEqual(n_grammer('1597532584', 3), [159, 753, 258, 400])


if __name__ == '__main__':
    unittest.main()
