# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover
from attractor import Attractor

def setup():
    size(640, 360)
    
    global m
    m = Mover()

    global a
    a = Attractor()

def draw():
    background(255)

    force = a.attract(m)
    m.applyForce(force)
    m.update()

    a.drag()
    a.hover(mouseX, mouseY)

    a.display()
    m.display()

def mousePressed():
    a.clicked(mouseX, mouseY)

def mouseReleased():
    a.stopDragging()