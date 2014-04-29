# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from walker import Walker

w = []


def setup():
    size(600, 400)


def draw():
    background(255)
    o = int(map(mouseX, 0, width, 1, 8))
    noiseDetail(o, 0.3)
    if frameCount % 30 == 0 and len(w) < 10:
        w.append(Walker())
    for walker in w:
        walker.walk()
        walker.display()

