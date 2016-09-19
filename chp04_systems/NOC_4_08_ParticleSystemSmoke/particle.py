# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Particle(object):
    def __init__(self, l, img):
        self.acceleration = PVector(0, 0)

        vx = randomGaussian()*0.3
        vy = randomGaussian()*0.3 - 1
        self.velocity = PVector(vx, vy)
        
        self.position = l.get()
        
        self.lifespan = 100
        self.img = img

    def run(self):
        self.update()
        self.display()

    def apply_force(self, force):
        self.acceleration.add(force)

    def update(self):
        """Method to update position"""
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.lifespan -= 2.5
        self.acceleration.mult(0)

    def display(self):
        """Method to display"""
        imageMode(CENTER)
        tint(255, self.lifespan)
        image(self.img, self.position.x, self.position.y)

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan <= 0.0
