# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Pendulum(object):
    """
    A Simple Pendulum Class
    Includes functionality for user can click and drag the pendulum
    """

    def __init__(self, origin, r):
        """
        This constructor could be improved to allow a greater variety of 
        pendulums
        """

        # position of pendulum ball
        self.position = PVector()

        # position of arm origin
        self.origin = origin.get()

        # Length of arm
        self.r = r

        # Pendulum arm angle
        self.angle = PI/4 

        # Angle velocity
        self.aVelocity = 0.0

        # Angle acceleration
        self.aAcceleration = 0.0 
        
        # Arbitary damping amount
        self.damping = 0.995

    def go(self):
        self.update()
        self.display()

    def update(self):
        """
        Function to update position
        """

        # Arbitrary constant
        gravity = 0.4

        # Calculate acceleration
        # (see: http://www.myphysicslab.com/pendulum1.html)
        self.aAcceleration = (-1 * gravity / self.r) * sin(self.angle)

        # Increment velocity
        self.aVelocity += self.aAcceleration

        # Arbitrary damping
        self.aVelocity *= self.damping

        # Increment angle
        self.angle += self.aVelocity

    def display(self):
        # Polar to cartesian conversion
        self.position.set(self.r*sin(self.angle), self.r*cos(self.angle), 0)

        #  Make sure the position is relative to the pendulum's origin
        self.position.add(self.origin)

        stroke(0)
        strokeWeight(2)
        
        # Draw the arm
        line(self.origin.x, self.origin.y, self.position.x, self.position.y)
        ellipseMode(CENTER)
        fill(175)
        
        # Draw the ball
        ellipse(self.position.x, self.position.y, 48, 48)