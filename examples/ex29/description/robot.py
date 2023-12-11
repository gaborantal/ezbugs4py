import unittest
from inspect import signature
from task import HauntedHouse


class TestRobot(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        try:
            HauntedHouse("Apple Street 4.", 15)
        except AttributeError:
            self.fail("Missing class!")
        except TypeError:
            self.fail("Incorrect constructor!")
        except RecursionError:
            self.fail("Infinite loop!")

        super().setUpClass()

    def test_init_param_count(self):
        self.assertEqual(len(signature(HauntedHouse.__init__).parameters), 3)

    def test_fields(self):
        target = HauntedHouse("Apple Street 4.", 15)
        self.assertEqual(target.address, 'Apple Street 4.')
        self.assertEqual(target._number_of_cats, 15)
        self.assertEqual(target.ghosts, list())

    def test_init_number_of_cats_incorrect(self):
        target = HauntedHouse('Apple Street 4.', 9)
        self.assertEqual(target.number_of_cats, 10)

    def test_getter_property(self):
        target = HauntedHouse("Apple Street 4.", 15)
        self.assertEqual(target.number_of_cats, 15)

    def test_setter_property_correct_parameter(self):
        target = HauntedHouse("Apple Street 4.", 15)
        target.number_of_cats = 300
        self.assertEqual(target._number_of_cats, 300)

    def test_setter_property_incorrect_parameter(self):
        target = HauntedHouse("Apple Street 4.", 15)
        target.number_of_cats = 9
        self.assertEqual(target._number_of_cats, 10)

    def test_iadd_operator_incorrect_parameter(self):
        target = HauntedHouse("Apple Street 4.", 15)
        target.ghosts = []
        try:
            target += 3.14
        except Exception as e:
            self.assertEqual(str(e), "Not a ghost")
        self.assertEqual(target.ghosts, [])

    def test_iadd_operator_empty_list(self):
        target = HauntedHouse("Apple Street 4.", 15)
        target.ghosts = []
        target += "Bela"
        self.assertEqual(target.ghosts, [
            "Bela"])

    def test_iadd_operator_not_in_list(self):
        target = HauntedHouse("Apple Street 4.", 15)
        target.ghosts = ["Feri", "Peti"]
        target += "Bela"
        self.assertEqual(target.ghosts, ["Feri", "Peti",
                                         "Bela"])

    def test_iadd_operator_is_in_list(self):
        target = HauntedHouse("Apple Street 4.", 15)
        target.ghosts = ["Feri", "Bela", "Peti"]
        target += "Bela"
        self.assertEqual(target.ghosts, [
            "Feri", "Bela1", "Peti", "Bela2"])

    def test_str_operator_no_ghost(self):
        target = HauntedHouse("Banana Street 4.", 20)
        target.address = "Banana Street 4."
        target._number_of_cats = 20
        target.ghosts = []
        self.assertEqual(
            str(target), "The haunted house at Banana Street 4. has 20 cats, and no ghost haunts it")

    def test_str_operator_ghosts(self):
        target = HauntedHouse("Banana Street 4.", 20)
        target.address = "Banana Street 4."
        target._number_of_cats = 20
        target.ghosts = ["Bela", "Feri"]
        self.assertEqual(
            str(target), "The haunted house at Banana Street 4. has 20 cats, and 2 ghosts haunt it")

    def test_eq_operator(self):
        target1 = HauntedHouse("Banana Street 4.", 20)
        target1.address = "Banana Street 4."
        target1._number_of_cats = 20
        target1.ghosts = ["Bela", "Feri"]

        target2 = HauntedHouse("Banana Street 4.", 20)
        target2.address = "Banana Street 4."
        target2._number_of_cats = 20
        target2.ghosts = ["Albert"]

        target3 = HauntedHouse("Banana Street 4.", 21)
        target3.address = "Banana Street 4."
        target3._number_of_cats = 21
        target3.ghosts = ["Bela", "Feri"]

        self.assertTrue(target1 == target2)
        self.assertFalse(target1 == target3)


if __name__ == '__main__':
    unittest.main()
