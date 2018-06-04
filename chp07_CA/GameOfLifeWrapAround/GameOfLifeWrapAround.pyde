# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Daniel Shiffman, Nature of Code

# A basic implementation of John Conway's Game of Life CA
# how could this be improved to use object oriented programming?
# think of it as similar to our particle system, with a "cell" class
# to describe each individual cell and a "cellular automata" class
# to describe a collection of cells

# Cells wrap around

from GOL import *

def setup():
    global gol
    size(400, 400)
    gol = GOL()


def draw():
    background(255)
    gol.generate()
    gol.display()

# reset board when mouse is pressed
def mousePressed():
    gol.init()
