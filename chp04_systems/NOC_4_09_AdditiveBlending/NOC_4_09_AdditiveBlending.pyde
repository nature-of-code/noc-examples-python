# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Additive Blending

# This example demonstrates a "glow" like effect using
# additive blending with a Particle system.  By playing
# with colors, textures, etc. you can achieve a variety
# of looks.

from particle_system import ParticleSystem

def setup():
    size(640, 360, P2D)

    # Create an alpha masked image to be applied as the particle's
    # texture.
    global img
    img = loadImage("texture.png")

    global ps
    ps = ParticleSystem(PVector(width/2, 50), img)

def draw():
    # Additive blending!
    blendMode(ADD)

    background(0)

    global ps
    global img
    ps.run()
    for i in range(10):
        ps.add_particle()