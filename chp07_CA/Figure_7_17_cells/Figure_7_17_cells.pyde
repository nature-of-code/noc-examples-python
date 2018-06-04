# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

size(1800, 90)
w = 90
total = width / w
cells = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0,]

print "cells = [",
for i, cell in enumerate(cells):
    if cell == 0:
        fill(255)
    else:
        fill(64)
    stroke(0)
    rect(i * w, 0, w - 1, w - 1)
    print str(cell) + ", ",
print "]",

saveFrame("cells.png")
