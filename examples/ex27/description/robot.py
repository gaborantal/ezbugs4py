import unittest
from inspect import signature
from task import split


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(split).parameters), 2)

    def test_example_input(self):
        self.assertEqual(split(
            "This is the best day of my life because it is almost Christmas.", [2, 1, 3]
        ),
            ["This is", "the", "best day of", "my life because it is almost Christmas."])
        self.assertEqual(split(
            "Stay awhile and listen.", [2, 4]
        ), [])

    def test_default_parameter(self):
        try:
            self.assertEqual(split(
                "Lorem ipsum dolor sit amet."
            ),
                ["Lorem ipsum dolor sit amet."]
            )
        except TypeError:
            self.fail("Number list must be optional!")

    def test_too_short_text(self):
        self.assertEqual(split("", [2]), [])
        self.assertEqual(split("a b", [1, 2]), [])
        self.assertEqual(split("a b c", [2, 3]), [])

    def test_exact_length(self):
        self.assertEqual(split("a bc def", [2, 1]), ["a bc", "def"])
        self.assertEqual(split("a bc def", [1, 2]), ["a", "bc def"])
        self.assertEqual(split("a bc def", [1, 1, 1]), ["a", "bc", "def"])

    def test_too_long_text(self):
        self.assertEqual(split("a bc def", [2]), ["a bc", "def"])
        self.assertEqual(split("a bc def", [1]), ["a", "bc def"])
        self.assertEqual(split("a bc def", [1, 1]), ["a", "bc", "def"])


if __name__ == '__main__':
    unittest.main()
