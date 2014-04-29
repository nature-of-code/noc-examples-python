# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from walker import Walker


def setup():
    size(400, 400)
    frameRate(30)
    # Create a walker object
    global w
    w = Walker()


def draw():
    background(255)
    # Run the walker object
    w.walk()
    w.display()

