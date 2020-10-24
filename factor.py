class Factor:
    """Generate Factors for a Number"""

    def __init__(self, number):
        """Set number to generate factors for"""

        if not isinstance(number, int):
            raise ValueError("Expected type of number to be int")

        if number < 1:
            raise ValueError("Expected a posive int value")

        self.number = number
    
    def __iter__(self):
        """Generator logic"""

        initial = 1
        while initial != self.number + 1:
            if self.number % initial == 0:
                yield initial
            initial += 1
    
    def __call__(self):
        """Get collection"""

        return tuple(i for i in self)
