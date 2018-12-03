# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Outline for game of life 
# This is just a grid of hexagons right now

from GOL import GOL

def setup():
    global gol
    size(600, 600)
    gol = GOL()


def draw():
    background(255)
    gol.display()

# reset board when mouse is pressed
def mousePressed():
    gol.init()
