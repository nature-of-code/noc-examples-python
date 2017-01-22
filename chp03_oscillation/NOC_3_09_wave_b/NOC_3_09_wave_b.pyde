# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

startAngle = 0
angleVel = 0.2

def setup():
    size(250, 200)
    smooth()

def draw():
    background(255)
    global startAngle, angleVel

    startAngle += 0.015
    angle = startAngle

    for x in range(0, width+1, 24):
        y = map(sin(angle), -1, 1, 0, height)
        
        stroke(0)
        fill(0, 50)
        strokeWeight(2)
        ellipse(x, y, 48, 48)
        
        angle += angleVel
