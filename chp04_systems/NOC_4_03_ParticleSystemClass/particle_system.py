# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# A simple particle system

from particle import Particle

class ParticleSystem(object):
    def __init__(self, location):
        self.particles = []
        self.origin = location.get()

    def add_particle(self):
        self.particles.append(Particle(self.origin))

    def run(self):
        for i, p in enumerate(self.particles):
            p.run()
            if p.is_dead():
                dead_p = self.particles.pop(i)
