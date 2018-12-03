# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Wolfram Cellular Automata

# A class to manage the CA

class CA():

    cell_size = 5

    def __init__(self, r):
        # A list to store the ruleset, for example:0,1,1,0,1,1,0,1
        self.ruleset = r
        # A list of 0s and 1s
        self.cells = [0] * (width / CA.cell_size)
        self.restart()

    # Make a random ruleset
    def randomize(self):
        for i in range(8):
            self.ruleset[i] = int(random(2))

    # Reset to generation 0
    def restart(self):
        for i in range(len(self.cells)):
            self.cells[i] = 0

        # We arbitrarily start with just the middle cell having a state of "1"
        self.cells[len(self.cells) / 2] = 1
        self.generation = 0

    # The process of creating the new generation
    def generate(self):
        # First we create an empty array for the new values
        nextgen = [0] * len(self.cells)
        # For every spot, determine new state by examing current state, and neighbor states
        # Ignore edges that only have one neighor
        for i in range(1, len(self.cells) - 1):
            left = self.cells[i - 1]   # Left neighbor state
            me = self.cells[i]       # Current state
            right = self.cells[i + 1]   # Right neighbor state
            # Compute next generation state based on ruleset
            nextgen[i] = self.rules(left, me, right)

        # The current generation is the new generation
        self.cells = nextgen
        self.generation += 1

    # This is the easy part, just draw the cells, fill 255 for '1', fill 0 for
    # '0'
    def display(self):
        for i, cell in enumerate(self.cells):
            if cell == 1:
                fill(0)
            else:
                fill(255)
            noStroke()
            rect(i * CA.cell_size,
                 self.generation * CA.cell_size,
                 CA.cell_size,
                 CA.cell_size)

    # Implementing the Wolfram rules
    # The convention is to put the 111 rule rule first, and 000 last
    # http://mathworld.wolfram.com/ElementaryCellularAutomaton.html

    # This would be the concise conversion to binary way
    # def rules(self, a, b, c):
    #     return self.ruleset[a<<2 | b<<1 | c]

    def rules(self, a, b, c):
        ruleset = self.ruleset
        if a == 1 and b == 1 and c == 1:
            return ruleset[0]
        if a == 1 and b == 1 and c == 0:
            return ruleset[1]
        if a == 1 and b == 0 and c == 1:
            return ruleset[2]
        if a == 1 and b == 0 and c == 0:
            return ruleset[3]
        if a == 0 and b == 1 and c == 1:
            return ruleset[4]
        if a == 0 and b == 1 and c == 0:
            return ruleset[5]
        if a == 0 and b == 0 and c == 1:
            return ruleset[6]
        if a == 0 and b == 0 and c == 0:
            return ruleset[7]
        return 0

    # The CA is done if it reaches the bottom of the screen
    def finished(self):
        return self.generation > height / CA.cell_size
