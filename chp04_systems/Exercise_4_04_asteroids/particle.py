# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Particle(object):
    """
    A Simple Paticle Class
    """
    def __init__(self, l, dir):
        self.acceleration = dir.get()
        self. velocity = PVector.random2D()
        self.location = l.get()
        self.lifespan = 255.0
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        """Method to update position"""
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= 2.0
    
    def display(self):
        """Method to display"""
        noStroke()
        fill(127, 0, 0, self.lifespan)
        ellipse(self.location.x, self.location.y, 8, 8)
        
    def is_dead(self):
        """Is the particle still useful?"""
        return self.lifespan < 0.0