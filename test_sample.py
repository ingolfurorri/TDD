import unittest
from sample import fizzbuzz 

class FizzTest(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
    
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
