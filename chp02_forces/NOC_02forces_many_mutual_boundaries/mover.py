# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    def __init__(self, m, x, y):
        self.mass = m
        self.position = PVector(x, y)
        self.velocity = PVector(1, 0)
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
        ellipse(self.position.x, self.position.y, self.mass*16, self.mass*16)

    def attract(self, m, g=0.4):
        force = PVector.sub(self.position, m.position)
        distance = force.mag()
        distance = constrain(distance, 5.0, 25.0)
        force.normalize()

        strength = (g * self.mass * m.mass)/float(distance * distance)
        force.mult(strength)
        return force

    def boundaries(self):
        d = 50
        force = PVector(0, 0)

        if self.position.x < d:
            force.x = 1
        elif self.position.x > (width - d):
            force.x = -1
        
        if self.position.y < d:
            force.y = 1
        elif self.position.y > (height - d):
            force.y = -1

        force.normalize()
        force.mult(0.1)

        self.applyForce(force)
