# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

class ParticleSystem(object):
    """
    A class to describe a group of particles
    A python list is used to manage the list of Particles (duh)
    """
    def __init__(self, position, img):
        # List of all the particles
        self.particles = []

        # Origin point for where the particles are birthed
        self.origin = position.get()
        self.img = img

    def add_particle(self, p=None):
        if not p:
            self.particles.append(Particle(self.origin, self.img))
        else:
            self.particles.append(p)

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.is_dead():
                dead_p = self.particles.pop(i)

    def dead(self):
        """
        A method to test if the particle system still has particles.
        """
        return len(self.particles) == 0