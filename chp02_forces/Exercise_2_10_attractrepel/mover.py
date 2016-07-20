# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    def __init__(self, m, x, y):
        self.mass = m
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0,0)
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        fill(175, 200)
        ellipse(self.position.x, self.position.y, self.mass*2, self.mass*2)

    def repel(self, m, g=0.4):
        force = PVector.sub(self.position, m.position)
        distance = force.mag()
        distance = constrain(distance, 1.0, 10000.0)
        force.normalize();

        strength = (g * self.mass * m.mass)/float(distance * distance)
        force.mult(-1*strength)
        return force

    def checkEdges(self):
        if self.position.x > width:
            self.position.x = width
            self.velocity.x *= -1
        elif selfself.position.x < 0:
            self.position.x = 0
            self.velocity.x *= -1

        if self.position.y > height:
            self.position.y = height
            self.velocity.y *= -1
        elif selfself.position.y < 0:
            self.position.y = 0
            self.velocity.y *= -1