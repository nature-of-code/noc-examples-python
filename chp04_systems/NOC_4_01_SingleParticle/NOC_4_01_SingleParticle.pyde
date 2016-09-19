# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

def setup():
    size(200, 200)
    global p
    p = Particle(PVector(width/2, 10))
    smooth()
    
def draw():
    background(255)
    global p
    
    p.run()
    if p.is_dead():
        print("Particle Dead!")
