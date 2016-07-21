# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Example 1-5: Vector magnitude


def setup():
    size(640, 360)


def draw():
    background(255)

    mouse = PVector(mouseX, mouseY)
    center = PVector(width / 2, height / 2)
    mouse.sub(center)
    m = mouse.mag()
    fill(0)
    noStroke()
    rect(0, 0, m, 10)

    translate(width / 2, height / 2)
    stroke(0)
    strokeWeight(2)
    line(0, 0, mouse.x, mouse.y)

