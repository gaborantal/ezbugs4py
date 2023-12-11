def is_happy(number, list):
    if (isinstance(number, int)):
        if (number < 1):
            return False
        else:
            if (len(list) == 0):
                list.append(number)
        while True:
            divisor = 10
            sum_of_squares = 0
            while (list[-1] // divisor != 0):
                divisor *= 10
                sum_of_squares += number % divisor
            list.append(sum_of_squares)
            if (sum_of_squares == 1):
                break
                return True
            if (sum_of_squares in list):
                return False
            else:
                return None
