# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from walker import Walker


def setup():
    size(640, 360)
    # Create a walker object
    global w
    w = Walker()


def draw():
    background(255)
    # Run the walker object
    w.walk()
    w.display()

