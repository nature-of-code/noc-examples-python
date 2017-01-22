# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Mover(object):
    def __init__(self, mass, x, y):
        self.mass = mass
        self.position = PVector(x, y)
        self.velocity = PVector(random(-1, 1), random(-1, 1))
        self.acceleration = PVector(0, 0)

        self.angle = 0
        self.aVelocity = 0
        self.aAcceleration = 0

    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        
        self.aAcceleration = self.acceleration.x / 10.0
        self.aVelocity += self.aAcceleration
        self.aVelocity = constrain(self.aVelocity,-0.1,0.1)
        self.angle += self.aVelocity
        
        self.acceleration.mult(0)        
    
    def display(self):
        stroke(0)
        fill(175, 200)
        rectMode(CENTER)
        
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(self.angle)
        rect(0, 0, self.mass*16, self.mass*16)
        popMatrix()
