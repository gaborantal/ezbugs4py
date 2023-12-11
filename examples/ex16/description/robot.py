import unittest
import task

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.film = task.Film("Harry Potter and the Prisoner of Azkaban", 142)
        self.film_long = task.Film("Harry Potter and the Prisoner of Azkaban", 142)
        self.film_short = task.Film("One-hour Cat Documentary", 60)
        self.film_same_length = task.Film("Harry Potter and the Prisoner of Azkaban", 60)
        self.non_film = "This is not a film"

    def test_init_with_all_parameters(self):
        self.assertEqual(self.film._title, "Harry Potter and the Prisoner of Azkaban")
        self.assertEqual(self.film.length, 142)
        self.assertEqual(self.film.ratings, [])

    def test_init_without_length_parameter(self):
        film = task.Film('One-hour Cat Documentary')
        self.assertEqual(film.length, 60)

    def test_title_property_get_and_set(self):
        self.assertEqual(self.film.title, "Harry Potter and the Prisoner of Azkaban")
        self.film.title = "Harry Potter 2"
        self.assertEqual(self.film.title, "Harry Potter 2")
        self.film.title = 42  # Should not change the title because it's not a string
        self.assertEqual(self.film.title, "Harry Potter 2")

    def test_add_rating_valid(self):
        self.film.add_rating(10.0)
        self.assertIn(10.0, self.film.ratings)
        self.film.add_rating(7.0)
        self.assertIn(7.0, self.film.ratings)
        self.film.add_rating(1.0)
        self.assertIn(1.0, self.film.ratings)

    def test_add_rating_invalid_high(self):
        with self.assertRaises(Exception) as context:
            self.film.add_rating(999.0)
        self.assertTrue('Invalid rating' in str(context.exception))

    def test_add_rating_invalid_low(self):
        with self.assertRaises(Exception) as context:
            self.film.add_rating(0.0)
        self.assertTrue('Invalid rating' in str(context.exception))

    def test_add_rating_invalid_type(self):
        with self.assertRaises(Exception) as context:
            self.film.add_rating("eight point zero")
        self.assertTrue('Invalid rating' in str(context.exception))

    def test_greater_than_operator(self):
        """Test the > operator."""
        self.assertTrue(self.film_long > self.film_short, "The current film is longer")
        self.film_long.length = 30
        self.assertFalse(self.film_long > self.film_short, "The current film is shorter")
        self.film_long.length = 142
        self.assertFalse(self.film_same_length > self.film_short, "Both films are the same length")
        self.film_long.length = 142
        self.assertFalse(self.film_long > self.non_film, "The other object is not a Film")

    def test_string_conversion(self):
        """Test string conversion."""
        self.assertEqual(str(self.film_long), "Harry Potter and the Prisoner of Azkaban, 142 minutes long film, with 0 ratings.")
        self.film_long.ratings = [9.0, 10.0, 7.0, 10.0, 9.5]
        self.assertEqual(str(self.film_long), "Harry Potter and the Prisoner of Azkaban, 142 minutes long film, with 5 ratings.")

    def test_equality_operator(self):
        """Test the equality operator."""
        film_equal_empty = task.Film("Harry Potter and the Prisoner of Azkaban", 142)
        self.assertTrue(self.film_long == film_equal_empty, "They are equal (ratings list is empty)")

        self.film_long.ratings = [10.0, 7.0, 8.0]
        film_equal_empty.ratings = [10.0, 7.0, 8.0]
        self.assertTrue(self.film_long == film_equal_empty, "They are equal (ratings list is not empty)")

        self.film_long.ratings = [10.0, 7.0, 8.0, 9.5]
        film_equal_empty.ratings = [10.0, 6.0, 8.0]
        self.assertFalse(self.film_long == film_equal_empty, "They are not equal (ratings list differs)")

        self.film_long._title = "Harry Potter and the Half-Blood Prince"
        self.assertFalse(self.film_long == film_equal_empty, "They are not equal (title differs)")

        self.film_long.length = 150
        self.assertFalse(self.film_long == film_equal_empty, "They are not equal (length differs)")

        self.assertFalse(self.film_long == 123, "They are not equal, not comparing with a Film")
        self.assertFalse(self.film_long == None, "They are not equal, not comparing with a Film")


if __name__ == "__main__":
    unittest.main()
