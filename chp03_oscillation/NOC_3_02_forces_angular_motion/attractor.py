# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Attractor(object):
    """A class for a draggable attractive body in our world"""
    def __init__(self, position=PVector(0, 0),
                    mass=20, g=0.4):
        self.position = position
        self.mass = mass
        self.g = g
        
    def attract(self, m):
        # Calculate the direction of force.
        force = PVector.sub(self.position, m.position)

        # Get the distance between the bodies using the force magnitude
        distance = force.mag()

        # Limit the distance to eliminate "extreme" results for very close
        # or very far objects
        distance = constrain(distance, 5.0, 25.0)

        # We are only interested in the direction, so normalize.
        force.normalize()

        # Calculate the gravitional force magnitude
        strength = (self.g * self.mass * m.mass)/(distance*distance)

        # Get force vector.
        force.mult(strength)

        return force

    def display(self):
        """Method to display"""
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 48, 48)
