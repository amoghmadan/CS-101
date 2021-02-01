class Palindrome(object):
    """Check if a number is a palindrome"""

    def __init__(self, number):
        """Validate number"""

        if not isinstance(number, int):
            raise TypeError("Expected number to be 'int' got '%s'" % (number.__class__.__name__, ))
        if number < 0:
            raise ValueError("Expected number to be greater than -1")

        self.number = number

    def __reversed__(self):
        """Reverse the number"""

        calculated, copy = 0, self.number
        while copy:
            calculated = (calculated * 10) + (copy % 10)
            copy //= 10
        return calculated
    
    def __bool__(self):
        """Check for palindrome"""
        
        return self.number == reversed(self)
