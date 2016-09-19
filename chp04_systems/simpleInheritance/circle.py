# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, r, c):
        """Inherits all instance variables from parent + adding one"""
        Shape.__init__(self, x, y, r)
        self.c = c

    def jiggle(self):
        """Call the parent for jiggle but do more stuff too."""
        super(Circle, self).jiggle()
        self.r += random(-1, 1)
        self.r = constrain(self.r, 0, 100)

    def change_color(self):
        """The change_color() method us unique to the Circle class"""
        self.c = color(random(255))

    def display(self):
        fill(self.c)
        stroke(0)
        ellipse(self.x, self.y, self.r, self.r)