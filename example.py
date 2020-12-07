from armstrong import Armstrong
from factor import Factor
from factorial import Factorial
from fibonacci import Fibonacci
from palindrome import Palindrome
from prime import Prime

print("Armstrong", bool(Armstrong(153)))

print("Fibonacci", [i for i in Fibonacci(5)])

print("Palindrome", bool(Palindrome(12321)))

print("Prime", bool(Prime(10007)))

print("Factors", [i for i in Factor(23)])

print("Factorial", Factorial(6)())
