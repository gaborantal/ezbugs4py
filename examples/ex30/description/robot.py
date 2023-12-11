import unittest
from inspect import signature
from task import average


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(average).parameters), 1)

    def test_empty_string(self):
        self.assertEqual(average(""), dict())

    def test_keys(self):
        self.assertEqual(average("Andras,3,4,5;Bela,1,2,3;Cecil,4,5,6").keys(), {
            "Andras": 4, "Bela": 2, "Cecil": 5}.keys())

    def test_averages_easy(self):
        self.assertEqual(average("Andras,3,4,5;Bela,1,2,3;Cecil,4,5,6").items(), {
            "Andras": 4, "Bela": 2, "Cecil": 5}.items())

    def test_averages_hard(self):
        self.assertEqual(average("Andras,3,4,5,6,7;Bela,1;Cecil,4,5,6").items(), {
            "Andras": 5.0, "Bela": 1.0, "Cecil": 5.0}.items())


if __name__ == '__main__':
    unittest.main()
