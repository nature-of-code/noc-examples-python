# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from particle_system import ParticleSystem

def setup():
    size(640, 360)
    global ps
    ps = ParticleSystem(PVector(width/2, 50))

def draw():
    background(255)
    global ps

    ps.add_particle()
    ps.run()
