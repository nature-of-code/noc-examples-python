# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from shape import Shape

class Square(Shape):
    # Varibales are inherited from the parent
    # We could also add variables unique to the Square class if we so desire

    # Inherits __init__() and jiggle() from the parent

    def display(self):
        """The square overrides its parent for display"""
        rectMode(CENTER)
        fill(175)
        stroke(0)
        rect(self.x, self.y, self.r, self.r)
