class Prime(object):
    """Check for Prime Number"""

    def __init__(self, number):
        """Set number to check"""

        if not isinstance(number, int):
            raise TypeError("Expected number to be 'int' got '%s'" % (number.__class__.__name__, ))
        if number < 2:
            raise ValueError("Expected number to be greater than 1")

        self.number = number

    def __bool__(self):
        """Check prime"""

        if self.number == 2:
            return True
        
        if self.number == 1 or self.number % 2 == 0:
            return False

        initial = 3
        while initial != self.number:
            if self.number % initial == 0:
                return False
            initial += 2

        return True
