from p5 import *
from Vehicle import *
from random import *
import math

vehicles = []
food = []
poison = []

def setup():
    global v, food
    size(800, 600)

    for i in range(5):
        x = randint(0, width)
        y = randint(0, height)
        vehicles.append(Vehicle(x, y))

    for i in range(100):
        x = randint(0, width)
        y = randint(0, height)
        food.append(Vector(x, y))

    for i in range(40):
        x = randint(0, width)
        y = randint(0, height)
        poison.append(Vector(x, y))

def draw():
    background(25)

    if (random() < 0.07):
        x = randint(0, width)
        y = randint(0, height)
        food.append(Vector(x, y))

    if (random() < 0.005):
        x = randint(0, width)
        y = randint(0, height)
        poison.append(Vector(x, y))

    target = Vector(mouse_x, mouse_y)

    # stroke(255)
    # stroke_weight(2)
    # fill(127)
    # ellipse((target.x, target.y), 48, 48)

    for i in range(len(food)):
        fill(0, 255, 0)
        no_stroke()
        ellipse((food[i].x, food[i].y), 8, 8)

    for i in range(len(poison)):
        fill(255, 0, 0)
        no_stroke()
        ellipse((poison[i].x, poison[i].y), 8, 8)

    for i in range(len(vehicles)-1, -1, -1):
        vehicles[i].boundaries()
        vehicles[i].behaviors(food, poison)
        vehicles[i].update()
        vehicles[i].display()

        newVehicle = vehicles[i].clone()
        if (newVehicle):
            vehicles.append(newVehicle )

        if (vehicles[i].dead()):
            x = vehicles[i].position.x
            y = vehicles[i].position.y
            food.append(Vector(x, y))

            list_splice(vehicles, i, 1)




run()
