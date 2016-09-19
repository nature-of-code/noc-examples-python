# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Object oriented programming allows us to define classes in terms of other 
# classes. A class can be a subclass (aka "child" ) of a super class (aka
# "parent"). This is a simple example demonstrating this concept, known as
# "inheritance."

from square import Square
from circle import Circle

def setup():
    size(200, 200)

    # A circle and a square
    global s, c
    s = Square(75, 75, 10)
    c = Circle(125, 125, 20, color(175))

def draw():
    background(255)
    global s, c

    c.jiggle()
    s.jiggle()

    c.display()
    s.display()
