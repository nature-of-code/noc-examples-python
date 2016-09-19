# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Particle(object):
    """
    A Simple Paticle Class
    """
    def __init__(self, x, y, r):
        self.acceleration = PVector(0, 0.01)
        self.velocity = PVector.random2D()
        self.velocity.mult(0.5)
        self.position = PVector(x, y)
        self.lifespan = 255.0

        self.r = r

    def run(self):
        self.update()
        self.display()

    def update(self):
        """Method to update position"""
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.lifespan -= 2.0

    def display(self):
        """Method to display"""
        stroke(0)
        fill(0)
        rectMode(CENTER)
        rect(self.position.x, self.position.y, self.r, self.r)

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan < 0.0