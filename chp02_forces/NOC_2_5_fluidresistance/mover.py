# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0,0)
        self.acceleration = PVector(0,0)
        self.mass = m
        
    def applyForce(self, force):
        # Newton's Second Law: F = M * A
        # or A = F / M

        # divide by mass
        f = PVector.div(force, self.mass)

        # accumulate all forces in a acceleration
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127, 200)
        ellipse(self.position.x, self.position.y, self.mass*16, self.mass*16)
    
    def checkEdges(self):
        # Bounce off the bottom of the window.
        if (self.position.y > height):
            self.position.y = height

            # A little dampening when hitting the bottom
            self.velocity.y *= -0.9