# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

class GOL():

    W = 8

    def __init__(self):
        # Initialize self.rows, self.cols and set-up a list of lists
        self.cols = width / GOL.W
        self.rows = height / GOL.W
        # Game of life board
        self.board = [[0] * self.rows for _ in range(self.cols)]
        # Call function to fill array with random values 0 or 1
        self.init()

    def init(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.board[i][j] = int(random(2))

    # The process of creating the new generation
    def generate(self):

        next = [[0] * self.rows for _ in range(self.cols)]

        # Loop through every spot in our 2D array and check spots neighbors
        for x in range(self.cols):
            for y in range(self.rows):
                # Add up all the states in a 3x3 surrounding grid
                neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nx = (x + i + self.cols) % self.cols
                        ny = (y + j + self.rows) % self.rows
                        neighbors += self.board[nx][ny]
                # A little trick to subtract the current cell's state since
                # we added it in the above loop
                neighbors -= self.board[x][y]
                # Rules of Life
                # Loneliness
                if self.board[x][y] == 1 and neighbors < 2:
                    next[x][y] = 0
                # Overpopulation
                elif self.board[x][y] == 1 and neighbors > 3:
                    next[x][y] = 0
                # Reproduction
                elif self.board[x][y] == 0 and neighbors == 3:
                    next[x][y] = 1
                # Stasis
                else:
                    next[x][y] = self.board[x][y]
        # Next is now our board
        self.board = next

    # The easy part, draw the cells, fill 255 for '1', fill 0 for '0'
    def display(self):
        background(255)
        for i in range(self.cols):
            for j in range(self.rows):
                if (self.board[i][j] == 1):
                    fill(0)
                else:
                    fill(255)
                stroke(0)
                rect(i * GOL.W, j * GOL.W, GOL.W, GOL.W)
