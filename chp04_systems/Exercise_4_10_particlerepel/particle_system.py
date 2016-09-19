# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from particle import Particle

class ParticleSystem(object):

    def __init__(self, position):
        self.particles = []
        
    def add_particle(self, x, y):
        self.particles.append(Particle(x, y))

    def display(self):
        for particle in self.particles:
            particle.display()

    def apply_force(self, f):
        for particle in self.particles:
            particle.apply_force(f)

    def intersection(self):
        for particle in self.particles:
            particle.intersects(self.particles)

    def update(self):
        for i, p in enumerate(self.particles):
            p.update()
            if p.is_dead():
                dead_p = self.particles.pop(i)