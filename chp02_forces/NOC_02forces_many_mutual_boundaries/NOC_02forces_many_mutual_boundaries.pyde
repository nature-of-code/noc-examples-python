# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover
g = 0.4
max_movers = 20

def setup():
    size(640, 360)
    global movers

    movers = [Mover(random(1,2), random(width), random(height)) \
                for i in xrange(max_movers)]

def draw():
    background(255)

    for mover in movers:
        for other_mover in movers:
            if other_mover != mover:
                force = other_mover.attract(mover)
                mover.applyForce(force)

        mover.boundaries()
        mover.update()
        mover.display()
