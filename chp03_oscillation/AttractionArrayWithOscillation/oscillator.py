# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Oscillator(object):
    """
    Attraction Array with Oscillating objects around each thing
    """

    def __init__(self, r):
        # Because we are going to oscillate along the x and y axis we can
        # use PVector for two angles, amplitudes, etc.!
        # Initialize randomly
        self.theta = 0
        self.amplitude = r

    def update(self, thetaVel):
        # Update self.theta and offset
        self.theta += thetaVel

    def display(self, pos):
        # Display based on a position
        x = map(cos(self.theta), -1, 1, 0, self.amplitude)

        stroke(0)
        fill(50)
        line(0, 0, x, 0)
        ellipse(x, 0, 8, 8)


