# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    
    def __init__(self):
        self.position = PVector(width/2.0, height/2.0)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0,0)
        self.mass = 1

    def shake(self):
        force = PVector.random2D()
        force.mult(0.7)
        self.applyForce(force)
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

        self.velocity.mult(0.95)
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 48, 48)

    def checkEdges():
        if (self.position.x > width):
            self.position.x = width
            self.velocity.x *= -1
        elif (self.position.x < 0):
            self.position.x = 0
            self.velocity.x *= -1

        if (self.position.y > height):
            self.position.y = width
            self.velocity.y *= -1