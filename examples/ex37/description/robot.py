import unittest
from inspect import signature
from task import filter


class TestRobot(unittest.TestCase):

    def test_param_count(self):
        self.assertEqual(len(signature(filter).parameters), 1)

    def test_function_on_params_not_string(self):
        self.assertEqual(filter(12345), [])
        self.assertEqual(filter(3.654), [])
        self.assertEqual(filter(True), [])
        self.assertEqual(filter({}), [])

    def test_function_on_empty_string(self):
        self.assertEqual(filter(""), [])
        self.assertEqual(filter(" "), [])

    def test_function_on_uppercase_palindrome_words(self):
        self.assertEqual(
            filter("LEVEL,KAYAK,ROTOR,BOB,SAS,NOON,RACECAR,MADAM"),
            ['LEVEL', 'KAYAK', 'ROTOR', 'RACECAR', 'MADAM'])
        self.assertEqual(filter("LEVEL"), [])
        self.assertEqual(filter("LEVEL,BOB"), ["LEVEL"])

    def test_function_on_mixed_case_palindrome_words(self):
        self.assertEqual(
            filter("LEVEL,kaYak,rotor,BOB,SAS,NOON,RaCeCaR,MADAM"),
            ['LEVEL', 'KAYAK', 'ROTOR', 'RACECAR', 'MADAM'])
        self.assertEqual(filter("level"), [])
        self.assertEqual(filter('apple,banana,grape'), ['ANANAB'])
        self.assertEqual(filter("LEVEl,bob"), ["LEVEL"])

    def test_function_on_every_condition_is_fulfilled(self):
        self.assertEqual(
            filter('mercury,venus,earth,mars,jupiter,saturn,uranus,neptune'),
            ['YRUCREM', 'RETIPUJ', 'NRUTAS', 'SUNARU', 'ENUTPEN'])
        self.assertEqual(
            filter('neptun,coospace,modulo,zoom,skype,moodle,colab,youtube'),
            ['NUTPEN', 'ECAPSOOC', 'OLUDOM', 'ELDOOM', 'EBUTUOY'])
        self.assertEqual(
            filter('google,miscrosoft,apple,xiaomi,asus,intel,amd'),
            ['ELGOOG', 'TFOSORCSIM', 'IMOAIX'])
        self.assertEqual(
            filter('honda,suzuki,kawasaki,peda,sprint,peugeot'),
            ['IKASAWAK', 'TOEGUEP'])


if __name__ == "__main__":
    unittest.main()
