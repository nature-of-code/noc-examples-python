# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

# A class for a draggable attractive body in our world

class Attractor(object):

    def __init__(self):
        self.position = PVector(0, 0)  # Position
        self.mass = 20  # Mass, tied to size
        self.g = 0.4;     # Gravitational Constant

    def attract(self, m):
        force = PVector.sub(self.position, m.position)
        d = force.mag()
        d = constrain(d,5.0,25.0)

        force.normalize();
        strength = (self.g * self.mass * m.mass)/float(d * d)
        force.mult(strength)

        return force

    def display(self):
        stroke(255)
        noFill()
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        sphere(self.mass*2)
        popMatrix()
