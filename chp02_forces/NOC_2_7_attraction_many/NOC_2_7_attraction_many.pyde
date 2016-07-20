# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover
from attractor import Attractor

def setup():
    size(640, 360)

    global movers
    movers = [Mover(random(0.1, 2), random(width), random(height)) \
                    for i in range(10)]

    global a
    a = Attractor()

def draw():
    background(255)

    a.display()
    a.drag()
    a.hover(mouseX, mouseY)

    for mover in movers:
        force = a.attract(mover)
        mover.applyForce(force)

        mover.update()
        mover.display()

def mousePressed():
    a.clicked(mouseX, mouseY)

def mouseReleased():
    a.stopDragging()
