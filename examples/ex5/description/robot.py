import unittest
from inspect import signature
from task import circle

class TestRobot(unittest.TestCase):
    
    def test_param_count(self):
        self.assertEqual(len(signature(circle).parameters), 3)
        
    def test_circle(self):
        self.assertEqual(circle(73,55,48), 36.5)
        self.assertEqual(circle(28,45,53), 26.5)
        self.assertEqual(circle(8,15,17), 8.5)
        self.assertEqual(circle(30,40,50), 25.0)
        self.assertEqual(circle(1,4,6), -1)
        self.assertEqual(circle(4,1,6), -1)
        self.assertEqual(circle(4,6,1), -1)
        self.assertEqual(circle(4,3,0), -1)
        self.assertEqual(circle(-1,2,2), -1)
        self.assertEqual(circle(2,-1,2), -1)
        
if __name__ == "__main__":
    unittest.main()