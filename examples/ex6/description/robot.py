import unittest
from inspect import signature
from task import Hypercube


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(Hypercube.__init__).parameters), 3)

    def setUp(self):
        self.hypercube = Hypercube(10, 10)

    def test_init(self):
        with self.assertRaises(Exception):
            Hypercube(-1, 1)
        with self.assertRaises(Exception):
            Hypercube(1, -1)

    def test_dimension(self):
        self.assertEqual(self.hypercube.dimension, 10)
        self.hypercube.dimension = 12
        self.assertEqual(self.hypercube.dimension, 12)

    def test_length(self):
        self.assertEqual(self.hypercube.length, 10)
        self.hypercube.length = 12
        self.assertEqual(self.hypercube.length, 12)

    def test_eq(self):
        self.assertFalse(self.hypercube.__eq__("Alma"))

    def test_methods_exist(self):
        self.assertTrue(hasattr(self.hypercube, 'get_no_vertex'))
        self.assertTrue(hasattr(self.hypercube, 'get_no_edge'))
        self.assertTrue(hasattr(self.hypercube, 'get_no_face'))
        self.assertTrue(hasattr(self.hypercube, 'get_area'))
        self.assertTrue(hasattr(self.hypercube, '__eq__'))
        self.assertTrue(hasattr(self.hypercube, '__str__'))

    def test_hypercube_methods(self):

        def _no_vertex(dim):
            return 2 ** dim

        def _no_edge(dim):
            if dim < 1:
                return 0
            return dim * 2 ** (dim - 1)

        def _no_face(dim):
            # 2**(dim-2)*(n! / (2!*(n-2)!))
            def factorial(n):
                s = 1
                for i in range(1, n + 1):
                    s *= i
                return s

            if dim < 2:
                return 0

            return 2 ** (dim - 2) * factorial(dim) / (2 * factorial(dim - 2))

        def _area(dim, length):
            return length ** dim

        l = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        random_list = [1] + l[:2]
        for i in random_list:
            dim = i
            length = (i + 1) * 2
            try:
                obj = Hypercube(dim, length)
            except Exception as e:
                self.fail(f"Hypercube initialization failed with dimensions: {dim}, length: {length}")

            self.assertEqual(obj.get_no_vertex(), _no_vertex(dim))
            self.assertEqual(obj.get_no_edge(), _no_edge(dim))
            self.assertEqual(obj.get_no_face(), _no_face(dim))
            self.assertEqual(obj.__eq__(obj), True)

            obj2 = Hypercube(dim + 1, length)
            self.assertEqual(obj.__eq__(obj2), False)

            obj3 = Hypercube(dim, length + 1)
            self.assertEqual(obj.__eq__(obj3), False)

            self.assertEqual(obj.get_no_face(), _no_face(dim))
            self.assertEqual(obj.__str__(), f"Dim: {dim}, Len: {length}, Area: {_area(dim, length)}")


if __name__ == "__main__":
    unittest.main()
