# The Nature of Code
# Chapter 3: Oscillation
# Daniel Shiffman
#
# Python port by Abhik Pal

class Spring(object):
    """
    Class to describe an anchor point that can connect to "Bob" objects via
    a spring.
    Thank you: http://www.myphysicslab.com/spring2d.html
    """

    def __init__(self, x, y, l):
        # position
        self.anchor = PVector(x, y)
        
        # Rest length and spring constant
        self.length = l
        self.k = 0.2

    def connect(self, b):
        """Calculate spring force"""

        # Vector pointing from anchor to bob position
        force = PVector.sub(b.position, self.anchor)
        
        # What is distance
        d = force.mag()
        
        # Stretch is difference between current distance and rest length
        stretch = d - self.length

        # Calculate force according to Hooke's Law
        # F = k * stretch
        force.normalize()
        force.mult(-1 * self.k * stretch)
        b.applyForce(force)

    def constrainLength(self, b, minlen, maxlen):
        """
        Constrain the distance between bob and anchor between min and max
        """
        
        direction = PVector.sub(b.position, self.anchor)
        d = direction.mag()
        
        # Is it too short?
        if d < minlen:
            direction.normalize()
            direction.mult(minlen)
            
            # Reset position and stop from moving (not realistic physics)
            b.position = PVector.add(self.anchor, direction)
            b.velocity.mult(0)
            
        # Is it too long?
        elif d > maxlen:
            direction.normalize()
            direction.mult(maxlen)
            
            # Reset position and stop from moving (not realistic physics)
            b.position = PVector.add(self.anchor, direction)
            b.velocity.mult(0)

    def display(self):
        stroke(0)
        fill(175)
        strokeWeight(2)
        rectMode(CENTER)
        rect(self.anchor.x, self.anchor.y, 10, 10)

    def displayLine(self, b):
        strokeWeight(2)
        stroke(0)
        line(b.position.x, b.position.y, self.anchor.x, self.anchor.y)
