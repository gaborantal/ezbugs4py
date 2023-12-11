class Convolution2D(object):
    def __init__(self, _image=None, _kernel=None):
        if _image is None:
            _image = [[], []]
        if _kernel is None:
            _kernel = [[], []]
        self._image = _image
        self._kernel = _kernel


    _kh = 0
    _kw = 0
    _H = 0
    _W = 0

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, paramList):
        if isinstance(paramList, list):
            self._image = paramList
            _H = paramList[0]
            _W = paramList[1]
        else:
            raise Exception("Wrong Convolution2D!")

    @property
    def kernel(self):
        return self._kernel

    @kernel.setter
    def kernel(self, paramList):
        if isinstance(paramList, list):
            self._kernel = paramList
            _kh = paramList[0]
            _kw = paramList[1]
        else:
            raise Exception("Wrong Convolution2D!")

    def compute_image_shape(self):
        for adat in self._image:
            if not isinstance(adat, list):
                raise Exception("Wrong Convolution2D!")
        return len(self._image)

    def compute_kernel_shape(self):
        for adat in self._kernel:
            if not isinstance(adat, list) and self._kw != self._kh and self._kh % 2 != 0:
                raise Exception("Wrong Convolution2D!")
        return len(self._kernel)

    def sum_numbers(self):
        return self._kw + self._kh + self._W + self._H

    def __eq__(self, other):
        if isinstance(other, Convolution2D):
            if self._kh == other._kh and self._kw == other._kw and self._H == other.H and self._W == other._W:
                return True
            else:
                return False

    def __str__(self):
        return f"H,W x h,w: {self._H},{self._W} x {self._kh},{self._kw} , ahogy a {self._H} , {self._W} , {self._kh} , {self._kw}"