class Factorial(object):
    """Callable Factorial"""

    def __init__(self, number):
        """Check type and value"""

        if not isinstance(number, int):
            raise TypeError("Expected number to be 'int' got '%s'" % (number.__class__.__name__, ))
        if number < 0:
            raise ValueError("Expected number to be greater than -1")

        self.number = number

    def __call__(self):
        """Calculate Factorial"""

        calculated, copy = 1, self.number
        while copy:
            calculated *= copy
            copy -= 1
        return calculated
