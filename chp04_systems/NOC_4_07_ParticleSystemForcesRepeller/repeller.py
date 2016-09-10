# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

# Particle + Forces

class Repeller(object):
    """A very basic repeller class."""
    def __init__(self, x, y):
        # Gravitational Constant
        self.G = 100

        # Position
        self.position = PVector(x, y)
        self.r = 10

    def repel(self, m):
        # Calculate the direction of force
        force = PVector.sub(self.position, m.position)

        # Distance between objects
        d = force.mag()

        # Limiting the distance to eliminate "extreme" results for 
        # very close or very far objects
        d = constrain(d, 5, 100)

        # Normalize vector (distance doesn't matter here, we just
        # want this vector for direction)
        force.normalize();

        # Calculate gravitional force magnitude
        strength = float(-1 * self.G)/float(d * d)

        # Get force vector --> magnitude * direction
        force.mult(strength)

        return force

    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(175)
        ellipse(self.position.x, self.position.y, self.r*2, self.r*2)