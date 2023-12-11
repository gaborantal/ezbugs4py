def k_combination(N, K):
    if N > 0 and K > 0 and N > K and isinstance(N, (int)) and isinstance(K, (
    int)):
        N_fact = 1
        K_fact = 1
        NK_fact = 1
        result = 0
        for i in range(2, (N + 1)):
            N_fact = N_fact * i
        for i in range(2, (K + 1)):
            K_fact = K_fact * i
        for i in range(2, ((N - K) + 1)):
            NK_fact = NK_fact * i
        result = N_fact / (K_fact * NK_fact)
    else:
        return 0

    return result


class Convolution2D(object):
    def __init__(self, image, kernel):
        self._image = image
        self._kernel = kernel

    @property
    def image(self):
        return self._image

    @property
    def kernel(self):
        return self._kernel

    @image.setter
    def image(self, image):
        if isinstance(image, (int)):
            self._image = image

    @kernel.setter
    def kernel(self, kernel):
        if isinstance(kernel, (int)):
            self._kernel = kernel

    def compute_image_shape(self, image, kernel):
        for i in image:
            H = i

    def compute_kernel_shape(self, image, kernel):
        for i in image:
            W = i

    def __str__(self):
        return f"H,W x h,w: {_H},{_W} x {_kh},{_kw}, as " \
               f"{_H}, {_W}, {_kh}, {_kw} are the above mentioned width and " \
               f"height values."


class WrongConvolution2D(object):
    def __init__(self, message):
        self.message = message
