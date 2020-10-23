class Palindrome:
    """."""

    def __init__(self, number):
        """."""

        if not isinstance(number, int):
            raise ValueError("Expected type to be of int")

        self.number = number
    
    def __call__(self):
        """."""
        
        copy = self.number
        calculated = 0
        while copy:
            calculated = (calculated * 10) + (copy % 10)
            copy //= 10
        return calculated == self.number
