# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

#  A Polar coordinate, radius now starts at 0 to spiral outwards
r = 0
theta = 0

def setup():
    size(750, 200)
    background(255)
    smooth()

def draw():
    global r, theta

    # Polar to Cartesian conversion
    x = r * cos(theta)
    y = r * sin(theta)

    # Draw an ellipse at x, y
    noStroke()
    fill(0)
    
    # Adjust for center of window
    ellipse(x + width/2,  y + height/2,  16,  16) 

    # Increment the angle
    theta += 0.01

    # Increment the radius
    r += 0.05
