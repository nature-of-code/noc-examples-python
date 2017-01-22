# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover
g = 0.4

def setup():
    size(640, 360)
    global movers
    movers = [Mover(random(0.1, 2),random(width),random(height)) \ 
                for i in range(20)]

def draw():
    background(255)

    for mover in movers:
        for other_mover in movers:
            if (mover != other_mover):
                global g
                force = other_mover.attract(mover, g)
                mover.applyForce(force)
        
        mover.update()
        mover.display()