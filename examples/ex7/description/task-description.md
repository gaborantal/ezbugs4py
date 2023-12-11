- Create a class named `Convolution2D` designed for performing matrix operations.
- The class's constructor expects two matrices: an image matrix and a kernel matrix (both are 2-dimensional lists) containing integers in their cells.
    * Save these matrices into private attributes `_image` and `_kernel`.
    * Implement working getter and setter methods for `image` and `kernel`.
    * If the parameters are not Python lists, the constructor should raise a general exception with the message `Wrong Convolution2D!`.
    * Store the height and width of both the image and kernel matrices in attributes `_H`, `_W`, `_kh`, and `_kw`. These represent the image height, image width, kernel height, and kernel width, respectively. Two class functions, `compute_image_shape` and `compute_kernel_shape`, should be called within the constructor to calculate these values.
- The `compute_image_shape` function calculates and saves the image height and iterates through each row to check if it is a Python list. If two rows have different lengths or if a row is not of list type, the function should raise a general exception with the message `Wrong Convolution2D!`.
- The `compute_kernel_shape` function is similar to `compute_image_shape` but computes the values for `_kh` and `_kw`. Additionally, it ensures that the kernel is always square (height equals width) and has an odd height. In case of any error, it should raise a general exception with the message `Wrong Convolution2D!`.
- The class should implement a class function named `sum_numbers`, which adds up all values in the image and kernel matrices separately. The product of these sums is then calculated, and a new matrix, the size of the image, is created with each cell containing this product. The function should return the newly created matrix.
- Override the equality operator to return True only if the image and kernel heights and widths are all equal between two instances of the class.
- Override the method responsible for converting the class instance to a string, returning the specified text: `H,W x h,w: {_H},{_W} x {_kh},{_kw}`, where `{_H}`, `{_W}`, `{_kh}`, and `{_kw}` represent the previously mentioned height and width values.