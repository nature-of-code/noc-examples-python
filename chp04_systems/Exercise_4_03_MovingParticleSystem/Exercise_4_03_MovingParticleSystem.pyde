# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle
from particle_system import ParticleSystem

def setup():
    size(640, 360)

    global ps
    ps = ParticleSystem(PVector(width/2, 50))

def draw():
    background(255)
    global ps

    # Option 1: Move the ParticleSystem origin
    ps.origin.set(mouseX, mouseY, 0)

    ps.add_particle()
    ps.run()

    # Option 2: Move the ParticleSystem origin
    # ps.add_particle(mouseX, mouseY)