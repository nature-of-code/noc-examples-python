# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


class Mover(object):

    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(random(-2, 2), random(-2, 2))

    def update(self):
        self.location.add(self.velocity)

    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.location.x, self.location.y, 48, 48)

    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width

        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height

