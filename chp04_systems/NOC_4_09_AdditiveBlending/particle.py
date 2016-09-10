# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Particle(object):
    """
    Simple particle. Renders the image as an image.
    """
    def __init__(self, l, img):
        self.acceleration = PVector(0, 0.05, 0)
        self.velocity = PVector(random(-1, 1), random(-1, 1), 0)
        self.velocity.mult(2)

        self.position = l.get()
        self.img = img
        
        self.lifespan = 255

    def run(self):
        self.update()
        self.render()

    def render(self):
        imageMode(CENTER)
        tint(self.lifespan)
        image(self.img, self.position.x, self.position.y)

    def update(self):
        """Method to update position"""
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.lifespan -= 2

    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan <= 0.0