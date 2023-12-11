import unittest
from inspect import signature
from task import pixel_art


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(pixel_art).parameters), 2)

    def test_empty_board(self):
        result = pixel_art(
            3,
            {})
        expected = "...\n" \
                   "...\n" \
                   "...\n"
        self.assertEqual(result, expected)

    def test_diagonal_on_board(self):
        result = pixel_art(3,
                           {(0, 0): "A",
                            (1, 1): "B",
                            (2, 2): "C"})
        expected = "A..\n" \
                   ".B.\n" \
                   "..C\n"
        self.assertEqual(result, expected)

    def test_mixed_board(self):
        result = pixel_art(3,
                           {(1, 0): "X",
                            (0, 2): "Y",
                            (2, 2): "Z"})
        expected = ".X.\n" \
                   "...\n" \
                   "Y.Z\n"
        self.assertEqual(result, expected)

    def test_numerous_art_examples(self):
        cases = [
            ([
                 15,
                 {
                     (0, 0): "#",
                     (0, 4): "$",
                     (1, 3): "ä",
                     (4, 8): "/",
                     (14, 14): "/",
                 }
             ], (
                 "#..............\n"
                 "...............\n"
                 "...............\n"
                 ".ä.............\n"
                 "$..............\n"
                 "...............\n"
                 "...............\n"
                 "...............\n"
                 "..../..........\n"
                 "...............\n"
                 "...............\n"
                 "...............\n"
                 "...............\n"
                 "...............\n"
                 "............../\n"
             )),
            ([
                 14,
                 {
                     (0, 0): "#",
                     (0, 4): "$",
                     (1, 3): "ä",
                     (4, 8): "/",
                 }
             ], (
                 "#.............\n"
                 "..............\n"
                 "..............\n"
                 ".ä............\n"
                 "$.............\n"
                 "..............\n"
                 "..............\n"
                 "..............\n"
                 "..../.........\n"
                 "..............\n"
                 "..............\n"
                 "..............\n"
                 "..............\n"
                 "..............\n"
             )),
            ([
                 5,
                 {
                     (1, 0): "#",
                     (0, 3): "$",
                     (1, 3): "ä",
                 }
             ], (
                 ".#...\n"
                 ".....\n"
                 ".....\n"
                 "$ä...\n"
                 ".....\n"
             )),
            ([
                 0,
                 {}
             ], ""),
        ]

        for case, expected_art in cases:
            self.assertEqual(pixel_art(*case), expected_art)


if __name__ == "__main__":
    unittest.main()
