import unittest
from inspect import signature

from task import coordinate_transform


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(coordinate_transform).parameters), 2)

    def test_empty_string(self):
        self.assertEqual(coordinate_transform("", tuple()), "")

    def test_no_translation(self):
        self.assertEqual(coordinate_transform("0,0", (0, 0)), "0.0,0.0")
        self.assertEqual(coordinate_transform("1,2 3,4 5,6", (0, 0)), "1.0,2.0 3.0,4.0 5.0,6.0")

    def test_translation(self):
        self.assertEqual(coordinate_transform("12,34", (1, 0)), "13.0,34.0")
        self.assertEqual(coordinate_transform("12,34", (0, 1)), "12.0,35.0")
        self.assertEqual(coordinate_transform("65,12 94,30 41,83", (11, 8)), "76.0,20.0 105.0,38.0 52.0,91.0")
        self.assertEqual(coordinate_transform("12,36 74,95", (-15, -3)), "-3.0,33.0 59.0,92.0")
        self.assertEqual(coordinate_transform("15.25,21.0 35.125,65.5 -15.75,10.5", (-5, 3)), "10.25,24.0 30.125,68.5 -20.75,13.5")
        self.assertEqual(coordinate_transform("15.25,21.0 35.125,-65.5 -15.75,10.5", (5.125, -3.875)), "20.375,17.125 40.25,-69.375 -10.625,6.625")
        self.assertEqual(coordinate_transform("106.125,52.25 -69.125,105.625 41.125,-83.0 -87.75,47.25 -92.5,-111.375 106.25,99.75 -15.125,41.625 -32.0,91.625 22.25,-72.375 -23.625,119.75", (-54.375, 61.375)), '51.75,113.625 -123.5,167.0 -13.25,-21.625 -142.125,108.625 -146.875,-50.0 51.875,161.125 -69.5,103.0 -86.375,153.0 -32.125,-11.0 -78.0,181.125')


if __name__ == "__main__":
    unittest.main()
