# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Oscillator(object):
    def __init__(self):
        self.angle = PVector()
        self.velocity = PVector(random(-0.05, 0.05), random(-0.05, 0.05))
        self.amplitude = PVector(random(20, width/2), random(20, height/2))
            
    def oscillate(self):
        self.angle.add(self.velocity)

    def display(self):
        x = sin(self.angle.x) * self.amplitude.x
        y = sin(self.angle.y) * self.amplitude.y

        pushMatrix()
        translate(width/2, height/2)
        stroke(0)
        strokeWeight(2)
        fill(127,127)
        line(0, 0, x, y)
        ellipse(x, y, 32, 32)
        popMatrix()