import unittest
from inspect import signature
from task import swap


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(swap).parameters), 2)

    def test_function_on_empty_parameters(self):
        self.assertEqual(swap("", {}), "")
        self.assertEqual(swap("", {2: "blue"}), "")
        self.assertEqual(swap("apple", {}), "apple")

    def test_function_on_plain_text(self):
        self.assertEqual(swap("This is plain téxt",
                              {"is": "as", "this": "that", "text": "text",
                               "pl": "in"}), "that-plain-text")

    def test_function_on_accented_sentence(self):
        self.assertEqual(swap("Im wrïting ācçents", {"writing": "reading"}),
                         "reading-accents")

    def test_function_on_accented_letters(self):
        self.assertEqual(swap("çéïàôñçéïñā", {}), "ceiaonceina")

    def test_function_on_short_word_sentence(self):
        self.assertEqual(swap("The big cat ran and hid", {}), "")

    def test_function_on_mixed_word_sentence(self):
        self.assertEqual(swap("Thïs àll is a téxt", {}), "this-text")

    def test_function_swap_feature(self):
        self.assertEqual(swap("Is this right-y?", {"-", " "}), "this-right-y?")


if __name__ == "__main__":
    unittest.main()
