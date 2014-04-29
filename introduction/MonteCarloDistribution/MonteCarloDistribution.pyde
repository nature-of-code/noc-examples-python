# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


def setup():
    size(200, 200)
    global vals, norms
    vals = [0.0] * width   # Array to count how often a random # is picked
    norms = [0.0] * width  # Normalized version of above


def draw():
    background(100)
    # Pick a random number between 0 and 1 based on custom probability function
    n = montecarlo()
    # What spot in the array did we pick
    index = int(n * width)
    vals[index] += 1
    stroke(255)
    normalization = False
    maxy = 0.0
    # Draw graph based on values in norms array
    # If a value is greater than the height, set normalization to True
    for x, val in enumerate(vals):
        line(x, height, x, height - norms[x])
        if val > height:
            normalization = True
        if val > maxy:
            maxy = val

    # If normalization is True then normalize to height
    # Otherwise, just copy the info
    for x, val in enumerate(vals):
        if normalization:
            norms[x] = (val / maxy) * height
        else:
            norms[x] = val


def montecarlo():
    """
    An algorithm for picking a random number based on monte carlo method
    Here probability is determined by formula y = x
    """
    # let's count just so we don't get stuck in an infinite loop by accident
    hack = 0
    while hack < 10000:
        # Pick two random numbers
        r1 = random(1)
        r2 = random(1)
        y = r1 * r1  # y = x*x (change for different results)
        # If r2 is valid, we'll use this one
        if r2 < y:
            return r1
        hack += 1
    # Hack in case we run into a problem (need to improve this)
    return 0

