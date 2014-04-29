# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Landscape with height values according to Perlin noise

from landscape import Landscape

theta = 0.0


def setup():
    size(800, 200, P3D)
    # Create a landscape object
    global land
    land = Landscape(20, 800, 400)


def draw():
    global theta

    # Ok, visualize the landscape space
    background(255)
    pushMatrix()
    translate(width / 2, height / 2 + 20, -160)
    rotateX(PI / 3)
    rotateZ(theta)
    land.render()
    popMatrix()
    land.calculate()

    theta += 0.0025

