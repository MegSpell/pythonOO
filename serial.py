"""
Python serial number generator.

The SerialGenerator class is designed to create and manage a sequence of unique, incrementing serial numbers. It allows generating the next number in the sequence and resetting the sequence back to its starting value.
"""

class SerialGenerator:
    """
    A class to generate unique incrementing serial numbers.
    
    This class maintains a sequence of serial numbers starting from an initial value.
    It allows you to generate the next number in the sequence and reset the sequence to its initial state.

    Attributes:
    - start (int): The initial value of the sequence.
    - next (int): The next value to be generated in the sequence.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """
        Initializes the SerialGenerator with a starting value.

        Sets the initial value of the serial number sequence to `start` and
        prepares the generator to begin from that value.

        Parameters:
        - start (int): The starting value for the serial number sequence. Defaults to 0.
        """

        self.start = self.next = start

    def __repr__(self):
        """
        Show representation.

        Returns a string representation of the SerialGenerator object.

        This representation includes the starting value and the next value to be generated,
        which is useful for debugging and inspecting the state of the generator.

        Returns:
        - str: A string showing the current state of the SerialGenerator.
        """

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """
        Generates and returns the next serial number in the sequence.

        Increments the internal counter and returns the previous value,
        which is the next serial number in the sequence.

        Returns:
        - int: The next serial number in the sequence.
        """

        self.next += 1
        return self.next - 1

    def reset(self):
        """
        Resets the serial number sequence to the initial starting value.

        This method sets the internal counter back to the value specified at initialization, allowing the sequence to start again from the beginning.
        """

        self.next = self.start