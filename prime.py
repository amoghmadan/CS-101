class Prime:
    """Check for Prime Number"""

    def __init__(self, number):
        """Set number to check"""

        if not isinstance(number, int):
            raise ValueError("Expected type of number to be int")

        if number < 2:
            raise ValueError("Can not check prime for value less than 2")

        self.number = number

    def __bool__(self):
        """Validate Number"""

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
