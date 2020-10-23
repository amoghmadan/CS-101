class Prime:
    """Check for Prime Number"""

    def __init__(self, number):
        """Set number to check"""

        if not isinstance(number, int):
            raise ValueError("Expected type of number to be int")

        if number < 2:
            raise ValueError("Can not check prime for value less than 2")

        self.number = number

    def __call__(self):
        """Validate Number"""

        if self.number == 2:
            return True
        
        if self.number % 2 == 0:
            return False

        for i in range(3, self.number, 2):
            if self.number % i == 0:
                return False

        return True
