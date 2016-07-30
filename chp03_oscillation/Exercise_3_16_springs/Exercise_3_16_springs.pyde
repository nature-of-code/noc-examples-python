# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from mover import Bob
from spring import Spring

def setup():
    size(640, 360)
    global bobs, springs
    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    bobs = [Bob(width/2, 100*k) for k in range(1, 4)]
    springs = [Spring(bobs[k], bobs[(k+1)%3], 100) for k in range(3)]

def draw():
    background(255) 
    global bobs, springs

    for s in springs:
        s.update()

    for s in springs:
        s.display()

    for b in bobs:
        b.update()
        b.display()
    
    bobs[0].drag(mouseX, mouseY)

def mousePressed():
    global bobs
    bobs[0].clicked(mouseX, mouseY)

def mouseReleased():
    global bobs
    bobs[0].stopDragging()

