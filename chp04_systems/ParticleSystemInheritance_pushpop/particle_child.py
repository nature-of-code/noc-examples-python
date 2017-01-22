# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from particle import Particle

class ParticleChild(Particle):
    # We override the display() method.
    def display(self):
        super(ParticleChild, self).display()
        theta = map(self.position.x, 0, width, 0, TWO_PI*2)
        rotate(theta)
        stroke(0)
        line(0, 0, 50, 0)
