import unittest
from sample import fizzbuzz 

class FizzTest(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')