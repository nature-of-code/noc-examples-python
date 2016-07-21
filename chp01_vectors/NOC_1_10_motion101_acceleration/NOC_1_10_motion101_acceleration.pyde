# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from mover import Mover


def setup():
    size(640, 360)
    global mover
    mover = Mover()


def draw():
    background(255)

    # Update the location
    mover.update()
    # Display the Mover
    mover.display()

