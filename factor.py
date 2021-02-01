class Factor(object):
    """Generate Factors for a Number"""

    def __init__(self, number):
        """Set number to generate factors for"""

        if not isinstance(number, int):
            raise TypeError("Expected number to be 'int' got '%s'" % (number.__class__.__name__, ))
        if number < 1:
            raise ValueError("Expected number to be greater than 0")

        self.number = number
    
    def __iter__(self):
        """Generator logic"""

        initial = 1
        while initial < self.number + 1:
            if self.number % initial == 0:
                yield initial
            initial += 1
