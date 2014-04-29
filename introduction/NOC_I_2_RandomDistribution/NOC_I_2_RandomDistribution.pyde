# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# An array to keep track of how often random numbers are picked

randomCounts = [0.0] * 20


def setup():
    size(640, 360)


def draw():
    background(255)

    # Pick a random number and increase the count
    index = int(random(len(randomCounts)))
    randomCounts[index] += 1

    # Draw a rectangle to graph results
    stroke(0)
    strokeWeight(2)
    fill(127)

    w = width / len(randomCounts)

    for x, r in enumerate(randomCounts):
        rect(x * w, height - r, w - 1, r)

