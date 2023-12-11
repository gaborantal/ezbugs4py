import unittest
import task

class TestWordStatistics(unittest.TestCase):
    
    def test_non_string_input(self):
        self.assertEqual(task.word_statistics(12345), {}, "Should handle non-string input")

    def test_empty_string(self):
        self.assertEqual(task.word_statistics(''), {}, "Should handle empty string")

    def test_single_word(self):
        self.assertEqual(task.word_statistics('Kutyamutya'), {}, "Should handle a single-word string")

    def test_same_length_words(self):
        self.assertEqual(task.word_statistics('gamma delta theta omega'), {'number_of_words': 4, 'average_length': 5, 'long_words': 0})

    def test_mixed_length_words_case1(self):
        self.assertEqual(task.word_statistics('Scripts Languages counts as an easy subject!'), {'number_of_words': 7, 'average_length': 5, 'long_words': 4})

    def test_mixed_length_words_case2(self):
        self.assertEqual(task.word_statistics('Somebody once told meg The world is gonna roll me I aint the sharpest tool in the shed She was looking kinda dumb With her finger and her thumb In the shape of an L on her forehead'),
                         {'number_of_words': 38, 'average_length': 3, 'long_words': 18})

    def test_mixed_length_words_case3(self):
        self.assertEqual(task.word_statistics('Short text'), {'number_of_words': 2, 'average_length': 4, 'long_words': 1})

    def test_mixed_length_words_case4(self):
        self.assertEqual(task.word_statistics('It would be necessary to write two test cases, perhaps a very long text would also be worthwhile'),
                         {'number_of_words': 18, 'average_length': 4, 'long_words': 7})

    def test_mixed_length_words_case5(self):
        self.assertEqual(task.word_statistics('A Rindfleischetikettierungsuberwachungsaufgabenubertragungsgesetz is a long german word'),
                         {'number_of_words': 7, 'average_length': 11, 'long_words': 1})

    def test_very_long_text(self):
        self.assertEqual(task.word_statistics('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget nibh nisi. Nam lobortis ullamcorper dolor, eget finibus neque ultricies ac. Nunc consectetur lacinia nisi, ac pretium nibh faucibus ut. Duis nec lacus ut neque feugiat gravida. Duis urna ante, egestas consequat nibh eu, volutpat luctus orci. Suspendisse feugiat suscipit sapien vel sollicitudin. Curabitur ultrices ipsum orci, at lacinia massa ultrices vel. Vivamus tristique augue sit amet mauris placerat iaculis. Integer tincidunt, lacus eu ullamcorper ornare, arcu libero tincidunt arcu, at vestibulum velit nibh at nulla. Quisque volutpat condimentum ornare.'),
                         {'number_of_words': 90, 'average_length': 6, 'long_words': 38})

if __name__ == "__main__":
    unittest.main()
