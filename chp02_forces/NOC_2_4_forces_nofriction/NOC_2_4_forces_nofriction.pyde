# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover

def setup():
    size(383, 200)
    randomSeed(1)

    global movers
    movers = [Mover(random(1, 4), random(width), 0) for i in range(5)]

def draw():
    background(255)

    for m in movers:

        wind = PVector(0.01, 0)
        gravity = PVector(0, 0.1*m.mass)

        c = 0.05
        friction = m.velocity.get()
        friction.mult(-1)
        friction.normalize()
        friction.mult(c)

        # m.applyForce(friction)
        m.applyForce(wind)
        m.applyForce(gravity)

        m.update()
        m.display()
        m.checkEdges()
