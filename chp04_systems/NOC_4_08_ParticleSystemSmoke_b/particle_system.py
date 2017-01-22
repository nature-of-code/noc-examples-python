# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Smoke particle system

from particle import Particle

class ParticleSystem(object):
    """
    A class to describe a group of particles
    A python list is used to manage the list of Particles (duh)
    """
    def __init__(self, num, position, img):
        # List of all the particles
        self.particles = []

        # Origin point for where the particles are birthed
        self.origin = position.get()
        self.img = img

        # Add `num` amount of particles
        for i in range(num):
            self.particles.append(Particle(self.origin, self.img))

    def add_particle(self):
        self.particles.append(Particle(self.origin, self.img))

    def apply_force(self, f):
        """A function to apply force to all particles"""
        for p in self.particles:
            p.apply_force(f)

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.is_dead():
                dead_p = self.particles.pop(i)
