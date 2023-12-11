import unittest
from inspect import signature
from task import palindrome_words


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(palindrome_words).parameters), 1)

    def test_function_on_number_input(self):
        self.assertNotEqual(palindrome_words(3355445533), 3355445533)
        self.assertEqual(palindrome_words(12345), -1)

    def test_function_on_empty_string_parameter(self):
        self.assertNotEqual(palindrome_words(""), "")
        self.assertEqual(palindrome_words(""), -1)

    def test_function_on_no_word_is_palindrome(self):
        self.assertEqual(palindrome_words("snowball,SCRIPT,"
                                          "mathiseasysubject,thisuni"), 0)
        self.assertEqual(palindrome_words("carrot"), 0)

    def test_function_on_every_word_is_palindrome(self):
        self.assertEqual(palindrome_words("RADAR,KAYAK,CIVIC,LEVEL,ROTOR"), 5)
        self.assertEqual(palindrome_words("RADAR,KAYAK,CIVIC,LEVEL"), 4)
        self.assertEqual(palindrome_words("RADAR"), 1)

    def test_function_on_three_letter_palindromes(self):
        self.assertEqual(palindrome_words("ABA,KAYAK,CIVIC,BOB,ROTOR"), 3)
        self.assertEqual(palindrome_words("ABA,BOB"), 0)
        self.assertEqual(palindrome_words("KAYAK,ABA"), 1)
        self.assertEqual(palindrome_words("DEED,NOON,BOB,ROTOR,REFER"), 4)

    def test_function_on_lower_case_characters(self):
        self.assertEqual(palindrome_words("DEEd,NOON,BOB,ROTOR,REFER"), 3)
        self.assertEqual(palindrome_words("ABA,kayak,CIVIC,BOB,ROTOR"), 2)
        self.assertEqual(palindrome_words("aba"), 0)
        self.assertEqual(palindrome_words("KAYAk,ABA"), 0)

    def test_function_on_mixed_quality_words(self):
        self.assertEqual(palindrome_words("DEEd,pool,AbA,,REFER"), 1)
        self.assertEqual(palindrome_words("Deep,LEVEL,CIVIC,bob,rotor"), 2)
        self.assertEqual(palindrome_words("aba,MADAM"), 1)
        self.assertEqual(palindrome_words("KAYAK,FRUIT"), 1)


if __name__ == "__main__":
    unittest.main()
