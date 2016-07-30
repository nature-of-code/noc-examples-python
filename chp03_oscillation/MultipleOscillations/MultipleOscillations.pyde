# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle1 = 0
aVelocity1 = 0.01
amplitude1 = 300
angle2 = 0
aVelocity2 = 0.3
amplitude2 = 10


def setup():
    size(640, 360)

def draw():
    global angle1, aVelocity1, amplitude1
    global angle2, aVelocity2, amplitude2
    background(255)

    x = 0
    x += amplitude1 * cos(angle1)
    x += amplitude2 * sin(angle2)

    angle1 += aVelocity1
    angle2 += aVelocity2

    ellipseMode(CENTER)
    stroke(0)
    fill(175)
    translate(width/2, height/2)
    line(0, 0, x, 0)
    ellipse(x, 0, 20, 20)
