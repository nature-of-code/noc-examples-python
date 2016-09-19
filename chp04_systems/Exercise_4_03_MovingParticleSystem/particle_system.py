# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

class ParticleSystem(object):
    """Simple Particle System

    A class to describe a group of Particles
    A list is used to manage the particles.
    """
    def __init__(self, location):
        # List of all the particles
        self.particles = []

        # Origin point for where the particles are birthed
        self.origin = location.get()

    def add_particle(self):
        self.particles.append(Particle(self.origin))

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.is_dead():
                dead_p = self.particles.pop(i)

    def is_dead(self):
        """A Method to test is the particle system has particles"""
        return len(self.particles) == 0
