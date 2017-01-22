# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

def setup():
    size(800, 200)

    global p
    p = Particle(PVector(width/2, 20))

    background(255)
    smooth()

def draw():
    global p

    if mousePressed:
        noStroke()
        fill(255, 5)
        rect(0, 0, width, height)

    p.run()
    if p.is_dead():
        print("Particle dead!")
