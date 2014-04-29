# Daniel Shiffman
# The Nature of Code
# http://natureofcode.com

increment = 0.02


def setup():
    size(640, 360)
    noLoop()


def draw():
    background(0)

    # Optional: adjust noise detail here
    # noiseDetail(8,0.65)

    loadPixels()
    xoff = 0.0  # Start xoff at 0

    # For every x,y coordinate in a 2D space, calculate a noise value and
    # produce a brightness value
    for x in range(width):
        xoff += increment  # Increment xoff
        yoff = 0.0  # For every xoff, start yoff at 0
        for y in range(height):
            yoff += increment  # Increment yoff

            # Calculate noise and scale by 255
            bright = noise(xoff, yoff) * 255
            # Try using this line instead
            #bright = random(0,255)

            # Set each pixel onscreen to a grayscale value
            pixels[x + y * width] = color(bright)

    updatePixels()

