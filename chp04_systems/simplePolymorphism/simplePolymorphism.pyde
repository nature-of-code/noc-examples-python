# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from circle import Circle
from square import Square

# A list of Shapes
shapes = []

def setup():
    size(200, 200)

    global shapes
    for i in range(30):
        r = int(random(0, 2))
        if r == 0:
            shapes.append(Circle(100, 100, 10, color(random(255), 100)))
        else:
            shapes.append(Square(100, 100, 10))

def draw():
    background(255)
    global shapes

    for shape in shapes:
        shape.jiggle()
        shape.display()