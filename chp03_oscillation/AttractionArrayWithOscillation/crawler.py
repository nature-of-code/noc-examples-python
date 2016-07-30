# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from oscillator import Oscillator

class Crawler(object):
    """
    Attraction
    
    A class to describe a thing in our world, has vectors for position, 
    velocity, and acceleration.
    Also includes scalar values for mass, maximum velocity, and elasticity.
    """

    def __init__(self):
        self.acc = PVector()
        self.vel = PVector(random(-1, 1), random(-1, 1))
        self.loc = PVector(random(width), random(height))
        self.mass = random(8, 16)
        self.osc = Oscillator(self.mass*2)

    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
        self.acc.add(f)

    def update(self):
        
        # Method to update position
        self.vel.add(self.acc)
        self.loc.add(self.vel)
        
        # Multiplying by 0 sets the all the components to 0
        self.acc.mult(0)

        self.osc.update(self.vel.mag()/10)

    def display(self):
        # Method to display
        angle = self.vel.heading2D()
        
        pushMatrix()
        translate(self.loc.x, self.loc.y)
        rotate(angle)
        
        ellipseMode(CENTER)
        stroke(0)
        fill(175, 100)
        ellipse(0, 0, self.mass*2, self.mass*2)

        self.osc.display(self.loc)
        
        popMatrix()
