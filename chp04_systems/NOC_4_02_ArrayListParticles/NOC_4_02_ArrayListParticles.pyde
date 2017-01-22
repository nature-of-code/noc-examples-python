# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

particles = []

def setup():
    size(640, 360)

def draw():
    background(255)
    global particles

    particles.append(Particle(PVector(width/2, 50)))

    for i, p in enumerate(particles):
        p.run()
        if p.is_dead():
            dead_p = particles.pop(i)