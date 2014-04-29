# Daniel Shiffman
# The Nature of Code
# http://natureofcode.com
# A random walker class!


class Walker(object):

    def __init__(self):
        self.loc = PVector(width / 2, height / 2)

    def render(self):
        stroke(0)
        fill(175)
        rectMode(CENTER)
        rect(self.loc.x, self.loc.y, 40, 40)

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        vel = PVector(random(-2, 2), random(-2, 2))
        self.loc.add(vel)

        # Stay on the screen
        self.loc.x = constrain(self.loc.x, 0, width - 1)
        self.loc.y = constrain(self.loc.y, 0, height - 1)

