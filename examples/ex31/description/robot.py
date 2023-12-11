import unittest
from inspect import signature
from task import Basket


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(Basket.__init__).parameters), 3)

    def test_fields(self):
        target = Basket("wood", 8)
        self.assertEqual(target.material, 'wood')
        self.assertEqual(target._size, 8)
        self.assertEqual(target.candies, list())

    def test_getter_property(self):
        target = Basket("wood", 8)
        self.assertEqual(target.size, 8)

    def test_setter_property(self):
        target = Basket("wood", 8)
        target.size = 300
        self.assertEqual(target._size, 300)

    def test_setter_property_candies_cut(self):
        target = Basket("wood", 3)
        target.candies = ["apple", "pear", "lemon"]
        target.size = 2
        self.assertEqual(target.candies, ["apple", "pear"])

    def test_add_candies_full(self):
        target = Basket("wood", 3)
        target._size = 3
        target.candies = ["apple", "pear", "lemon"]
        try:
            target.add_candy("banana")
        except ValueError as e:
            self.assertEqual(str(e), "The basket is full")
        self.assertEqual(target.candies, ["apple", "pear", "lemon"])

    def test_candy_already_in_basket(self):
        target = Basket("wood", 10)
        target.candies = ["apple", "pear", "lemon"]
        try:
            target.add_candy("pear")
        except ValueError as e:
            self.assertEqual(str(e), "This candy is already in the basket")
        self.assertEqual(target.candies, ["apple", "pear", "lemon"])

    def test_add_candy_correct_parameter(self):
        target = Basket("wood", 4)
        target.candies = ["apple", "pear", "lemon"]
        target.add_candy("banana")
        self.assertEqual(len(target.candies), 4)
        self.assertEqual(target.candies, ["apple", "pear", "lemon", "banana"])

    def test_add_operator_result_object(self):
        target1 = Basket("wood", 200)
        target2 = Basket("plastic", 300)
        result = target1 + target2
        self.assertIsNot(result, target1)
        self.assertIsNot(result, target2)

    def test_add_operator_basket_fields(self):
        target1 = Basket("wood", 200)
        target2 = Basket("plastic", 300)
        result = target1 + target2
        self.assertEqual(result.material, "mixed material")
        self.assertEqual(result._size, 500)

    def test_add_operator_candies(self):
        target1 = Basket("wood", 200)
        target2 = Basket("plastic", 300)
        target1.candies = ["apple", "pear"]
        target2.candies = ["banana", "peach"]
        result = target1 + target2
        self.assertEqual(sorted(result.candies), sorted(["apple", "pear", "banana", "peach"]))

    def test_str_operator(self):
        target = Basket("wood", 200)
        target.material = "wood"
        target._size = 200
        target.candies = ["apple", "pear"]
        self.assertEqual(
            str(target), "The wood basket size is 200, currently there are 2 candies in it")
        target.material = "plastic"
        target._size = 10
        target.candies = ["apple"]
        self.assertEqual(
            str(target), "The plastic basket size is 10, currently there are 1 candies in it")

    def test_eq_operator(self):
        target1 = Basket("wood", 200)
        target1.material = "wood"
        target1._size = 200
        target1.candies = ["apple", "pear"]

        target2 = Basket("wood", 200)
        target2.material = "wood"
        target2._size = 200
        target2.candies = ["apple", "pear", "banana"]

        self.assertTrue(target1 == target2)

        target2._size = 201
        self.assertFalse(target1 == target2)


if __name__ == '__main__':
    unittest.main()
