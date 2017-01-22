# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover

def setup():
    size(640, 360)
    global m
    m = Mover()

def draw():
    background(255)

    wind = PVector(0.01, 0)
    gravity = PVector(0, 0.1)

    m.applyForce(wind)
    m.applyForce(gravity)

    m.update()
    m.display()
    m.checkEdges()
