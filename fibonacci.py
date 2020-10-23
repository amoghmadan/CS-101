class Fibonacci:
    """Generate Fibonacci Numbers"""

    def __init__(self, length, first=0, second=1):
        """Set length and initials for the series"""

        if not isinstance(length, int):
            raise ValueError("Expected length to be of type int")

        if length < 2:
            raise ValueError("Length should be a minimum of 2")

        if not (isinstance(first, int) or isinstance(first, float)):
            raise ValueError("Expected type of first to be of int or float")

        if not (isinstance(second, int) or isinstance(second, float)):
            raise ValueError("Expected type of second to be of int or float")

        self.length = length
        self.first = first
        self.second = second
    
    def __iter__(self):
        """Iterate to generate numbers until length reduces down to 0"""

        while self.length:
            yield self.first
            self.first, self.second = self.second, self.first + self.second
            self.length -= 1
    
    def __call__(self):
        """Get collection"""

        return tuple(i for i in self)