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

        # Arbitrary ball radius
        self.ballr = 48 
        
        # Arbitary damping amount
        self.damping = 0.995
        
        self.dragging = False

    def go(self):
        self.update()
        self.drag()         # for user interaction
        self.display()

    def update(self):
        """
        Function to update position
        """
        # As long as we aren't dragging the pendulum, let it swing!
        if not self.dragging:
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

        if self.dragging:
            fill(0)
        
        # Draw the ball
        ellipse(self.position.x, self.position.y, self.ballr, self.ballr)

    # The methods below are for mouse interaction

    def clicked(self, mx, my):
        """
        This checks to see if we clicked on the pendulum ball
        """
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.ballr:
            self.dragging = True

    def stopDragging(self):
        """
        This tells us we are not longer clicking on the ball.
        """
        # No velocity once you let go
        self.aVelocity = 0 
        self.dragging = False

    def drag(self):
    # If we are draging the ball, we calculate the angle between the 
    # pendulum origin and mouse position we assign that angle to the 
    # pendulum
        if self.dragging:
            # Difference between 2 points
            diff = PVector.sub(self.origin, PVector(mouseX, mouseY))
            # Angle relative to vertical axis
            angle = atan2(-1*diff.y, diff.x) - radians(90)