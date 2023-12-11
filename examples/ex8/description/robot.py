import unittest
from inspect import signature
from random import shuffle

from task import PrettyPrint


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(PrettyPrint.__init__).parameters), 2)

    def setUp(self):
        self.test_param1 = "prefix"
        self.test_param2 = 1

    def test_init_with_correct_parameter_quantity(self):
        pp_instance1 = PrettyPrint(self.test_param1)
        self.assertEqual(pp_instance1._prefix, self.test_param1)
        pp_instance2 = PrettyPrint(self.test_param2)
        self.assertEqual(pp_instance2._prefix, self.test_param2)

    def test_init_with_zero_parameter(self):
        pp_instance = PrettyPrint()
        self.assertNotEqual(pp_instance._prefix, self.test_param1)
        self.assertNotEqual(pp_instance._prefix, self.test_param2)
        self.assertEqual(pp_instance._prefix, "")

    def test_init_with_incorrect_parameter_quantity(self):
        with self.assertRaises(Exception) as context:
            pp_instance = PrettyPrint(self.test_param1, self.test_param2)
        self.assertEqual(str(context.exception),
                         "PrettyPrint.__init__() takes from 1 to 2 positional arguments "
                         "but 3 were given")

    def test_prefix_set_up(self):
        pp_instance = PrettyPrint(self.test_param1)
        self.assertEqual(pp_instance._prefix, self.test_param1)

    def test_prefix_getter_works(self):
        pp_instance = PrettyPrint(self.test_param1)
        self.assertEqual(pp_instance.prefix, self.test_param1)

    def test_prefix_setter_works(self):
        pp_instance = PrettyPrint(self.test_param1)
        self.assertEqual(pp_instance.prefix, self.test_param1)
        pp_instance.prefix = self.test_param2
        self.assertEqual(pp_instance.prefix, self.test_param2)

    def test_prefix_setter_exists(self):
        pp_instance = PrettyPrint(42)
        self.assertFalse(callable(getattr(pp_instance, 'prefix')))
        self.assertTrue(hasattr(pp_instance.__class__, 'prefix'))
        self.assertTrue(
            isinstance(getattr(pp_instance.__class__, 'prefix'),
                       property))
        self.assertTrue(
            hasattr(getattr(pp_instance.__class__, 'prefix'), 'setter'))

    def test_get_function_exists(self):
        pp_instance = PrettyPrint("pref")
        self.assertTrue(hasattr(pp_instance, 'get'))
        self.assertTrue(callable(getattr(pp_instance, 'get')))

    def test_get_prefixed_functions_exist(self):
        types = ["NoneType", "int", "float", "str", "list", "dict"]
        pp_instance = PrettyPrint("pref")
        for t in types:
            self.assertTrue(hasattr(pp_instance, 'get_' + t))
            self.assertTrue(callable(getattr(pp_instance, 'get_' + t)))

    def test_get_function_on_numerous_parameters(self):
        random_data = [
            None,
            -34,
            3.14,
            45.2,
            "words",
            "text",
            [4, 5, 6],
            [None],
            {'a': 1, 'b': 'str'},
            {None: "none", 13.3: 3},
            Exception("helo"),
            (34, "abc")]
        shuffle(random_data)

        # Same function on same element returns the same value
        for element in random_data:
            pp_instance1 = PrettyPrint("__start__")
            pp_instance2 = PrettyPrint("__start__")
            self.assertEqual(pp_instance1.get(element), pp_instance2.get(
                element))

        # Same function on different element does not returns the same value
        for element in random_data:
            pp_instance1 = PrettyPrint("__start__")
            pp_instance2 = PrettyPrint("__start__")
            clamped_index = max(0, min(random_data.index(
                element), len(random_data) - 1))

            if pp_instance1.get(element) != pp_instance2.get(
                    random_data[clamped_index]):
                self.assertNotEqual(pp_instance1.get(element),
                                    pp_instance2.get(
                                        random_data[clamped_index]))


if __name__ == "__main__":
    unittest.main()
