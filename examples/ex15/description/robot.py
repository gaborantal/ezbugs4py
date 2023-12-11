import unittest
import task

class TestLengthStat(unittest.TestCase):
    def test_empty_string_param(self):
        """Test with an empty string parameter."""
        self.assertEqual(task.length_stat(''), [])

    def test_invalid_type_param(self):
        """Test with a non-string type parameter."""
        self.assertEqual(task.length_stat(42), [])

    def test_one_word_param(self):
        """Test with a one-word text."""
        self.assertEqual(task.length_stat('kutyamutya'), [10, 0])

    def test_multiple_words_same_length(self):
        """Test with a multi-word text (words of the same length)."""
        self.assertEqual(task.length_stat('asd foo bar bla bla bla'), [3, 0])

    def test_multiple_words_and_length_1(self):
        """Test with a multi-word text, varying word lengths (1)."""
        self.assertEqual(task.length_stat('I will max out the first test'), [3, 3])

    def test_multiple_words_and_length_2(self):
        """Test with a multi-word text, varying word lengths (2)."""
        self.assertEqual(task.length_stat('Never gonna give you up Never gonna let you down Never gonna run around And desert you'), [4, 8])

    def test_multiple_words_and_length_3(self):
        """Test with a multi-word text, varying word lengths (3)."""
        self.assertEqual(task.length_stat('Somebody once told meg The world is gonna roll me I aint the sharpest tool in the shed She was looking kinda dumb With her finger and her thumb In the shape of an L on her forehead'), [3, 18])

    def test_multiple_words_and_length_4(self):
        """Test with a multi-word text, varying word lengths (4)."""
        self.assertEqual(task.length_stat('Short texttt'), [5, 1])

    def test_multiple_words_and_length_5(self):
        """Test with a multi-word text, varying word lengths (5)."""
        self.assertEqual(task.length_stat('There should be another testcase, maybe it is worth to search for a longer text'), [4, 8])

    def test_super_long_text(self):
        """Test with an especially long text, varying word lengths."""
        self.assertEqual(task.length_stat('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget nibh nisi. Nam lobortis ullamcorper dolor, eget finibus neque ultricies ac. Nunc consectetur lacinia nisi, ac pretium nibh faucibus ut. Duis nec lacus ut neque feugiat gravida. Duis urna ante, egestas consequat nibh eu, volutpat luctus orci. Suspendisse feugiat suscipit sapien vel sollicitudin. Curabitur ultrices ipsum orci, at lacinia massa ultrices vel. Vivamus tristique augue sit amet mauris placerat iaculis. Integer tincidunt, lacus eu ullamcorper ornare, arcu libero tincidunt arcu, at vestibulum velit nibh at nulla. Quisque volutpat condimentum ornare.'), [6, 38])

if __name__ == "__main__":
    unittest.main()
