# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

# A class for a draggable attractive body in our world

class Attractor(object):

    def __init__(self):
        self.position = PVector(width/2, height/2)  # Position
        self.mass = 10  # Mass, tied to size

        # holds the offset when the object is clicked on 
        self.drag = PVector(0.0, 0.0)
        
        self.dragging = False; # Is the object being dragged?
        self.rollover = False; # Is the mouse over the ellipse?

    def attract(self, m, g=0.4):
        # Calculate the direction of force
        force = PVector.sub(self.position, m.position)

        # Distance between objects
        d = force.mag()

        # Limiting the distance to eliminate "extreme" results for 
        # very close or very far objects
        d = constrain(d,5.0,25.0)

        # Normalize vector (distance doesn't matter here, we just
        # want this vector for direction)
        force.normalize();

        # Calculate gravitional force magnitude
        strength = (g * self.mass * m.mass)/float(d * d)

        # Get force vector --> magnitude * direction
        force.mult(strength)

        return force

    def display(self):
        ellipseMode(CENTER)
        stroke(0)
        if (self.dragging):
            fill (50)
        elif (self.rollover):
            fill(100);
        else:
            fill(0);
        ellipse(self.position.x, self.position.y, self.mass*6, self.mass*6);


    def clicked(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if (d < self.mass):
            self.dragging = True
            self.drag.x = self.position.x - mx
            self.drag.y = self.position.y - my

    def rollover(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if (d < self.mass):
            rollover = True
        else:
            rollover = False

    def stopDragging(self):
        self.dragging = False

    def drag(self):
        if (self.dragging):
            self.position.x = mouseX + self.drag.x
            self.position.y = mouseY + self.drag.y
