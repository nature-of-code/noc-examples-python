# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# ported by: Jakub Pustelnik

# A rectangular box
class Box:
    x = None
    y = None
    w = None
    h = None
    
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
    
    # Drawing the box
    def display(self):
        fill(127)
        stroke(9)
        strokeWeight(2)
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)
        