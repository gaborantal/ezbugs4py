class Convolution2D(object):

    def __init__(self, image, kernel):
        self._image = image
        self._kernel = kernel

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if isinstance(image, list):
            _H = self.compute_image_shape(image)
            _W = self.compute_image_shape(image)
        else:
            raise Exception("Wrong Convolution2D!")

    @property
    def kernel(self):
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        if isinstance(kernel, list):
            _kh = self.compute_kernel_shape(kernel)
            _kw = self.compute_kernel_shape(kernel)
        else:
            raise Exception("Wrong Convolution2D!")

    def sum_numbers(self):
        return self.kernel * self.image

    def __eq__(self, k):
        if isinstance(k, self.kernel):
                if (self._H == k._kh and self._W == k._kw):
                    return True
                else:
                    return False

    def __str__(self):
        return f"H,W x h,w: {self._H},{self._W} x {self._kh},{self._kw}"

    def compute_image_shape(self):
        ilen = len(self.image)
        w = 0
        for i in len(self.image):
            if ilen != len(self.image):
                raise Exception("Wrong Convolution2D!")
            for j in range(len(self.image[i])):
                w = w + 1;
            else:
                self._H = len(self.image)
                self._W = w

    def compute_kernel_shape(self):
        ikern = len(self.kernel)
        w = 0
        for i in len(self.kernel):
            if ikern != len(self.kernel):
                raise Exception("Wrong Convolution2D!")
            for j in range(len(self.kernel[i])):
                w = w + 1;
        else:
                self._kh = len(self.kernel)
                self._kw = w
