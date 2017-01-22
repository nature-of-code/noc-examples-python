# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle_system import ParticleSystem

def setup():
    size(640, 360)
    global ps
    ps = ParticleSystem(100, 100, 5)

def draw():
    background(255)

    global ps
    ps.display()
    ps.update()

def mousePressed():
    global ps
    ps.shatter()
