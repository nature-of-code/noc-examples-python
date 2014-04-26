# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Example 1-1: Bouncing Ball, no vectors

x = 100
y = 100
xspeed = 2.5
yspeed = 2


def setup():
    size(800, 200)
    smooth()


def draw():
    background(255)
    # Add the current speed to the location.
    global x, y, xspeed, yspeed
    x = x + xspeed
    y = y + yspeed
    if (x > width) or (x < 0):
        xspeed = xspeed * -1
    if (y > height) or (y < 0):
        yspeed = yspeed * -1
    # Display circle at x location
    stroke(0)
    strokeWeight(2)
    fill(127)
    ellipse(x, y, 48, 48)

