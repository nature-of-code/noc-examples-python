# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# L-System
# Just demonstrating working with L-System strings
# No drawing

# Start with "A"
current = "A"
# Number of  generations
count = 0

def setup():
    size(800, 200)
    println("Generation {}: {}".format(count, current))

def draw():
    background(255)
    fill(0)
    text("Click mouse to generate", 10, height - 20)
    noLoop()

def mousePressed():
    global current, count

    # A new string for the next generation
    next_string = ""

    # Look through the current String to replace according to L-System rules
    for c in current:
        if c == 'A':
            # If we find A replace with AB
            next_string += "AB"
        elif c == 'B':
            # If we find B replace with A
            next_string += "A"

    # The current String is now the next one
    current = next_string
    count += 1
    # Print to message console
    println("Generation {}: {}".format(count, current))

