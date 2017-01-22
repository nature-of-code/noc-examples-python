# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from particle import Particle

class ParticleSystem(object):
    """A class to describe a group of particles
    A list is used to manage the particles."""
    def __init__(self, imgs):
        self.textures = imgs

        # initialize the list of particles
        self.particles = []

    def run(self):
        for i, particle in enumerate(self.particles):
            particle.run()
            if particle.is_dead():
                self.particles.pop(i)
    
    def add_particle(self, x, y, p=None):
        if not p:
            r = int(random(len(self.textures)))
            self.particles.append(Particle(x, y, self.textures[r]))
        else:
            self.particles.append(p)

    def apply_force(self, f):
        for particle in self.particles:
            particle.apply_force(f)


    def dead(self):
        return len(self.particles) == 0