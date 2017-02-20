# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Collisions -- Elastic, Equal Mass, Two objects only

# Based off of Chapter 9: Resolving Collisions
# Mathematics and Physics for Programmers by Danny Kodicek

# A Thing class for idealized collisions

# ported by: Jakub Pustelnik

from Mover import Mover

showVectors = True

def setup():
    global a, b
    size(200, 200)
    a = Mover(PVector(random(5), random(-5, 5)), PVector(10,10))
    b = Mover(PVector(-2,1), PVector(150,150))


def draw():
    global a, b, showVectors
    background(255)
    a.go(showVectors)
    b.go(showVectors)
    
    a.collideEqualMass(b)

def mousePressed() :
    global showVectors
    showVectors = not showVectors