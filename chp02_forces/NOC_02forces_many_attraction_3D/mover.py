# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    def __init__(self, m, x, y, z):
        self.mass = m
        self.position = PVector(x, y, z)
        self.velocity = PVector(1, 0)
        self.acceleration = PVector(0,0)
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        noStroke()
        fill(255)
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        sphere(self.mass*8)
        popMatrix()

    def checkEdges(self):
        if (self.position.x > width):
            self.position.x = 0
        elif (self.position.y < 0):
            self.position.y = width

        if (self.position.y > height):
            self.velocity.y *= -1
            self.position.y = height