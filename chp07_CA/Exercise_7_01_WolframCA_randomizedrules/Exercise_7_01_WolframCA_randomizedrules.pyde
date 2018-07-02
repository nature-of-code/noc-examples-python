# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Wolfram Cellular Automata

# Simple demonstration of a Wolfram 1-dimensional cellular automata
# When the system reaches bottom of the window, it restarts with a new ruleset
# Mouse click restarts as well

# import CA a class to describe a Wolfram elementary Cellular Automata
from CA import CA

delay = 0

def setup():
    global ca
    size(800, 200)
    background(255)
    ruleset = [0, 1, 0, 1, 1, 0, 1, 0]  # An initial rule system
    ca = CA(ruleset)                    # Initialize CA
    frameRate(30)


def draw():
    global delay
    ca.display()          # Draw the CA
    ca.generate()

    # If we're done, clear the screen, pick a new ruleset and restart
    if ca.finished():
        delay += 1
        if delay > 30:
            background(255)
            ca.randomize()
            ca.restart()
            delay = 0


def mousePressed():
    background(255)
    ca.randomize()
    ca.restart()
