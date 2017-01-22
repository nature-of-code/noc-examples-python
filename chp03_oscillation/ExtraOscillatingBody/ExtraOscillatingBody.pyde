# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from attractor import Attractor
from mover import Mover

def setup():
    global a, m
    size(640, 360)
    m = Mover() 
    a = Attractor()

def draw():
    global a, m
    background(255)

    force = a.attract(m)
    m.applyForce(force)
    m.update()

    a.drag()
    a.hover(mouseX, mouseY)

    a.display()
    m.display()

def mousePressed():
    global a
    a.clicked(mouseX, mouseY) 

def mouseReleased():
    global a
    a.stopDragging() 
