# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

class Wave(object):
    def __init__(self, origin, w, a, p):
        
        # How far apart should each horizontal position be spaced
        self.xspacing = 8
        
        # Width of entire wave
        self.w = w

        # Where does the wave's first point start
        self.origin = origin.get()
        
        # Start angle at 0
        self.theta = 0.0
        
        # Height of wave
        self.amplitude = a
        
        # How many pixels before the wave repeats
        self.period = p
        
        # Value for incrementing X, to be calculated as a function of period 
        # and xspacing
        self.dx = (TWO_PI / self.period) * self.xspacing
        
        # Using an array to store height values for the wave (not entirely 
        # necessary)
        self.yvalues_length = w/self.xspacing
        self.yvalues = []

    def calculate(self):
        # Increment self.theta (try different values for 'angular velocity' here
        self.theta += 0.02

        # For every x value, calculate a y value with sine function
        x = self.theta
        self.yvalues = []
        for i in range(self.yvalues_length):
            self.yvalues.append(sin(x)*self.amplitude)
            x += self.dx

    def display(self):
        # A simple way to draw the wave with an ellipse at each position
        for x, yval in enumerate(self.yvalues):
            stroke(0)
            fill(0,50)
            ellipseMode(CENTER)
            ellipse(self.origin.x+x*self.xspacing, \
                    self.origin.y+yval, \
                    48, 48)
