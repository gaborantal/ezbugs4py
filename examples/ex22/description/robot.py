import unittest
from task import twice


class TestRobot(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(twice(""), [])

    def test_all_once(self):
        self.assertEqual(twice("Bela"), [])
        self.assertEqual(twice("Bela, Ferenc, Jozsef, Kalman"), [])

    def test_twice(self):
        self.assertEqual(twice("Bela, Ferenc, Bela, Kalman"), ["Bela"])
        self.assertEqual(sorted(twice("Bela, Ferenc, Bela, Kalman, Elemer, Ferenc")), sorted(["Bela", "Ferenc"]))

    def test_more(self):
        self.assertEqual(twice(
            "Bela, Ferenc, Bela, Kalman, Bela, Ferenc"), ["Ferenc"])
        self.assertEqual(sorted(twice(
            "Bela, Ferenc, Elemer, Bela, Kalman, Elemer, Ferenc, Bela, Peti, Peti, Peti, Peti")),
            sorted(["Elemer", "Ferenc"]))


if __name__ == '__main__':
    unittest.main()
