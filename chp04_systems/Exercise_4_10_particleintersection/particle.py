# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

class Particle(object):
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.position = PVector(x, y)
        self.lifespan = 255

        self.r = 6
        self.highlight = False

    def run(self):
        self.update()
        self.display()

    def intersect(self, particles):
        self.highlight = False
        for other in particles:
            if other != self:
                d = PVector.dist(other.position, self.position)
                if d < self.r:
                    self.highlight = True

    def apply_force(self, force):
        self.acceleration.add(force)

    def update(self):
        """Method to update position."""
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.lifespan -= 2.0

    def display(self):
        """Method to display"""
        stroke(0, self.lifespan)
        strokeWeight(2)
        fill(127, self.lifespan)
        if self.highlight:
            fill(127, 0, 0)
        ellipse(self.position.x, self.position.y, self.r*2, self.r*2)

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan < 0