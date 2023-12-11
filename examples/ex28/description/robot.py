import unittest
from inspect import signature
from task import threetimes


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(threetimes).parameters), 1)

    def test_empty_string(self):
        self.assertEqual(threetimes(""), [])

    def test_all_once(self):
        self.assertEqual(threetimes("Bela"), [])
        self.assertEqual(threetimes(
            "Bela, Ferenc, Jozsef, Kalman, Jozsef"), [])

    def test_three_times(self):
        self.assertEqual(threetimes(
            "Bela, Ferenc, Bela, Kalman, Bela"), ["Bela"])
        self.assertEqual(sorted(threetimes(
            "Bela, Ferenc, Bela, Kalman, Bela, Elemer, Ferenc, Ferenc")), sorted(["Bela", "Ferenc"]))

    def test_various(self):
        self.assertEqual(threetimes(
            "Bela, Ferenc, Bela, Kalman, Bela, Bela, Ferenc, Ferenc, Kalman"), ["Ferenc"])
        self.assertEqual(sorted(threetimes(
            "Bela, Ferenc, Elemer, Elemer, Bela, Kalman, Elemer, Ferenc, Bela, Peti, Bela, Kalman, Kalman, Peti, Peti")),
            sorted(["Elemer", "Kalman", "Peti"]))


if __name__ == '__main__':
    unittest.main()
