# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover

def setup():
    size(640, 360)
    global movers
    movers = []
    for i in range(20):
        movers.append(Mover(random(1, 4), 0, 0))

def draw():
    background(255)

    for m in movers:
        wind = PVector(0.01, 0)
        gravity = PVector(0, 0.1*m.mass)

        m.applyForce(wind)
        m.applyForce(gravity)

        m.update()
        m.display()
        m.checkEdges()
