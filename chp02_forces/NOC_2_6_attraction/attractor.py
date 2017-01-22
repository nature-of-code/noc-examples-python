# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

# A class for a draggable attractive body in our world

class Attractor(object):

    def __init__(self):
        self.position = PVector(width/2, height/2)  # Position
        self.mass = 20  # Mass, tied to size
        self.G = 1;     # Gravitational Constant

        # holds the offset when the object is clicked on 
        self.dragOffset = PVector(0.0, 0.0)
        
        self.dragging = False; # Is the object being dragged?
        self.rollover = False; # Is the mouse over the ellipse?

    def attract(self, m):
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
        strength = (self.G * self.mass * m.mass)/float(d * d)

        # Get force vector --> magnitude * direction
        force.mult(strength)

        return force

    def display(self):
        ellipseMode(CENTER)
        strokeWeight(4)
        stroke(0)
        if (self.dragging):
            fill (50)
        elif (self.rollover):
            fill(100);
        else:
            fill(175,200);
        ellipse(self.position.x, self.position.y, self.mass*2, self.mass*2);


    def clicked(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if (d < self.mass):
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def hover(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if (d < self.mass):
            rollover = True
        else:
            rollover = False

    def stopDragging(self):
        self.dragging = False

    def drag(self):
        if (self.dragging):
            self.position.x = mouseX + self.dragOffset.x
            self.position.y = mouseY + self.dragOffset.y