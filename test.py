import unittest

from armstrong import Armstrong
from factor import Factor
from factorial import Factorial
from fibonacci import Fibonacci
from palindrome import Palindrome
from prime import Prime


class Test(unittest.TestCase):
    """."""

    def test_armstrong(self):
        """."""

        self.assertEqual(bool(Armstrong(153)), True)
        self.assertEqual(bool(Armstrong(1634)), True)
        self.assertEqual(bool(Armstrong(151)), False)
        self.assertEqual(bool(Armstrong(1624)), False)
        with self.assertRaises(TypeError):
            bool(Armstrong(1.1))

    def test_palindrome(self):
        """."""

        self.assertEqual(bool(Palindrome(121)), True)
        self.assertEqual(bool(Palindrome(122)), False)

    def test_fibonacci(self):
        """."""

        self.assertEqual([i for i in Fibonacci(5)], [0, 1, 1, 2, 3])

    def test_factor(self):
        """."""

        self.assertEqual([i for i in Factor(10)], [1, 2, 5, 10])

    def test_factorial(self):
        """."""

        self.assertEqual(Factorial(6)(), 720)

    def test_prime(self):
        """."""

        self.assertEqual(bool(Prime(7)), True)
        self.assertEqual(bool(Prime(6)), False)
