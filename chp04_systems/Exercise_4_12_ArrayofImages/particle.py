# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

class Particle(object):
    """Simple Particle class"""
    def __init__(self, x, y, img):
        self.acc = PVector(0, 0)
        self.vel = PVector.random2D()
        self.pos = PVector(x, y)
        self.lifespan = 255
        self.img = img

    def run(self):
        self.update()
        self.display()

    def apply_force(self, f):
        self.acc.add(f)

    def update(self):
        """Method to update position"""
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
        self.lifespan -= 2

    def display(self):
        """Method to display"""
        imageMode(CENTER)
        tint(self.lifespan)
        image(self.img, self.pos.x, self.pos.y, 32, 32)

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan <= 0