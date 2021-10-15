# The Nature of Code
# Daniel Shiffman
# https://natureofcode.com

# Recursive Tree
# Renders a simple tree-like structure via recursion
# Branching angle calculated as a def of horizontal mouse position

def setup():
    size(640, 360)

    
def draw():
    global theta
    background(255)
    # Let's pick an angle 0 to 90 degrees based on the mouse position
    theta = map(mouseX, 0, width, 0, PI / 2)
    # Start the tree from the bottom of the screen
    translate(width / 2, height)
    stroke(0)
    branch(120)

    
def branch(lenght):
    # Each branch will be 2/3rds the size of the previous one

    #sw = map(lenght, 2, 120, 1, 10)
    # strokeWeight(sw)
    strokeWeight(2)
    line(0, 0, 0, -lenght)
    # Move to the end of that line
    translate(0, -lenght)

    lenght *= 0.66
    # All recursive functions must have an exit condition!!!!
    # Here, ours is when the lenghtgth of the branch is 2 pixels or less
    if lenght > 2:
        # Save the current state of transformation (i.e. where are we now)
        pushMatrix()
        rotate(theta)  # Rotate by theta
        branch(lenght)  # Ok, now call myself to draw two new branches!!
        # Whenever we get back here, we "pop" in order to
        # restore the previous matrix state
        popMatrix()
        # Repeat the same thing, only branch off to the "left" this time!
        pushMatrix()
        rotate(-theta)
        branch(lenght)
        popMatrix()
