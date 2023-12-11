import unittest
import task


class TestAlliteration(unittest.TestCase):

    def test_empty_string_parameter(self):
        """Test with an empty string parameter."""
        self.assertIsNone(task.alliteration(''))

    def test_invalid_parameter_type(self):
        """Test with a non-string type parameter."""
        self.assertIsNone(task.alliteration(100))

    def test_one_word_text(self):
        """Test with a one-word text."""
        self.assertIsNone(task.alliteration('carrot'))

    def test_two_word_text(self):
        """Test with a two-word text."""
        self.assertEqual(task.alliteration('Python ZH'), 1)

    def test_two_word_case(self):
        """Test with a two-word text."""
        self.assertEqual(task.alliteration('MA Makes maCAron'), 3)

    def test_multiple_word_text_5(self):
        """Test with a multi-word text (5 words)."""
        self.assertEqual(task.alliteration('minden macska most megy mosni'), 5)

    def test_multiple_word_text_3(self):
        """Test with a multi-word text (3 words)."""
        self.assertEqual(task.alliteration('Robi, Roli regi haverok'), 3)

    def test_multiple_word_text_6(self):
        """Test with a multi-word text (6 words)."""
        self.assertEqual(task.alliteration('Bekescsaba, Budapest, Baja, Belapatfalva, Berettyoujfalu, Balatonalmadi'), 6)

    def test_multiple_word_text_5_2(self):
        """Test with a multi-word text (5 words)."""
        self.assertEqual(task.alliteration('Szegeden szabad venni szeget, szemet szemert, szeget szegert'), 5)

    def test_multiple_word_text_3_2(self):
        """Test with a multi-word text (3 words)."""
        self.assertEqual(task.alliteration('Karoly kozepiskolas koraban sem kodolt kivaloan Kotlinban'), 3)

    def test_especially_long_text(self):
        """Test with an especially long text."""
        self.assertEqual(task.alliteration('Pannonia panzio penteki programja: Piri pankot pirit, Piroska petrezselymet perzsel, pimasz peneszt Patrik pusztitja, pesti pityokat Pongrac pucolja. Pompas pava parkban porog, Picurka papagaj polcon pihen. Pata patakba pattan, Palmaval pancsolni. Pecas pisztrangot perdit Peter penzet pazarolja. Pultos, pecsenyet, paprikast, pecsi palinkat poharba. Parom, puszillak.'), 45)


if __name__ == "__main__":
    unittest.main()
