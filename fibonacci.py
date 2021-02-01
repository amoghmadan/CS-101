class Fibonacci(object):
    """Generate Fibonacci Numbers"""

    def __init__(self, length, first=0, second=1):
        """Set length and initials for the series"""

        if not isinstance(length, int):
            raise TypeError("Expected length to be 'int' got '%s'" % (length.__class__.__name__, ))
        if length < 2:
            raise ValueError("Expected length to be greater than 1")

        if not isinstance(first, int):
            raise TypeError("Expected first to be 'int' got '%s'" % (first.__class__.__name__, ))

        if not isinstance(second, int):
            raise TypeError("Expected second to be 'int' got '%s'" % (second.__class__.__name__, ))

        self.length = length
        self.first = first
        self.second = second
    
    def __iter__(self):
        """Iterate to generate numbers until length reduces down to 0"""

        length, first, second = self.length, self.first, self.second

        while length:
            yield first
            first, second = second, first + second
            length -= 1
