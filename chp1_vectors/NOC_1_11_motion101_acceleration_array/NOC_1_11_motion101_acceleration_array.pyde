# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Demonstration of the basics of motion with vector.
# A "Mover" object stores location, velocity, and acceleration as vectors
# The motion is controlled by affecting the acceleration (in this case
# towards the mouse)

from mover import Mover

moverCount = 20
movers = []


def setup():
    size(640, 360)
    for i in range(moverCount):
        movers.append(Mover())


def draw():
    background(255)
    for mover in movers:
        mover.update()
        mover.display()

