# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Simple Particle System

# Particles are generated each cycle through draw(),
# fall with gravity and fade out over time
# A ParticleSystem object manages a variable size 
# list of particles.

from particle import Particle
from particle_system import ParticleSystem

systems = []

def setup():
    size(640, 360)

def draw():
    background(255)
    global systems
    for ps in systems:
        ps.run()
        ps.add_particle()

    fill(0)
    text("click mouse to add particle systems", 10, height-30)

def mousePressed():
    global systems
    systems.append(ParticleSystem(1, PVector(mouseX, mouseY)))