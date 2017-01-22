# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Smoke Particle System

# A basic smoke effect using a particle system
# Each particle is rendered as an alpha masked image

from particle_system import ParticleSystem

def setup():
    size(640, 360)
    img = loadImage("texture.png")
    global ps 
    ps = ParticleSystem(0, PVector(width/2, height-75), img)
    smooth()

def draw():
    background(0)
    global ps

    # Calculate the "wind" force based on mouse horizontal position
    dx = map(mouseX, 0, width, -0.2, 0.2)
    wind = PVector(dx, 0)
    ps.apply_force(wind)
    ps.run()

    for i in range(2):
      ps.add_particle()

    draw_vector(wind, PVector(width/2, 50, 0), 500)


def draw_vector(v, pos, scayl):
    """
    Renders a vector object `v` as an arrow and a position `pos`
    """
    pushMatrix()
    arrow_size = 4

    # Translate position to draw vector
    translate(pos.x, pos.y)
    stroke(255)

    # Call the vector heading fucntion to thet direction
    # (note that pointing up is a heading of 0)
    rotate(v.heading2D())

    # Calculate the length of the vector and scale it to be bigger or smaller
    # if necessary.
    length = v.mag() * scayl

    # Draw three lines to make an arrow
    # (draw pointing up since we've rotated to the proper direction)
    line(0, 0, length, 0);
    line(length, 0, length-arrow_size, arrow_size/2.0);
    line(length, 0, length-arrow_size, -arrow_size/2.0);

    popMatrix()