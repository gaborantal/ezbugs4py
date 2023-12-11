class Convolution2D:
    def __init__(self, image, kernel):
        self._image = image
        self._kernel = kernel

        if not isinstance(image, list) or not isinstance(kernel, list):
            raise Exception("Wrong Convolution2D!")

        self._H = 0
        self._W = 0
        self._kh = 0
        self._kw = 0

        self.compute_image_shape()
        self.compute_kernel_shape()

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if not isinstance(image, list):
            raise Exception("Wrong Convolution2D!")
        self._image = image
        self.compute_image_shape()

    @property
    def kernel(self):
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        if not isinstance(kernel, list):
            raise Exception("Wrong Convolution2D!")
        self._kernel = kernel
        self.compute_kernel_shape()

    def compute_image_shape(self):
        self._H = len(self._image)
        if not isinstance(self._image, list):
            raise Exception("Wrong Convolution2D!")
        for row in self._image:
            if not isinstance(row, list):
                raise Exception("Wrong Convolution2D!")

            if self._W == 0:
                self._W = len(row)

            if self._W != len(row):
                raise Exception("Wrong Convolution2D!")

    def compute_kernel_shape(self):
        self._kh = len(self._kernel)
        if not isinstance(self._kernel, list):
            raise Exception("Wrong Convolution2D!")
        for row in self._kernel:
            if not isinstance(row, list):
                raise Exception("Wrong Convolution2D!")

            if self._kw == 0:
                self._kw = len(row)

            if self._kw != len(row):
                raise Exception("Wrong Convolution2D!")

        if self._kw != self._kh or self._kw % 2 == 0:
            raise Exception("Wrong Convolution2D!")

    def sum_numbers(self):
        result = [[0] * self._W for _ in range(self._H)]

        s = 0
        for y in range(self._H):
            for x in range(self._W):
                s += self._image[y][x]
        k = 0
        for y in range(self._kh):
            for x in range(self._kw):
                k += self._kernel[y][x]

        for y in range(self._H):
            for x in range(self._W):
                result[y][x] = s * k

        return result

    def __str__(self):
        return f"H,W x h,w: {self._H},{self._W} x {self._kh},{self._kw}"

    def __eq__(self, other):
        if not isinstance(other, Convolution2D):
            return False
        return self._H == other._H and self._W == other._W and self._kh == other._kh and self._kw == other._kw
