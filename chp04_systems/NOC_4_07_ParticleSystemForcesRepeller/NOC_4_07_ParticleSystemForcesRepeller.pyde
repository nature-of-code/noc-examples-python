# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle_system import ParticleSystem
from repeller import Repeller

def setup():
    size(640, 360)
    global ps, repeller
    ps = ParticleSystem(PVector(width/2, 50))
    repeller = Repeller(width/2 - 20, height/2)

def draw():
    background(255)
    global ps, repeller

    ps.add_particle()

    # Apply gravity to all particles
    gravity = PVector(0, 0.1)
    ps.apply_force(gravity)

    ps.apply_repeller(repeller)

    repeller.display()
    ps.run()