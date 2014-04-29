# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from walker import Walker

def setup():
    size(640, 360)
    global w
    w = Walker()
    background(0)


def draw():
    # Run the walker object
    w.step()
    w.render()

