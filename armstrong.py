class Armstrong(object):
    """Check Armstrong Number"""

    def __init__(self, number):
        """Set number"""

        if not isinstance(number, int):
            raise TypeError("Expected number to be 'int' got '%s'" % (number.__class__.__name__, ))
        if number < 1:
            raise ValueError("Expected number to be greater than 0")

        self.number = number
    
    def __len__(self):
        """Get order"""

        order, copy = 0, self.number
        while copy:
            order += 1
            copy //= 10
        return order

    @property
    def calculated(self):
        """Perform calculation"""

        calculated, order, copy = 0, len(self), self.number
        while copy:
            calculated += (copy % 10) ** order
            copy //= 10
        return calculated
    
    def __bool__(self):
        """Get boolean check value"""
        
        return self.number == self.calculated
