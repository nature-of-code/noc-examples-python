# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from attractor import Attractor
from mover import Mover

max_movers = 20
g = 1

def setup():
    size(640, 360)
    global a
    a = Attractor()

    global movers
    movers = [Mover(random(4, 12),random(width),random(height)) \
                for i in range(max_movers)]

def draw():
    background(255)

    a.display()

    for mover in movers:
        for other_mover in movers:
            if mover != other_mover:
                force = other_mover.repel(mover)
                mover.applyForce(force)
        
        force = a.attract(mover)
        mover.applyForce(force)
        mover.update()
        mover.display()