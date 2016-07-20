# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from attractor import Attractor
from mover import Mover

max_movers = 10
angle = 0

a = Attractor()

def setup():
    size(640, 360, P3D)
    background(255)
    
    global movers
    movers = [Mover(random(0.1, 2), random(-width/2, width/2), \
                random(-height/2, height/2), random(-100,100)) \
                for i in xrange(max_movers)]

def draw():
    global angle, a
    background(0)
    sphereDetail(8)
    lights()
    translate(width/2, height/2)
    
    rotateY(angle)

    a.display()

    for mover in movers:
        force = a.attract(mover)
        mover.applyForce(force)
        mover.update()
        mover.display()

    angle += 0.003