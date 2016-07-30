# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from cannon_ball import CannonBall

# All of this stuff should go into a Cannon class
angle = -PI/4
position = PVector(50, 300)
shot = False

def setup():
    size(640, 360)

    global ball, position
    ball = CannonBall(position.x, position.y)

def draw():
    background(255)
    global angle, ball, position, shot

    pushMatrix()
    translate(position.x, position.y)
    rotate(angle)
    rect(0, -5, 50, 10)
    popMatrix()

    if shot:
        gravity = PVector(0, 0.2)
        ball.applyForce(gravity)
        ball.update()


    ball.display()

    if ball.position.y > height:
        ball = CannonBall(position.x, position.y)
        shot = False

def keyPressed():
    global angle, ball, shot

    if (key == CODED) and (keyCode == RIGHT):
        angle += 0.1
 
    elif (key == CODED) and (keyCode == LEFT):
        angle -= 0.1
 
    elif key == ' ':
        shot = True
        force = PVector.fromAngle(angle)
        force.mult(10)
        ball.applyForce(force)