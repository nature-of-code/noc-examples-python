# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

class Cell():

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.xoff = w / 2
        self.yoff = sin(radians(60)) * w
        self.state = int(random(2))

    def display(self):

        fill(self.state * 255)
        stroke(0)
        with pushMatrix():
            translate(self.x, self.y)
            with beginShape():
                vertex(0, self.yoff)
                vertex(self.xoff, 0)
                vertex(self.xoff + self.w, 0)
                vertex(2 * self.w, self.yoff)
                vertex(self.xoff + self.w, 2 * self.yoff)
                vertex(self.xoff, 2 * self.yoff)
                vertex(0, self.yoff)
