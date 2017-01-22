# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Liquid(object):
    def __init__(self, x, y, w,  h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def contains(self, m):
        l = m.position
        return (l.x > self.x) and (l.x < (self.x + self.w)) and \
                (l.y > self.y) and (l.y < (self.y + self.h))

    def drag(self, m):
        """
        Calculates the drag force
        """
        speed = m.velocity.mag()
        dragMagnitude = self.c * speed * speed

        dragForce = m.velocity.get()
        dragForce.mult(-1)

        # dragForce.setMag(dragMagnitude)
        dragForce.normalize()
        dragForce.mult(dragMagnitude)
        return dragForce

    def display(self):
        noStroke()
        fill(50)
        rect(self.x, self.y, self.w, self.h)