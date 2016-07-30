# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

angle = 0
angleVel = 0.1

size(640, 360)

background(255)
stroke(0)
strokeWeight(2)
noFill()

beginShape()
for x in range(0, width+1, 5):
    y = map(sin(angle), -1, 1, 0, height)
    vertex(x, y)
    angle += angleVel
endShape()

