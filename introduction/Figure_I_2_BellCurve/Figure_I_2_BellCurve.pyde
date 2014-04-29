# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


def setup():
    size(400, 200)
    smooth()
    global heights
    heights = [0.0] * width


def draw():
    background(255)
    # "e", see http://mathforum.org/dr.math/faq/faq.e.html for more info
    e = 2.71828183
    m = 0  # default mean of 0
    sd = map(mouseX, 0, width, 0.4, 2)  # standard deviation based on mouseX
    for i in range(width):
        xcoord = map(i, 0, width, -3, 3)
        sq2pi = sqrt(2 * PI)  # square root of 2 * PI
        xmsq = -1 * (xcoord - m) * (xcoord - m)  # -(x - mu)^2
        sdsq = sd * sd  # variance (standard deviation squared)
        heights[i] = (1 / (sd * sq2pi)) * \
            (pow(e, (xmsq / sdsq)))  # P(x) function

    # a little for loop that draws a line between each point on the graph
    stroke(0)
    strokeWeight(2)
    noFill()
    beginShape()
    for x, h in enumerate(heights):
        vertex(x, map(h, 0, 1, height - 2, 2))
    endShape()

