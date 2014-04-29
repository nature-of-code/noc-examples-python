# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# TIME
t = 0.0


def setup():
    size(400, 200)
    smooth()


def draw():
    global t
    background(255)
    xoff = t
    noFill()
    stroke(0)
    strokeWeight(2)
    beginShape()
    for i in range(width):
        y = noise(xoff) * height
        xoff += 0.01
        vertex(i, y)

    endShape()
    t += 0.01

