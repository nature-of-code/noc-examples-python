# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker object!


class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def render(self):
        stroke(0)
        strokeWeight(2)
        point(self.x, self.y)

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        r = random(1)
        # A 40% of moving to the right!
        if r < 0.4:
            self.x += 1
        elif r < 0.5:
            self.x -= 1
        elif r < 0.9:
            self.y += 1
        else:
            self.y -= 1

        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

