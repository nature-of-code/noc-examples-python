# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker object!


class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def render(self):
        stroke(255)
        point(self.x, self.y)

    # Randomly move according to floating point values
    def step(self):
        stepx = random(-1, 1)
        stepy = random(-1, 1)
        self.x += stepx
        self.y += stepy
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

