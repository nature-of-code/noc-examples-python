# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Mover(object):

    def __init__(self):
        self.position = PVector(400, 50)
        self.velocity = PVector(1, 0)
        self.acceleration = PVector(0, 0)
        self.mass = 1

    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        
        pushMatrix()
        translate(self.position.x, self.position.y)
        heading = self.velocity.heading()
        rotate(heading)
        ellipse(0, 0, 16, 16)
        rectMode(CENTER)
        # "20" should be a variable that is oscillating
        # with sine function
        rect(20, 0, 10, 10)
        popMatrix()

    def checkEdges(self):
        if position.x > width:
            self.position.x = 0
        elif position.x < 0:
            self.position.x = width

        if position.y > height:
            self.velocity.y *= -1
            self.position.y = height
