# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Collisions

# ported by: Jakub Pustelnik

class Mover:

    def __init__(self, v, l):
        self.vel = v.copy()
        self.loc = l.copy()
        self.bounce = 1.0
        self.r = 20
        self.colliding = False

    # Main method to operate object
    def go(self, s):
        self.update()
        self.borders()
        self.display(s)

    # Method to update location
    def update(self):
        self.loc.add(self.vel)

    # Check for bouncing off borders
    def borders(self):
        if self.loc.y > height:
            self.vel.y *= -self.bounce
            self.loc.y = height
        elif self.loc.y < 0:
            self.vel.y *= -self.bounce
            self.loc.y = 0

        if self.loc.x > width:
            self.vel.x *= -self.bounce
            self.loc.x = width
        elif self.loc.x < 0:
            self.vel.x *= -self.bounce
            self.loc.x = 0

    # Method to display
    def display(self, showVectors):

        ellipseMode(CENTER)
        stroke(0)
        fill(175, 200)
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)

        if showVectors:
            self.drawVector(self.vel, self.loc, 10.0)

    # draw vector moved here for simplicity
    def drawVector(self, v, pos, scayl):
        pushMatrix()
        arrowsize = 4

        # Translate to position to render vector
        translate(pos.x, pos.y)
        stroke(0)

        # Call vector heading function to get direction
        # (note that pointing up is a heading of 0) and rotate
        rotate(v.heading())

        # Calculate length of vector & scale it to be bigger or smaller if necessary
        # len is renamed to leng because len is a python key word
        leng = v.mag() * scayl

        # Draw three lines to make an arrow
        # (draw pointing up since we've rotate to the proper direction)
        line(0, 0, leng, 0)
        line(leng, 0, leng - arrowsize, +arrowsize / 2)
        line(leng, 0, leng - arrowsize, -arrowsize / 2)

        popMatrix()

    def collideEqualMass(self, other):
        d = PVector.dist(self.loc, other.loc)
        sumR = self.r + other.r

        # Are they colliding?
        if not self.colliding and d <= sumR:
            # Yes, make new velocities!
            self.colliding = True

            # Direction of one object another
            n = PVector.sub(other.loc, self.loc)
            n.normalize()

            # Difference of velocities so that we think of one object as
            # stationary
            u = PVector.sub(self.vel, other.vel)

            # Separate out components -- one in direction of normal
            un = componentVector(u, n)

            # Other component
            u.sub(un)

            # These are the new velocities plus the velocity
            # of the object we consider as stastionary
            self.vel = PVector.add(u, other.vel)
            other.vel = PVector.add(un, other.vel)
        elif d > sumR:
            self.colliding = False

def componentVector(vector, directionVector):
    # The function arguments are vector, directionVector (2D vectors), and it
    # returns the component vector of vector in the direction directionVector.

    # normalize directionVector
    directionVector.normalize()
    directionVector.mult(vector.dot(directionVector))

    return directionVector

# draw vector moved here for simplicity
def drawVector(self, v, pos, scayl):
    pushMatrix()
    arrowsize = 4.0

    # Translate to position to render vector
    translate(pos.x, pos.y)
    stroke(0)

    # Call vector heading function to get direction
    # (note that pointing up is a heading of 0) and rotate
    rotate(v.heading())

    # Calculate length of vector & scale it to be bigger or smaller if necessary
    # len is renamed to leng because len is a python key word
    leng = v.mag() * float(scayl)

    # Draw three lines to make an arrow (draw pointing up since
    # we've rotate to the proper direction)
    line(0, 0, leng, 0)
    line(leng, 0, leng - arrowsize, +arrowsize / 2)
    line(leng, 0, leng - arrowsize, -arrowsize / 2)
