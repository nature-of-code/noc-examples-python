# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from mover import Bob
from spring import Spring

bobs = [None for k in range(5)]
springs = [None for k in range(4)]

def setup():
    size(640, 360)
    global bobs, springs

    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    for i in range(len(bobs)):
        bobs[i] = Bob(width/2, i*40)

    for i in range(len(springs)):
        springs[i] = Spring(bobs[i], bobs[i+1],40)

def draw():
    background(255)
    global bobs, springs

    for s in springs:
        s.update()
        s.display()

    for b in bobs:
        b.update()
        b.display()
        b.drag(mouseX, mouseY)

def mousePressed():
    global bobs
    for b in bobs:
        b.clicked(mouseX, mouseY)

def mouseReleased():
    global bobs
    for b in bobs:
        b.stopDragging()
