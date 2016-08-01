# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

# Attraction Array with Oscillating objects around each Crawler
# Click and drag attractive body to move throughout space\

from attractor import Attractor
from crawler import Crawler

crawlers = []
crawlers_num = 6

def setup():
    size(640, 360)
    global a, crawlers, crawlers_num
    
    # Some random bodies
    crawlers = [Crawler() for i in range(crawlers_num)]
    
    # Create an attractive body
    a = Attractor(PVector(width/2, height/2), 20, 0.4)

def draw():
    background(255)
    global a, crawlers

    a.rollover(mouseX, mouseY)
    a.go()

    for crawler in crawlers:
        # Calculate a force exerted by "attractor" on "Crawler"
        f = a.attract(crawler)
        
        # Apply that force to the Crawler
        crawler.applyForce(f)
        
        # Update and render
        crawler.update()
        crawler.display()

def mousePressed():
    global a
    a.clicked(mouseX, mouseY)

def mouseReleased():
    global a
    a.stopDragging()