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

    def run(self):
        self.update()
        self.display()

    def intersects(self, particles):
        for other in particles:
            if other != self:
                dir = PVector.sub(self.position, other.position)
                if dir.mag() < self.r*2:
                    dir.setMag(0.5)
                    self.apply_force(dir)

    def apply_force(self, force):
        self.acceleration.add(force)

    def update(self):
        """Method to update position."""
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.lifespan -= 0.5

    def display(self):
        """Method to display"""
        stroke(0, self.lifespan)
        strokeWeight(2)
        fill(127, self.lifespan)
        ellipse(self.position.x, self.position.y, self.r*2, self.r*2)

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan < 0