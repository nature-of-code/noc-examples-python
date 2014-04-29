# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


def setup():
    size(640, 360)
    background(255)


def draw():
    # Get a gaussian random number w/ mean of 0 and standard deviation of 1.0
    xloc = randomGaussian()
    sd = 60  # Define a standard deviation
    # Define a mean value (middle of the screen along the x-axis)
    mean = width / 2
    # Scale the gaussian random number by standard deviation and mean
    xloc = (xloc * sd) + mean
    fill(0, 10)
    noStroke()
    # Draw an ellipse at our "normal" random location
    ellipse(xloc, height / 2, 16, 16)

