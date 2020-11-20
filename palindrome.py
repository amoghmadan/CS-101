class Palindrome:
    """."""

    def __init__(self, number):
        """."""

        if not isinstance(number, int):
            raise ValueError("Expected type to be of int")

        self.number = number

    def __reversed__(self):
        """."""

        calculated, copy = 0, self.number
        while copy:
            calculated = (calculated * 10) + (copy % 10)
            copy //= 10

        return calculated
    
    def __call__(self):
        """."""
        
        return self.number == reversed(self)
