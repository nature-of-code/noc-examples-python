# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Sine Wave

from particle import Particle
from wave import Wave

def setup():
    size(640, 360)
    global wave0, wave1
    # Initialize a wave with starting point, width, amplitude, and period
    wave0 = Wave(PVector(200, 75), 100, 20, 500)
    wave1 = Wave(PVector(150, 250), 300, 40, 220)

def draw():
    background(255)
    global wave0, wave1

    # Update and display waves
    wave0.calculate()
    wave0.display()

    wave1.calculate()
    wave1.display()
