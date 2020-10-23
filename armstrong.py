class Armstrong:
    """Check Armstrong Number"""

    def __init__(self, number):
        """Set number"""

        if not isinstance(number, int):
            raise ValueError("Expected number of type int")

        self.number = number
    
    def __len__(self):
        """Get order"""

        count = 0

        copy = self.number
        while copy:
            copy //= 10
            count += 1
        
        return count
    
    def __call__(self):
        """Get boolean check value"""

        copy = self.number
        order = len(self)
        calculated = 0
        while copy:
            calculated += (copy % 10) ** order
            copy //= 10
        
        return calculated == self.number
