import unittest
from inspect import signature
from task import Mathematician


class TestRobot(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        try:
            Mathematician("Bela", 4)
        except (TypeError, AttributeError):
            self.fail("Incorrect constructor!")
        except RecursionError:
            self.fail("Infinite loop!")
        except BaseException as ex:
            self.fail(f'Something went wrong: {ex}')
        super().setUpClass()

    def test_init_param_count(self):
        self.assertEqual(len(signature(Mathematician.__init__).parameters), 3)

    def test_fields(self):
        target = Mathematician("Bela", 4)
        self.assertEqual(target._name, 'Bela')
        self.assertEqual(target.favorite_length, 4)
        self.assertEqual(target.studies, dict())

    def test_getter_property(self):
        target = Mathematician("Bela", 4)
        self.assertEqual(target.name, 'Bela')

    def test_setter_property(self):
        target = Mathematician("Bela", 4)
        target.name = 'Sanyi'
        self.assertEqual(target._name, 'Sanyi')

    def test_add_study_matches_favorite_length(self):
        target = Mathematician("Bela", 4)
        n_gram = [1111, 2222, 4444, 5555]
        target.add_study(n_gram)
        self.assertEqual(target.studies, {4: n_gram})

    def test_add_study_not_matches_favorite_length(self):
        target = Mathematician("Bela", 4)
        n_gram = [333, 111, 222, 987]

        target.add_study(n_gram)
        self.assertEqual(target.studies, {})
        self.assertEqual(target.favorite_length, 3, )

    def test_add_study_complete(self):
        target = Mathematician("Bela", 4)
        n_gram1 = [1234, 5678, 9876, 1357]
        target.add_study(n_gram1)
        self.assertEqual(target.studies, {4: n_gram1})

        n_gram2 = [123, 678, 976, 157]

        target.add_study(n_gram2)

        self.assertEqual(target.studies, {4: n_gram1})
        self.assertEqual(target.favorite_length, 3)

        n_gram3 = [124, 567, 986, 125]

        target.add_study(n_gram3)

        self.assertEqual(target.studies, {4: n_gram1, 3: n_gram3})
        self.assertEqual(target.favorite_length, 3)

    def test_add_study_exception(self):
        target = Mathematician("Bela", 4)
        n_gram = [1, 2, 45]

        with self.assertRaises(ValueError, msg='Incorrect error type'):
            target.add_study(n_gram)

        try:
            target.add_study(n_gram)
        except ValueError as ex:
            self.assertEqual(str(ex), 'Ugly numbers')
        except BaseException:
            self.fail('Incorrect error type')

    def test_lt_operator(self):
        target1 = Mathematician("Bela", 3)
        target2 = Mathematician("Bela", 4)

        self.assertTrue(target1 < target2)

        target2.favorite_length = 2

        self.assertFalse(target1 < target2)

        target1.favorite_length = 2

        self.assertFalse(target1 < target2)

    def test_str_operator(self):
        target = Mathematician("Bela", 3)

        self.assertEqual(str(target),
                         'The mathematician named Bela has a favorite number length of 3, and participated in 0 studies.')

        target.favorite_length = 4

        target.studies = {
            '1': [1, 1, 1],
            '2': [22, 22, 55]
        }

        self.assertEqual(str(target),
                         'The mathematician named Bela has a favorite number length of 4, and participated in 2 studies.')


if __name__ == '__main__':
    unittest.main()
