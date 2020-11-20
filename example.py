from armstrong import Armstrong
from factor import Factor
from factorial import Factorial
from fibonacci import Fibonacci
from palindrome import Palindrome
from prime import Prime

is_armstrong = Armstrong(153)
print("Armstrong", is_armstrong())

fibonacci = Fibonacci(5)
print("Fibonacci", fibonacci())

is_palindrome = Palindrome(12321)
print("Palindrome", is_palindrome())

is_prime = Prime(10007)
print("Prime", is_prime())

has_factors = Factor(23)
print("Factors", has_factors())

factorial = Factorial(6)
print("Factorial", factorial())
