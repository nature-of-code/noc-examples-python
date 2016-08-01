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

    def __init__(self, a, b, l):
        self.a = a
        self.b = b

        # Rest length and spring constant
        self.length = l
        self.k = 0.2

    def update(self):
        """Calculate spring force"""

        # Vector pointing from anchor to bob position
        force = PVector.sub(self.a.position, self.b.position)
        
        # What is distance
        d = force.mag()
        
        # Stretch is difference between current distance and rest length
        stretch = d - self.length

        # Calculate force according to Hooke's Law
        # F = k * stretch
        force.normalize()
        force.mult(-1 * self.k * stretch)
        self.a.applyForce(force)
        force.mult(-1)
        self.b.applyForce(force)

    def display(self):
        strokeWeight(2)
        stroke(0)
        line(self.b.position.x, self.b.position.y, \
             self.a.position.x, self.a.position.y)
