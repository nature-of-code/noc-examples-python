# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Attractor(object):
    # Attraction
    # A class for a draggable attractive body in our world

    def __init__(self):
        # position
        self.pos = PVector(width/2, height/2)
        
        # Mass, tied to size
        self.mass = 20
        
        # Gravitational Constant
        self.G = 1
        
        # holds the offset for when object is clicked on
        self.dragOffset = PVector(0.0, 0.0)

        
        # Is the object being dragged?
        self.dragging = False
        
        # Is the mouse over the ellipse?
        self.rollover_state = False

    def go(self):
        self.render()
        self.drag()

    def attract(self, m):
        # Calculate direction of force
        direction = PVector.sub(self.pos, m.position)
        
        # Distance between objects
        d = direction.mag()
        
        # Limiting the distance to eliminate "extreme" results for very
        # close or very far objects
        d = constrain(d, 5.0, 25.0)
        
        # Normalize vector (distance doesn't matter here, we just want
        # this vector for direction)
        direction.normalize()
        
        # Calculate gravitional force magnitude
        force = (self.G * self.mass * m.mass) / (d * d)
        
        # Get force vector --> magnitude * direction
        direction.mult(force)
        
        return direction


    def display(self):
        # Method to display
        ellipseMode(CENTER)
        strokeWeight(4)
        stroke(0)

        if self.dragging:
            fill (50)
        elif self.rollover_state:
            fill(100)
        else:
            fill(175, 200)
        
        ellipse(self.pos.x, self.pos.y, self.mass*2, self.mass*2)

    def clicked(self, mx, my):
        # The methods below are for mouse interaction
        d = dist(mx, my, self.pos.x, self.pos.y)
        
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.pos.x - mx
            self.dragOffset.y = self.pos.y - my

    def hover(self, mx, my):
        d = dist(mx, my, self.pos.x, self.pos.y)
        
        if d < self.mass:
            self.rollover_state = True
        else:
            self.rollover_state = False

    def stopDragging(self):
        self.dragging = False

    def drag(self):
        if (self.dragging):
            self.pos.x = mouseX + self.dragOffset.x
            self.pos.y = mouseY + self.dragOffset.y