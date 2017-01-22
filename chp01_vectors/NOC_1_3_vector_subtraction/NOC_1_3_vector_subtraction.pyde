# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Example 1-3: Vector subtraction


def setup():
    size(640, 360)


def draw():
    background(255)

    mouse = PVector(mouseX, mouseY)
    center = PVector(width / 2, height / 2)
    mouse.sub(center)

    translate(width / 2, height / 2)
    strokeWeight(2)
    stroke(0)
    line(0, 0, mouse.x, mouse.y)

