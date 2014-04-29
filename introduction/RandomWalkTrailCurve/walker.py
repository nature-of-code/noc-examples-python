# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker object!


class Walker(object):

    def __init__(self):
        self.position = PVector(width / 2, height / 2)
        self.history = []

    def render(self):
        stroke(0)
        beginShape()
        for v in self.history:
            curveVertex(v.x, v.y)
        endShape()
        noFill()
        stroke(0)
        ellipse(self.position.x, self.position.y, 16, 16)

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        self.position.x += random(-10, 10)
        self.position.y += random(-10, 10)
        self.position.x = constrain(self.position.x, 0, width - 1)
        self.position.y = constrain(self.position.y, 0, height - 1)
        self.history.append(self.position.get())

