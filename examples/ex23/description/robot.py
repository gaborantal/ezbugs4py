import unittest
from inspect import signature
from task import Cemetery


class TestRobot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            Cemetery("MainCemetery", 500)
        except AttributeError:
            cls.fail("No class!")
        except TypeError:
            cls.fail("Bad constructor!")
        except RecursionError:
            cls.fail("Infinite loop!")

    def test_init_param_count(self):
        self.assertEqual(len(signature(Cemetery.__init__).parameters), 3)

    def test_fields(self):
        target = Cemetery("MainCemetery", 500)
        self.assertEqual(target.name, 'MainCemetery')
        self.assertEqual(target._number_of_graves, 500)
        self.assertEqual(target.ghosts, list())

    def test_init_number_of_graves(self):
        target = Cemetery("MainCemetery", 9)
        self.assertEqual(target.number_of_graves, 10)

    def test_getter_property(self):
        target = Cemetery("MainCemetery", 500)
        self.assertEqual(target.number_of_graves, 500)

    def test_setter_property_correct_parameter(self):
        target = Cemetery("MainCemetery", 500)
        target.number_of_graves = 300
        self.assertEqual(target._number_of_graves, 300)

    def test_setter_property_incorrect_parameter(self):
        target = Cemetery("MainCemetery", 500)
        target.number_of_graves = 9
        self.assertEqual(target._number_of_graves, 10)

    def test_iadd_incorrect_parameter(self):
        target = Cemetery("MainCemetery", 500)
        target.ghosts = []
        try:
            target += 3.14
        except Exception as e:
            self.assertEqual(str(e), "Not a ghost")
        self.assertEqual(target.ghosts, [])

    def test_iadd_empty_list(self):
        target = Cemetery("MainCemetery", 500)
        target.ghosts = []
        target += "Bela"
        self.assertEqual(target.ghosts, ["Bela"])

    def test_iadd_not_in_list(self):
        target = Cemetery("MainCemetery", 500)
        target.ghosts = ["Feri", "Peti"]
        target += "Bela"
        self.assertEqual(target.ghosts, ["Feri", "Peti", "Bela"])

    def test_iadd_in_list(self):
        target = Cemetery("MainCemetery", 500)
        target.ghosts = ["Feri", "Bela", "Peti"]
        target += "Bela"
        self.assertEqual(target.ghosts, ["Feri", "Bela1", "Peti", "Bela2"])

    def test_str_operator_no_ghost(self):
        target = Cemetery("MainCemetery", 200)
        target.name = "MainCemetery"
        target._number_of_graves = 200
        target.ghosts = []

        self.assertEqual(
            str(target), "In the MainCemetery cemetery, there are 200 graves, and no ghosts haunt it")

    def test_str_operator_ghosts(self):
        target = Cemetery("MainCemetery", 200)
        target.name = "MainCemetery"
        target._number_of_graves = 200
        target.ghosts = ["Bela", "Feri"]

        self.assertEqual(
            str(target), "In the MainCemetery cemetery, there are 200 graves, and 2 ghosts haunt it")

    def test_eq_operator(self):
        target1 = Cemetery("MainCemetery", 200)
        target1.name = "MainCemetery"
        target1._number_of_graves = 200
        target1.ghosts = ["Bela", "Feri"]

        target2 = Cemetery("MainCemetery", 200)
        target2.name = "MainCemetery"
        target2._number_of_graves = 200
        target2.ghosts = ["Albert"]

        target3 = Cemetery("MainCemetery", 201)
        target3.name = "MainCemetery"
        target3._number_of_graves = 201
        target3.ghosts = ["Bela", "Feri"]

        self.assertTrue(target1 == target2)
        self.assertFalse(target1 == target3)


if __name__ == '__main__':
    unittest.main()
