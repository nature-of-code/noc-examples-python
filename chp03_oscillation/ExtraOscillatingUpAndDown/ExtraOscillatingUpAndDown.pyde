# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle = 0

def setup():
    size(400, 400)

def draw():
    background(255)
    global angle

    y = 100*sin(angle)
    angle += 0.02

    fill(127)
    translate(width/2, height/2)
    line(0, 0, 0, y)
    ellipse(0, y, 16, 16)
