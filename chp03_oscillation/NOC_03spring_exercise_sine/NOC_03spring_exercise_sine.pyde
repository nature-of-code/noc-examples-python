# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle = 0
aVelocity = 0.05

def setup():
    size(640, 360)
    smooth()

def draw():
    background(255)
    global angle, aVelocity
    
    x = width/2
    y = map(sin(angle), -1, 1, 50, 250)
    angle += aVelocity

    ellipseMode(CENTER)
    stroke(0)
    fill(175)
    line(x, 0, x, y)
    ellipse(x, y, 20, 20)
