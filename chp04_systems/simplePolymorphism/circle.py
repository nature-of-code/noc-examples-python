# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, r, c):
        # Call the parent constructor
        super(Circle, self).__init__(x, y, r)
        
        # Inherits all instance variables from parent + adding one
        # Also deal with the this new instance varibale
        self.c = c

    def jiggle(self):
        # Call the parent jiggle, but dos ome more stuff too.
        super(Circle, self).jiggle()

        # The circle jiggles its size as well as its x, y position
        self.r += random(-1, 1)
        self.r = constrain(self.r, 0, 100)

    def change_color(self):
        # The change_color() function is unique to the Circle class.
        self.c = color(random(255))

    def display(self):
        ellipseMode(CENTER)
        fill(self.c)
        stroke(0)
        ellipse(self.x, self.y, self.r, self.r)