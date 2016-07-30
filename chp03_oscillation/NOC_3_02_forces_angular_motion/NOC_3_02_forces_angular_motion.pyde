# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from attractor import Attractor
from mover import Mover

max_movers = 20


def setup():
    size(640, 360)
    
    global movers, a

    movers = [Mover(random(0.1, 2), random(width), random(height)) \
            for i in xrange(max_movers)]
    a = Attractor(position=PVector(width/2, height/2))

    background(255)

def draw():
    global a, movers
    
    background(255)
    a.display()

    for mv in movers:
        force = a.attract(mv)
        mv.applyForce(force)

        mv.update()
        mv.display()