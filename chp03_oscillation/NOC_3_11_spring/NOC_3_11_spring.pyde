# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from mover import Bob
from spring import Spring

def setup():
    size(640, 360)

    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    global bob, spring
    spring = Spring(width/2, 10, 100) 
    bob = Bob(width/2, 100) 

def draw():
    background(255)
    global bob, spring
    
    # Apply a gravity force to the bob
    gravity = PVector(0, 2)
    bob.applyForce(gravity)

    # Connect the bob to the spring (this calculates the force)
    spring.connect(bob)
    
    # Constrain spring distance between min and max
    spring.constrainLength(bob, 30, 200)

    # Update bob
    bob.update()
    # If it's being dragged
    bob.drag(mouseX, mouseY)

    # Draw a line between spring and bob
    spring.displayLine(bob)

    # Draw everything else
    bob.display() 
    spring.display() 

    fill(0)
    text("click on bob to drag", 10, height-5)

# For mouse interaction with bob
def mousePressed():
    global bob
    bob.clicked(mouseX, mouseY)

def mouseReleased():
    global bob
    bob.stopDragging() 


