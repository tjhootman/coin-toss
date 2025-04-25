from random import choice

class Coin:
    """A class representing a single coin."""

    def __init__(self):
        """Intiaizes the coin. The intial state is determined by the first flip."""
        self.state = None

    def flip(self):
        """Simulates flipping the coin.

        Returns:
            str: State of coing flip. 'Heads' or 'Tails'.
        """
        self.state = choice(['Heads', 'Tails'])
        return self.state
    