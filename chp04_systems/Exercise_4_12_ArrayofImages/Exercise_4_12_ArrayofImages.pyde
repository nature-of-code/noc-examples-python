# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port by Abhik Pal

from particle_system import ParticleSystem

# List of Images for particle textures
imgs = []

def setup():
    size(640, 360, P2D)

    global imgs, ps

    imgs.append(loadImage("corona.png"))
    imgs.append(loadImage("emitter.png"))
    imgs.append(loadImage("particle.png"))
    imgs.append(loadImage("texture.png"))
    imgs.append(loadImage("reflection.png"))
    
    ps = ParticleSystem(imgs)

def draw():
    # Additive blending!
    blendMode(ADD)

    background(0)
    global ps

    up = PVector(0, -0.2)
    ps.apply_force(up)

    ps.run()

    for i in range(5):
        ps.add_particle(mouseX, mouseY)