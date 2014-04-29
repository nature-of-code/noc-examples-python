# Daniel Shiffman
# The Nature of Code
# http://www.shiffman.net/
from walker import Walker


def setup():
    size(600, 400)
    # Create a walker object
    global w
    w = Walker()
    background(255)


def draw():
    # Run the walker object
    w.step()
    w.render()

