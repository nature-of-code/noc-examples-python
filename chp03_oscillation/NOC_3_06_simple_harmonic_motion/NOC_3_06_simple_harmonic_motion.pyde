# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle = 0
aVelocity = 0.03

def setup():
    size(640, 360)
    smooth()


def draw():
    background(255)
    global angle, aVelocity

    amplitude = 300
    x = amplitude * sin(angle)
    angle += aVelocity

    ellipseMode(CENTER)
    stroke(0)
    fill(175)
    translate(width/2, height/2)
    line(0, 0, x, 0)
    ellipse(x, 0, 20, 20)