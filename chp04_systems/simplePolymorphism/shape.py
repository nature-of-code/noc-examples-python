# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

class Shape(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def jiggle(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)

    def display(self):
        """
        A generic shape does not really know how to be fisplayed
        This will be overridden in the child classes.
        """
        point(self.x, self.y)
