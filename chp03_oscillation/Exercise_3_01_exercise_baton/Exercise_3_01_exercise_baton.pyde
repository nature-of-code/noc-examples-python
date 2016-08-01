# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle = 0

def setup():
    size(750, 150)
    smooth()

def draw():
    background(255)
    global angle

    fill(127)
    stroke(0)
    
    rectMode(CENTER)
    translate(width/2, height/2)
    rotate(angle)
    line(-50, 0, 50, 0)
    stroke(0)
    strokeWeight(2)
    fill(127)
    ellipse(50, 0, 16, 16)
    ellipse(-50, 0, 16, 16)
    
    angle += 0.05
