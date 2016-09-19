# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

class ParticleSystem(object):
    def __init__(self, position):
        # List of all the particles
        self.particles = []

        # Origin point for where the particles are birthed
        self.origin = position.get()

    def add_particle(self):
        self.particles.append(Particle(self.origin))

    def apply_force(self, f):
        """A function to apply force to all particles"""
        for p in self.particles:
            p.apply_force(f)

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.is_dead():
                dead_p = self.particles.pop(i)
