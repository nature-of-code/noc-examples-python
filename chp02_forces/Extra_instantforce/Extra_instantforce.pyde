# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

from mover import Mover

t = 0.0

def setup():
    size(640, 360)
    global m
    m = Mover()

def draw():
    background(255)

    global m, t

    wx = map(noise(t), 0, 1, -1, 1)
    wind = PVector(wx, 0)
    t += 0.01

    line(width/2, height/2, width/2 + wind.x*100, height/2 + wind.y*100)
    m.applyForce(wind)
  
    # Gravity
    gravity = PVector(0, 0.1)
    # m.applyForce(gravity);

    # Shake Force
    # m.shake();
  
    # Boundary force
    if (m.position.x > width - 50):
        boundary = PVector(-1,0)
        m.applyForce(boundary)
    elif (m.position.x < 50):
        boundary = PVector(1, 0)
        m.applyForce(boundary)

    m.update()
    m.display()

    # m.checkEdges()

def mousePressed():
    cannon = PVector.random2D()
    cannon.mult(5)

    global m
    m.applyForce(cannon)