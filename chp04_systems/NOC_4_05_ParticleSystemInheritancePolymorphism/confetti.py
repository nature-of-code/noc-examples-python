# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

class Confetti(Particle):
    def __init__(self, location):
        super(Confetti, self).__init__(location)
    
    def display(self):
        rectMode(CENTER)
        fill(127, self.lifespan)
        stroke(0, self.lifespan)
        strokeWeight(2)
        pushMatrix()
        translate(self.position.x, self.position.y)
        theta = map(self.position.x, 0, width, 0, TWO_PI*2)
        rotate(theta)
        rect(0, 0, 12, 12)
        popMatrix()