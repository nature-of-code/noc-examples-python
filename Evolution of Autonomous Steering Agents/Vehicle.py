from p5 import *
import math
from random import *

mutation_rate = 0.01

def list_splice(target, start, delete_count=None, *items):
    """Remove existing elements and/or add new elements to a list.

    target        the target list (will be changed)
    start         index of starting position
    delete_count  number of items to remove (default: len(target) - start)
    *items        items to insert at start index

    Returns a new list of removed items (or an empty list)
    """
    if delete_count == None:
        delete_count = len(target) - start

    # store removed range in a separate list and replace with *items
    total = start + delete_count
    removed = target[start:total]
    target[start:total] = items

    return removed

class Vehicle:
    def __init__(self, x, y, dna = []):
        self.velocity = Vector(0, -2)
        self.position = Vector(x, y)
        self.acceleration = Vector(0, 0)
        self.r = 7
        self.maxspeed = 4
        self.maxforce = 0.4

        self.health = 1

        self.dna = []

        if (dna == []):
            self.dna = [randint(-2, 2), randint(-2, 2), randint(0, 100), randint(0, 100)]
        else:
            for i in range(len(dna)):
                self.dna.append(dna[i])
                if (random() < mutation_rate):
                    if (i < len(self.dna) - 2):
                        self.dna[i] += random_uniform(-0.1, 0.1)
                    else:
                        self.dna[i] += random_uniform(-10, 10)

        # self.dna.append(randint(-5, 5))
        # self.dna.append(randint(-5, 5))

    def update(self):

        self.health -= 0.005

        self.velocity += self.acceleration
        self.velocity.limit(self.maxspeed)
        self.position += self.velocity
        self.acceleration *= 0

    def applyForce(self, force):
        self.acceleration += force

    def eat(self, list, nutrition, perception):
        record = float('inf')
        closest = None
        for i in range(len(list)-1, -1, -1):
            d = self.position.dist(list[i])

            if (d < self.maxspeed):
                list_splice(list, i, 1)
                self.health += nutrition
            else:
                if (d < record and d < perception):
                    record = d
                    closest = list[i]

        if (closest != None):
            return self.seek(closest)

        return Vector(0, 0)

    def clone(self):
        if (random() < 0.003):
            return Vehicle(self.position.x, self.position.y, self.dna)

    def behaviors(self, good, bad):
        steerG = self.eat(good, 0.2, self.dna[2])
        steerB = self.eat(bad, -0.3, self.dna[3])

        steerG *= self.dna[0]
        steerB *= self.dna[1]

        self.applyForce(steerG)
        self.applyForce(steerB)

    def seek(self, target):
        desired = target - self.position
        desired.magnitude = self.maxspeed
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        # self.applyForce(steer)

        return steer

    def dead(self):
        return (self.health < 0)

    def boundaries(self):
        d = 25
        desired = None

        if (self.position.x < d):
            desired = Vector(self.maxspeed, self.velocity.y)
        elif (self.position.x > width - d):
            desired = Vector(-self.maxspeed, self.velocity.y)


        if (self.position.y < d):
            desired = Vector(self.velocity.x, self.maxspeed)
        elif (self.position.y > height - d):
            desired = Vector(self.velocity.x, -self.maxspeed)


        if (desired != None):
            desired.normalize()
            desired *= self.maxspeed
            steer = desired - self.velocity
            steer.limit(self.maxforce)
            self.applyForce(steer)


    def display(self):
        angle = self.velocity.angle + (math.pi/2)
        push_matrix()

        translate(self.position.x, self.position.y)
        rotate(angle)

        stroke(0, 255, 0)
        no_fill()
        ellipse((0, 0), self.dna[2]*2, self.dna[2]*2)
        stroke(255, 0, 0)
        no_fill()
        ellipse((0, 0), -self.dna[3]*2, self.dna[3]*2)

        col = Color(0, 0, 255).lerp(Color(0, 255, 0), self.health)
        fill(col)
        stroke(0)
        stroke_weight(1)
        begin_shape()
        vertex(0, -self.r*2)
        vertex(-self.r, self.r*2)
        vertex(self.r, self.r*2)
        end_shape('CLOSE')
        reset_matrix()
