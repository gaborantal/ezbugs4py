import unittest
import random
from inspect import signature
from task import Convolution2D


class TestRobot(unittest.TestCase):

    def test_init_param_count(self):
        self.assertEqual(len(signature(Convolution2D.__init__).parameters), 3)

    def test_init(self):
        with self.assertRaises(Exception):
            Convolution2D(None, None)
        with self.assertRaises(Exception):
            Convolution2D([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0], [0, 0]])

    def test_image(self):
        obj = Convolution2D([[1, 2, 3], [2, 2, 0], [0, 1, 3]], [[2]])
        self.assertEqual(obj._image, [[1, 2, 3], [2, 2, 0], [0, 1, 3]])
        self.assertEqual(obj.image, [[1, 2, 3], [2, 2, 0], [0, 1, 3]])
        obj.image = [[1, 2, 3], [2, 2, 3], [1, 1, 1]]
        self.assertEqual(obj.image, [[1, 2, 3], [2, 2, 3], [1, 1, 1]])

    def test_kernel(self):
        obj = Convolution2D([[1, 2, 3], [2, 2, 0], [0, 1, 3]], [[2]])
        self.assertEqual(obj._kernel, [[2]])
        self.assertEqual(obj.kernel, [[2]])
        obj.kernel = [[3]]
        self.assertEqual(obj.kernel, [[3]])

    def test_methods(self):
        self.assertTrue(hasattr(Convolution2D, 'compute_image_shape'))
        self.assertTrue(hasattr(Convolution2D, 'compute_kernel_shape'))
        self.assertTrue(hasattr(Convolution2D, 'sum_numbers'))
        self.assertTrue(hasattr(Convolution2D, '__eq__'))
        self.assertTrue(hasattr(Convolution2D, '__str__'))

    def test_lots(self):
        i = 0
        for H in range(7, 10):
            W = H
            for kh in [1, 3]:
                kw = kh
                image = [[0] * W for _ in range(H)]
                si = 0
                for y in range(H):
                    for x in range(W):
                        temp = random.randint(0, 10)
                        image[y][x] = temp
                        si += temp

                kernel = [[0] * kw for _ in range(kh)]
                sk = 0
                for y in range(kh):
                    for x in range(kw):
                        temp = random.randint(-2, 2)
                        kernel[y][x] = temp
                        sk += temp

                res_img = [[si * sk] * W] * H
                i += 1

                obj = Convolution2D(image, kernel)
                self.assertEqual(obj.sum_numbers(), res_img)

                obj2 = Convolution2D(image, kernel)
                self.assertTrue(obj.__eq__(obj2))

                obj3 = Convolution2D(image, [[0] * 7] * 7)
                self.assertFalse(obj.__eq__(obj3))

                obj4 = Convolution2D([[0]], kernel)
                self.assertFalse(obj.__eq__(obj4))

                obj5 = Convolution2D([[0]], kernel)
                self.assertFalse(obj5.__eq__([3, 4]))

                self.assertEqual(str(obj), f"H,W x h,w: {H},{W} x {kh},{kw}")


if __name__ == "__main__":
    unittest.main()
