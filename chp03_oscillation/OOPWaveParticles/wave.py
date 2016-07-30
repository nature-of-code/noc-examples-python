# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle import Particle

class Wave(object):

    def __init__(self, origin, wave_width, amplitude, period):
        # How far apart should each horizontal position be spaced
        self.xspacing = 8
        
        # Width of entire wave
        self.w = wave_width

        # Where does the wave's first point start
        self.origin = origin.get()

        # Start angle at 0
        self.theta = 0.0
        
        # Height of wave
        self.amplitude = amplitude
        
        # How many pixels before the wave repeats
        self.period = period

        # Value for incrementing X, to be calculated as a function of 
        # self.period and self.xspacing
        self.dx = (TWO_PI / self.period) * self.xspacing
        
        # Using an array to store height values for the wave (not entirely 
        # necessary)
        self. yvalues = []
        self.particles = [None for k in range((self.w/self.xspacing))]

        for i, particle in enumerate(self.particles):
            self.particles[i] = Particle()

    def calculate(self):
        # Increment self.theta (try different values for 'angular velocity' 
        # here
        self.theta += 0.02

        # For every x value, calculate a y value with sine function
        x = self.theta
        for i, particle in enumerate(self.particles):
            self.particles[i].setposition(self.origin.x+i*self.xspacing, \
                                        self.origin.y+sin(x)*self.amplitude)
            x += self.dx

    def manipulate(self):
        # Loop through the array of self.particles and check stuff regarding 
        # the mouse
        pass

    def display(self):
        # A simple way to draw the wave with an ellipse at each position
        for particle in self.particles:
            particle.display()
