import unittest
from inspect import signature
from task import LightString


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(LightString.__init__).parameters), 3)

    def test_init(self):
        obj = LightString(0, list())
        self.assertEqual(obj.length, 0)
        self.assertEqual(obj._lights, list())
        lights = ["cold_white"] * 10
        obj = LightString(50, lights)
        self.assertEqual(obj.length, 50)
        self.assertEqual(obj._lights, lights)
        self.assertIsNot(obj._lights, lights)
        obj = LightString()
        self.assertEqual(obj.length, 0)
        self.assertEqual(obj._lights, list())
        obj2 = LightString()
        self.assertIsNot(obj._lights, obj2._lights)

    def test_lights_property(self):
        lights = ["red", "blue", "yellow", "green"] * 10
        obj = LightString(200, lights)
        new_lights = obj.lights
        self.assertEqual(new_lights, lights)
        self.assertIsNot(new_lights, lights)
        new_lights = ["warm_white"] * 15
        obj.lights = new_lights
        self.assertEqual(obj._lights, new_lights)
        self.assertIsNot(obj._lights, new_lights)
        with self.assertRaises(TypeError) as context:
            obj.lights = "melon"
        self.assertTrue('The lights can only be a list!' in str(context.exception))

    def test_add_light(self):
        obj = LightString()
        obj.add_light("red")
        self.assertEqual(obj._lights, ["red"])
        obj.add_light("cold_white")
        obj.add_light("warm_white")
        obj.add_light("green")
        obj.add_light("blue")
        obj.add_light("yellow")
        self.assertEqual(obj._lights, ["red", "cold_white", "warm_white", "green", "blue", "yellow"])

    def test_lt(self):
        obj1 = LightString()
        obj2 = LightString()
        obj1.length = 100
        obj2.length = 100
        obj1._lights = ['red']
        obj2._lights = ['red', 'blue']
        self.assertFalse(obj1 < obj2)
        obj1.length = 101
        self.assertFalse(obj1 < obj2)
        obj1.length = 99
        self.assertTrue(obj1 < obj2)

    def test_str(self):
        obj = LightString()
        obj.length = 200
        obj._lights = ['cold_white'] * 25
        self.assertEqual(str(obj), "200 centimeter long light string, 25 pieces (cold_white) colored lights.")
        obj._lights = ['cold_white', 'warm_white'] * 10
        self.assertEqual(str(obj), "200 centimeter long light string, 20 pieces (cold_white, warm_white) colored lights.")
        obj._lights = ['red', 'green', 'blue']
        self.assertEqual(str(obj), "200 centimeter long light string, 3 pieces (blue, green, red) colored lights.")

    def test_eq(self):
        obj = LightString()
        obj.length = 400
        obj._lights = ['red', 'blue', 'yellow', 'green'] * 50
        other = LightString()
        other.length = 400
        other._lights = ['red', 'blue', 'yellow', 'green'] * 50
        self.assertEqual(obj, other)
        obj._lights = ['red', 'blue', 'yellow', 'green']
        self.assertNotEqual(obj, other)
        obj.length = 399
        self.assertNotEqual(obj, other)


if __name__ == "__main__":
    unittest.main()
