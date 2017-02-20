# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# ported by: Jakub Pustelnik
from Box import Box

# A list for all of our rectangles
boxes = []

def setup():
    size(640, 360)

def draw():
    background(255)

    if mousePressed:
        p = Box(mouseX, mouseY)
        boxes.append(p)

    for b in boxes:
        b.display()
