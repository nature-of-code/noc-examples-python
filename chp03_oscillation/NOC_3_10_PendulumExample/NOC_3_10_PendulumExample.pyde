# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Pendulum
#
# A simple pendulum simulation
# Given a pendulum with an angle theta (0 being the pendulum at rest) and
# a radius r we can use sine to calculate the angular component of the 
# gravitational force.
# 
# Gravity Force = Mass * Gravitational Constant;
# Pendulum Force = Gravity Force * sine(theta)
# Angular Acceleration = 
#       Pendulum Force / Mass = gravitational acceleration * sine(theta);
# 
# Note this is an ideal world scenario with no tension in the pendulum arm, 
# a more realistic formula might be: 
#       Angular Acceleration = (g / R) * sine(theta)
# 
# For a more substantial explanation, visit:
# http://www.myphysicslab.com/pendulum1.html 

from pendulum import Pendulum

def setup():
    size(640, 360)
    
    # Make a new Pendulum with an origin position and armlength
    global p
    p = Pendulum(PVector(width/2, 0), 175)

def draw():
    background(255)
    p.go()

def mousePressed():
    p.clicked(mouseX, mouseY)

def mouseReleased():
    p.stopDragging()
