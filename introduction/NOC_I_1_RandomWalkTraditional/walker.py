# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# A random walker object!


class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def render(self):
        stroke(0)
        point(self.x, self.y)

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        choice = int(random(4))

        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1

        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

