# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A Mover object


class Mover(object):

    def __init__(self):
        # The Mover tracks location, velocity, and acceleration
        # Start in the center
        self.location = PVector(width / 2, height / 2)
        self.velocity = PVector(0, 0)
        # The Mover's maximum speed
        self.topspeed = 5

    def update(self):
        # Compute a vector that points from location to mouse
        mouse = PVector(mouseX, mouseY)
        acceleration = PVector.sub(mouse, self.location)
        # Set magnitude of acceleration
        acceleration.setMag(0.2)

        # Velocity changes according to acceleration
        self.velocity.add(acceleration)
        # Limit the velocity by topspeed
        self.velocity.limit(self.topspeed)
        # Location changes by velocity
        self.location.add(self.velocity)

    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.location.x, self.location.y, 48, 48)

