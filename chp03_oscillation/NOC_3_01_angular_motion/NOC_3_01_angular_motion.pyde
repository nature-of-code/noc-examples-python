# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle = 0
aVelocity = 0
aAcceleration = 0.0001

def setup():
    size(800, 200)
    smooth()

def draw():
    global angle, aVelocity, aAcceleration
    
    background(255)

    fill(127)
    stroke(0)

    translate(width/2, height/2)
    rectMode(CENTER)
    rotate(angle)

    stroke(0)
    strokeWeight(2)
    fill(127)
    line(-60, 0, 60, 0)
    ellipse(60, 0, 16, 16)
    ellipse(-60, 0, 16, 16)

    angle += aVelocity;
    aVelocity += aAcceleration;

