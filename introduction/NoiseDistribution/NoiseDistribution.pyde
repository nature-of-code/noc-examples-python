# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Testing Distribution of Perlin Noise generated #'s vs. Randoms

xoff = 0.0


def setup():
    size(300, 200)
    global vals, norms
    vals = [0.0] * width
    norms = [0.0] * width


def draw():
    background(100)
    global xoff
    n = noise(xoff)
    index = int(n * width)
    vals[index] += 1
    xoff += 0.01
    stroke(255)
    normalization = False
    maxy = 0.0
    for x, val in enumerate(vals):
        line(x, height, x, height - norms[x])
        if val > height:
            normalization = True
        if val > maxy:
            maxy = vals[x]

    for x, val in enumerate(vals):
        if normalization:
            norms[x] = (val / maxy) * height
        else:
            norms[x] = val

