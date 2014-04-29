# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker class!


class Walker(object):

    def __init__(self):
        self.location = PVector(width / 2, height / 2)
        self.noff = PVector(random(1000), random(1000))

    def display(self):
        strokeWeight(2)
        fill(127)
        stroke(0)
        ellipse(self.location.x, self.location.y, 48, 48)

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        self.location.x = map(noise(self.noff.x), 0, 1, 0, width)
        self.location.y = map(noise(self.noff.y), 0, 1, 0, height)
        self.noff.x += 0.01
        self.noff.y += 0.01

