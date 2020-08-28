from random import choice

class RandomWalk():
    """A calss to generatefrandom walks."""
    
    def __int__(self, num_points=500):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at 0, 0.
        self.x_values = [0]
        self.y_values = [0]
