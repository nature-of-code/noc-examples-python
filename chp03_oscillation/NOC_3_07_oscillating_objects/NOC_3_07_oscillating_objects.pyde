# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from oscillator import Oscillator

max_oscillators = 10

def setup():
    size(640, 360)
    smooth()
    
    # Initialize all objects
    global oscillators
    oscillators = [Oscillator() for i in range(max_oscillators)]

    background(255)

def draw():
    background(255)
    # Run all objects
    for oscillator in oscillators: 
        oscillator.oscillate()
        oscillator.display()




