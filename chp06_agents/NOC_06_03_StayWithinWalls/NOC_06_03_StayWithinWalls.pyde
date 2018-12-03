# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Stay Within Walls
# "Made-up" Steering behavior to stay within walls

from vehicle import Vehicle

debug = True
d = 25

def setup():
    global v
    size(640, 360)
    v = Vehicle(width / 2, height / 2)


def draw():
    background(255)

    if debug:
        stroke(175)
        noFill()
        rectMode(CENTER)
        rect(width / 2, height / 2, width - d * 2, height - d * 2)

    v.boundaries(d)
    v.run()

def mousePressed():
    global debug
    debug = not debug
