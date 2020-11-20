class Armstrong:
    """Check Armstrong Number"""

    def __init__(self, number):
        """Set number"""

        if not isinstance(number, int):
            raise ValueError("Expected number of type int")

        self.number = number
    
    def __len__(self):
        """Get order"""

        count, copy = 0, self.number
        while copy:
            copy //= 10
            count += 1
        
        return count

    @property
    def calculated(self):
        """Perform calculation"""

        calculated, order, copy = 0, len(self), self.number
        while copy:
            calculated += (copy % 10) ** order
            copy //= 10

        return calculated
    
    def __call__(self):
        """Get boolean check value"""
        
        return self.calculated == self.number
