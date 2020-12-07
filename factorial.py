class Factorial:
    """."""

    def __init__(self, number):
        """."""

        if not isinstance(number, int):
            raise TypeError("Expected number to be of type int")

        if number < 0:
            raise ValueError("Expected number to be greater than -1")

        self.number = number

    def __call__(self):
        """."""

        calculated, copy = 1, self.number
        while copy:
            calculated *= copy
            copy -= 1
        return calculated
