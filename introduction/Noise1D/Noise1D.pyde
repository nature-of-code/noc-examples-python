# Daniel Shiffman
# The Nature of Code
# http://natureofcode.com
xoff = 0.0
xincrement = 0.01


def setup():
    size(200, 200)
    background(0)
    noStroke()


def draw():
    # Create an alpha blended background
    fill(0, 10)
    rect(0, 0, width, height)

    # n = random(0,width)# Try this line instead of noise

    # Get a noise value based on xoff and scale it according to the window's
    # width
    global xoff
    n = noise(xoff) * width

    # With each cycle, increment xoff
    xoff += xincrement

    # Draw the ellipse at the value produced by perlin noise
    fill(200)
    ellipse(n, height / 2, 16, 16)

