# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker class!


class Walker(object):

    def __init__(self):
        self.location = PVector(width / 2, height / 2)
        self.history = []

    def display(self):
        stroke(0)
        fill(175)
        rectMode(CENTER)
        rect(self.location.x, self.location.y, 16, 16)
        beginShape()
        stroke(0)
        noFill()
        for v in self.history:
            vertex(v.x, v.y)
        endShape()

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        vel = PVector(random(-2, 2), random(-2, 2))
        self.location.add(vel)
        # Stay on the screen
        self.location.x = constrain(self.location.x, 0, width - 1)
        self.location.y = constrain(self.location.y, 0, height - 1)
        self.history.append(self.location.get())
        if len(self.history) > 1000:
            self.history = self.history[1:]

