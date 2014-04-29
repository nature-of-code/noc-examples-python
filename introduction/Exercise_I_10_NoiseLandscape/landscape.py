# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# "Landscape" example


class Landscape(object):

    def __init__(self, scl_,  w_,  h_):
        # size of each cell
        self.scl = scl_
        # width and height of thingie
        self.w = w_
        self.h = h_
        self.zoff = 0.0  # perlin noise argument
        # using an array to store all the height values
        self.z = []
        for _ in range(self.w / self.scl):
            self.z.append([0.0] * (self.h / self.scl))

    # Calculate height values (based off a neural netork)
    def calculate(self):
        xoff = 0
        for col in self.z:
            yoff = 0
            for row in range(len(col)):
                col[row] = map(noise(xoff, yoff, self.zoff), 0, 1, -120, 120)
                yoff += 0.1
            xoff += 0.1
        self.zoff += 0.01

    # Render landscape as grid of quads
    def render(self):
        # Every cell is an individual quad
        # (could use quad_strip here, but produces funny results, investigate this)
        z = self.z
        for x in range(len(z) - 1):
            for y in range(len(z[x]) - 1):
                # one quad at a time
                # each quad's color is determined by the height value at each vertex
                # (clean this part up)
                stroke(0)
                fill(100, 100)
                pushMatrix()
                beginShape(QUADS)
                translate(x * self.scl - self.w / 2, y * self.scl - self.h / 2, 0)
                vertex(0, 0, z[x][y])
                vertex(self.scl, 0, z[x + 1][y])
                vertex(self.scl, self.scl, z[x + 1][y + 1])
                vertex(0, self.scl, z[x][y + 1])
                endShape()
                popMatrix()

