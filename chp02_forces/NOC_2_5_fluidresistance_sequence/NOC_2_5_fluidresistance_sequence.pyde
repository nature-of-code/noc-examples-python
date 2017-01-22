# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

# Forces (Gravity and Fluid Resistence) with Vectors 

# Demonstration of multiple force acting on bodies (Mover class)
# Bodies experience gravity continuously
# Bodies experience fluid resistance when in "water"

from mover import Mover
from liquid import Liquid

def setup():
    size(450, 450)
    randomSeed(1)
    reset()

    global liquid
    liquid = Liquid(0, height/2, width, height/2, 0.1)

def draw():
    background(255)

    liquid.display()

    for mover in movers:

        # Is the Mover in the liquid?
        if liquid.contains(mover):
            # Calculate the drag force
            dragForce = liquid.drag(mover)
            # Apply the drag force
            mover.applyForce(dragForce)

        # Gravity is scaled by mass here!
        gravity = PVector(0, 0.1*mover.mass)
        # Apply gravity
        mover.applyForce(gravity)

        # update and display
        mover.update()
        mover.display()
        mover.checkEdges()

    fill(255)
    # text("click mouse to reset", 10, 30)
    if (frameCount % 20 == 0):
        saveFrame("ch2_05_#####.png")

def mousePressed():
    reset()

def reset():
    # restart all movers randomly
    global movers
    movers = [Mover(random(0.5*2.25, 3*2.25), 20*2.25 + i*40*2.25, 0) for i in range(5)]