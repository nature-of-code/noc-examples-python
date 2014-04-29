# Daniel Shiffman
# The Nature of Code
# http://www.shiffman.net/
# A random walker object!


class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2
        self.grid = []
        for _ in range(width):
            self.grid.append([False] * height)

    def render(self):
        stroke(0)
        line(self.x, self.y, self.x, self.y)

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        ok = False
        helpme = 0
        while not ok:
            choice = int(random(4))
            saveX = self.x
            saveY = self.y
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
            if not self.grid[self.x][self.y]:
                ok = True
                self.grid[self.x][self.y] = True
            else:
                self.x = saveX
                self.y = saveY

            helpme += 1
            if helpme > 1000:
                println("STUCK")
                noLoop()
                ok = True

