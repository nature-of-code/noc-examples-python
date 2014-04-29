# Daniel Shiffman
# The Nature of Code
# http://natureofcode.com
# A random walker object!


class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2
        self.prevX = 0
        self.prevY = 0

    def render(self):
        stroke(255)
        line(self.prevX, self.prevY, self.x, self.y)

    # Randomly move according to floating point values
    def step(self):
        self.prevX = self.x
        self.prevY = self.y

        stepx = random(-1, 1)
        stepy = random(-1, 1)

        stepsize = montecarlo() * 50
        stepx *= stepsize
        stepy *= stepsize

        self.x += stepx
        self.y += stepy
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)


def montecarlo():
    while True:
        r1 = random(1)
        probability = pow(1.0 - r1, 8)
        r2 = random(1)
        if r2 < probability:
            return r1

