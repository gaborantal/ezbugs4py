import unittest
from inspect import signature
from task import SurrealNumber


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(SurrealNumber.__init__).parameters), 3)

    def setUp(self):
        self.test_param1 = set()
        self.test_param2 = set()

        self.sn_instance1 = SurrealNumber(set(), set())
        self.sn_instance2 = SurrealNumber({self.sn_instance1}, set())
        self.sn_instance3 = SurrealNumber(set(), {self.sn_instance1})
        self.sn_bad_instance = SurrealNumber({self.sn_instance1},
                                             {self.sn_instance1})

    def test_init_with_correct_parameter_quantity(self):
        sn_instance = SurrealNumber(set(), set())
        self.assertEqual(sn_instance._left, self.test_param1)
        self.assertEqual(sn_instance._right, self.test_param2)

    def test_init_with_incorrect_parameters(self):
        with self.assertRaises(Exception) as context:
            sn_instance = SurrealNumber(list(), set())


    def test_init_with_zero_parameter(self):
        with self.assertRaises(Exception) as context:
            sn_instance = SurrealNumber()
        self.assertEqual(str(context.exception),
                         "SurrealNumber.__init__() missing 2 required positional arguments: "
                         "'left' and 'right'")

    def test_init_with_incorrect_parameter_quantity(self):
        with self.assertRaises(Exception) as context:
            sn_instance = SurrealNumber(self.test_param1, self.test_param2,
                                        set())
        self.assertEqual(str(context.exception),
                         "SurrealNumber.__init__() takes 3 positional arguments "
                         "but 4 were given")

    def test_setting_left_and_right_attributes(self):
        sn_instance = SurrealNumber(set(), set())
        self.assertEqual(sn_instance._right, set())
        self.assertEqual(sn_instance._left, set())

    def test_left_and_right_properties(self):
        sn_instance = SurrealNumber(set(), set())
        self.assertEqual(sn_instance.right, tuple())
        self.assertEqual(sn_instance.left, tuple())

    def test_function_str(self):
        self.assertEqual(self.sn_instance1.__str__(), '{|}')
        self.assertEqual(self.sn_instance2.__str__(), '{{|}|}')
        self.assertEqual(self.sn_instance3.__str__(), '{|{|}}')

    def test_function_le(self):
        self.assertTrue(self.sn_instance1.__le__(self.sn_instance1))
        self.assertTrue(self.sn_instance2.__le__(self.sn_instance2))
        self.assertTrue(self.sn_instance3.__le__(self.sn_instance3))

        self.assertFalse(self.sn_instance2.__le__(self.sn_instance1))
        self.assertFalse(self.sn_instance1.__le__(self.sn_instance3))
        self.assertFalse(self.sn_instance2.__le__(self.sn_instance3))

        self.assertTrue(self.sn_instance1.__le__(self.sn_instance2))
        self.assertTrue(self.sn_instance3.__le__(self.sn_instance1))
        self.assertTrue(self.sn_instance3.__le__(self.sn_instance2))

    def test_function_lt(self):
        self.assertFalse(self.sn_instance1.__lt__(self.sn_instance1))
        self.assertFalse(self.sn_instance2.__lt__(self.sn_instance2))
        self.assertFalse(self.sn_instance3.__lt__(self.sn_instance3))

        self.assertFalse(self.sn_instance2.__lt__(self.sn_instance1))
        self.assertFalse(self.sn_instance1.__lt__(self.sn_instance3))
        self.assertFalse(self.sn_instance2.__lt__(self.sn_instance3))

        self.assertTrue(self.sn_instance1.__lt__(self.sn_instance2))
        self.assertTrue(self.sn_instance3.__lt__(self.sn_instance1))
        self.assertTrue(self.sn_instance3.__lt__(self.sn_instance2))

    def test_function_check(self):
        self.assertTrue(self.sn_instance1.check())
        self.assertTrue(self.sn_instance2.check())
        self.assertFalse(self.sn_bad_instance.check())


if __name__ == "__main__":
    unittest.main()
