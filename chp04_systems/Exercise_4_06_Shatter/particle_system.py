# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

class ParticleSystem(object):

    def __init__(self, x, y, r):
        self.particles = []

        self.rows = 20
        self.cols = 20

        self.intact = True

        for i in range(self.rows*self.cols):
            self.add_particle(x + (i%self.cols)*r,
                y + (i/self.rows)*r,
                r)

    def add_particle(self, x, y, r):
        self.particles.append(Particle(x, y, r))

    def display(self):
        for p in self.particles:
            p.display()

    def shatter(self):
        self.intact = False

    def update(self):
        if not self.intact:
            for p in self.particles:
                p.update()