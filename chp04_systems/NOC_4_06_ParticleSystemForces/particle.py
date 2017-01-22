# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Particle(object):
    def __init__(self, l):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.position = l.get()
        self.lifespan = 255.0
        self.mass = 1

    def run(self):
        self.update()
        self.display()

    def apply_force(self, force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)

    def update(self):
        """Method to update position"""
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.lifespan -= 2.0

    def display(self):
        """Method to display"""
        stroke(0, self.lifespan)
        strokeWeight(2)
        fill(0, self.lifespan)
        ellipse(self.position.x, self.position.y, 12, 12)

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan < 0.0
