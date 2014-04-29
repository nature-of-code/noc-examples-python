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

    # Randomly move to any neighboring pixel (or stay in the same spot)
    def step(self):
        stepx = int(random(3)) - 1
        stepy = int(random(3)) - 1
        self.x += stepx
        self.y += stepy
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

