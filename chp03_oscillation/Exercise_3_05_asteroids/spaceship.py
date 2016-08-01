# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Chapter 3: Asteroids

class Spaceship(object): 
    def __init__(self):
        # All of our regular motion stuff
        self.position = PVector(width/2, height/2)
        self.velocity = PVector()
        self.acceleration = PVector()

        # Arbitrary damping to slow down ship
        self.damping = 0.995
        self.topspeed = 6

        # Variable for heading!
        self.heading = 0

        # Size
        self.r = 16

        # Are we thrusting (to color boosters)
        self.thrusting = False 

    def update(self): 
        """Standard Euler integration"""
        self.velocity.add(self.acceleration)
        self.velocity.mult(self.damping)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def applyForce(self, force):
        """Newton's law: F = M * A"""
        f = force.get()

        # ignoring mass right now
        # f.div(mass)
        
        self.acceleration.add(f)

    def turn(self, a):
        """Turn changes angle"""
        self.heading += a

    def thrust(self):
        """Apply a thrust force"""
        
        # Offset the angle since we drew the ship vertically
        angle = self.heading - PI/2
        
        # Polar to cartesian for force vector!
        force = PVector(cos(angle),sin(angle))
        force.mult(0.1)
        self.applyForce(force)
        
        # To draw booster
        self.thrusting = True

    def wrapEdges(self):
        wrap_buffer = self.r*2
        if self.position.x > (width + wrap_buffer):
            self.position.x = -wrap_buffer
        elif self.position.x <  (-wrap_buffer):
            self.position.x = width + wrap_buffer

        if self.position.y > (height + wrap_buffer):
            self.position.y = -wrap_buffer
        elif self.position.y < (-wrap_buffer):
            self.position.y = height + wrap_buffer

    def display(self): 
        """Draw the ship"""
        stroke(0)
        strokeWeight(2)
        
        pushMatrix()

        translate(self.position.x, self.position.y+self.r)
        rotate(self.heading)
        fill(175)
        
        if self.thrusting:
            fill(255,0,0)
        
        # Booster rockets
        rect(-self.r/2,self.r, self.r/3, self.r/2)
        rect(self.r/2,self.r, self.r/3, self.r/2)
        fill(175)
        
        # A triangle
        beginShape()
        vertex(-self.r, self.r)
        vertex(0, -self.r)
        vertex(self.r, self.r)
        endShape(CLOSE)
        
        rectMode(CENTER)
        
        popMatrix()

        self.thrusting = False