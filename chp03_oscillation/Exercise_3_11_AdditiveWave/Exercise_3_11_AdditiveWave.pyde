# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Additive Wave
# Create a more complex wave by adding two waves together. 

# How far apart should each horizontal position be spaced
xspacing = 8

# total # of waves to add together
maxwaves = 5

theta = 0.0

# Height of wave
amplitude = []

# Value for incrementing X, to be calculated as a function of period
# and xspacing
dx = []

# Using an array to store height values for the wave (not entirely 
# necessary)
yvalues = []

def setup():
    size(750,200)
    global w, xspacing, maxwaves, theta, amplitude, dx, yvalues
    
    # Width of entire wave
    w = width + 16

    for i in range(maxwaves):
        amplitude.append(random(10,30))

        # How many pixels before the wave repeats
        period = random(100,300)
        dx.append((TWO_PI / period) * xspacing)

    yvalues = [None for k in range(w/xspacing)]

def draw():
    background(255)
    calcWave()
    renderWave()

def calcWave():
    global w, xspacing, maxwaves, theta, amplitude, dx, yvalues
    # Increment theta (try different values for 'angular velocity' here
    theta += 0.02

    # Set all height values to zero
    for i in range(len(yvalues)):
        yvalues[i] = 0


    # Accumulate wave height values
    for j in range(maxwaves):
        x = theta
        for i in range(len(yvalues)):
            # Every other wave is cosine instead of sine
            if j%2 == 0:
                yvalues[i] += sin(x)*amplitude[j]
            else:
                yvalues[i] += cos(x)*amplitude[j]
            x += dx[j]
    
def renderWave():
    global yvalues
    # A simple way to draw the wave with an ellipse at each position
    stroke(0)
    fill(127,50)
    ellipseMode(CENTER)
    for x, yval in enumerate(yvalues):
        ellipse(x*xspacing, height/2+yval, 48, 48)
