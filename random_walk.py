from random import choice


class RandomWalk:
    """Class used to generate random walk"""

    def __init__(self, num_points=5000):
        """Initialize attributes for random walk"""
        self.num_points = num_points

        # Initial coordinates
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate all points for random walk"""

        # Use steps until certain number of points is reached
        while len(self.x_values) < self.num_points:

            # Set direction and distance cover in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Discard steps that lead to nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Set next values for X and Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
