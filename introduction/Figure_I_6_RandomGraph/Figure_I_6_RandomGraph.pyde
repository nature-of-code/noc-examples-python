# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


def setup():
    size(400, 200)
    smooth()


def draw():
    background(255)
    noFill()
    stroke(0)
    strokeWeight(2)
    beginShape()
    for i in range(width):
        y = random(height)
        vertex(i, y)
    endShape()
    noLoop()

