import unittest
from inspect import signature
from task import Clustering


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(Clustering.__init__).parameters), 2)

    def setUp(self):
        self.test_param1 = "Cool"
        self.test_param2 = 1

    def test_init_with_correct_parameter_quantity(self):
        cluster_instance = Clustering("Cool")
        self.assertEqual(cluster_instance._algorithm, self.test_param1)
        self.assertNotEqual(cluster_instance._algorithm, self.test_param2)

    def test_init_with_zero_parameter(self):
        with self.assertRaises(Exception) as context:
            cluster_instance = Clustering()
        self.assertEqual(str(context.exception),
                         "Clustering.__init__() missing 1 required positional "
                         "argument: 'name'")

    def test_init_with_incorrect_parameter_quantity(self):
        with self.assertRaises(Exception) as context:
            cluster_instance = Clustering(self.test_param1, self.test_param2)
        self.assertEqual(str(context.exception),
                         "Clustering.__init__() takes 2 positional arguments but 3 "
                         "were given")

    def test_setting_algorithm_attribute(self):
        cluster_instance = Clustering("Cool")
        self.assertNotEqual(cluster_instance._algorithm, "")
        self.assertEqual(cluster_instance._algorithm, "Cool")

    def test_algorithm_property(self):
        cluster_instance = Clustering("Cool")
        self.assertNotEqual(cluster_instance.algorithm, "")
        self.assertEqual(cluster_instance.algorithm, '"Cool" algorithm')

    def test_function_put_into(self):
        cluster_instance = Clustering("Cool")
        self.assertTrue(cluster_instance.put_into("apple", "fruit"))
        self.assertTrue(cluster_instance.put_into("pear", "fruit"))
        self.assertTrue(cluster_instance.put_into("carrot", 12))
        self.assertFalse(cluster_instance.put_into("apple", "fruit"))

    def test_function_str(self):
        cluster_instance = Clustering("Cool")

        self.assertEqual(cluster_instance.__str__(),
                         '0 items in 0 clusters detected with '
                         '"Cool" algorithm')
        self.assertTrue(cluster_instance.put_into("celery", 12))
        self.assertEqual(cluster_instance.__str__(),
                         '1 items in 1 clusters detected with '
                         '"Cool" algorithm')
        self.assertTrue(cluster_instance.put_into("apple", 3))
        self.assertTrue(cluster_instance.put_into("pear", "fruit"))
        self.assertEqual(cluster_instance.__str__(),
                         '3 items in 3 clusters detected with "'
                         'Cool" algorithm')

    def test_function_cluster_count(self):
        cluster_instance = Clustering("Cool")
        self.assertEqual(cluster_instance.cluster_count, 0)

        self.assertTrue(cluster_instance.put_into("celery", 12))
        self.assertTrue(cluster_instance.put_into("apple", 3))
        self.assertTrue(cluster_instance.put_into("pear", "fruit"))

        self.assertEqual(cluster_instance.cluster_count, 3)
        self.assertFalse(cluster_instance.put_into("pear", 12))
        self.assertEqual(cluster_instance.cluster_count, 2)

    def test_function_count_of(self):
        cluster_instance = Clustering("Cool")
        self.assertTrue(cluster_instance.put_into("celery", 12))
        self.assertTrue(cluster_instance.put_into("apple", 3))
        self.assertTrue(cluster_instance.put_into("pear", "fruit"))
        self.assertTrue(cluster_instance.put_into("melon", "fruit"))

        self.assertEqual(cluster_instance.count_of("fruit"), 2)
        self.assertEqual(cluster_instance.count_of(12), 1)
        self.assertEqual(cluster_instance.count_of("new"), 0)


if __name__ == "__main__":
    unittest.main()
