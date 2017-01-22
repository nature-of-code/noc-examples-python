# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle
from confetti import Confetti

class ParticleSystem(object):
    """Simple Particle System

    A class to describe a group of Particles
    A list is used to manage the particles.
    """
    def __init__(self, position):
        # List of all the particles
        self.particles = []

        # Origin point for where the particles are birthed
        self.origin = position.get()

    def add_particle(self):
        r = random(1)
        if r < 0.5:
            self.particles.append(Particle(self.origin))
        else:
            self.particles.append(Confetti(self.origin))

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.is_dead():
                dead_p = self.particles.pop(i)