# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from cell import Cell

class GOL():

    W = 20
    H = sin(radians(60)) * W

    def __init__(self):
        # Initialize self.rows, self.cols and set-up a list of lists
        self.cols = width / int(GOL.W*3)
        self.rows = height / int(GOL.H)
        # Game of life board
        self.board = [[0] * self.rows for _ in range(self.cols)]
        # Call function to fill array with random values 0 or 1
        self.init()

    def init(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if j % 2 == 0:
                    self.board[i][j] = Cell(i * GOL.W * 3,
                                            j * GOL.H,
                                            GOL.W)
                else:
                    self.board[i][j] = Cell(i * GOL.W * 3 + GOL.W + GOL.W / 2,
                                            j * GOL.H,
                                            GOL.W)

    
    # The easy part, draw the cells, fill 255 for '1', fill 0 for '0'
    def display(self):
        background(255)
        for i in range(self.cols):
            for j in range(self.rows):
                self.board[i][j].display()
