# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker object!


class Walker(object):

    def __init__(self):
        self.tx = 0
        self.ty = 10000
        self.x = map(noise(self.tx), 0, 1, 0, width)
        self.y = map(noise(self.ty), 0, 1, 0, height)
        self.prevX, self.prevY = 0, 0

    def render(self):
        stroke(255)
        line(self.prevX, self.prevY, self.x, self.y)

    # Randomly move according to floating point values
    def step(self):
        self.prevX = self.x
        self.prevY = self.y
        self.x = map(noise(self.tx), 0, 1, 0, width)
        self.y = map(noise(self.ty), 0, 1, 0, height)
        self.tx += 0.01
        self.ty += 0.01

