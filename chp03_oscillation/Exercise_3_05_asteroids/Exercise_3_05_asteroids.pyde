# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Chapter 3: Asteroids exercise

from spaceship import Spaceship

def setup():
    size(640, 360)
    
    global ship
    ship = Spaceship()

def draw():
    background(255) 

    # Update position
    ship.update()
    
    # Wrape edges
    ship.wrapEdges()
    
    # Draw ship
    ship.display()


    fill(0)
    # text("left right arrows to turn, z to thrust", 10, height-5)

    # Turn or thrust the ship depending on what key is pressed
    if keyPressed:
        if (key == CODED) and (keyCode == LEFT):
            ship.turn(-0.03)
    
        elif (key == CODED) and (keyCode == RIGHT):
            ship.turn(0.03)
    
        elif (key == 'z') or (key == 'Z'):
            ship.thrust()