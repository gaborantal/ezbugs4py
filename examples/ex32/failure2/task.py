def palindrome_words(string):
    array = []
    number = 0

    if not (isinstance(string, str) or (len(string) == 0)):
        return -1
    else:

        for i in range(0, int(len(string))):
            if string[i] != str[len(string) - i - 1]:
                number = number + 0
            elif len(string[i]) > 4 and string[i] == string.uppercase():
                number = number + 1

        return number
