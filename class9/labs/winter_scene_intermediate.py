"""
winter_scene.py
===
Using the drawing and animation techniques we learned create an animation of snow falling.

1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Incorporate the code from multiple_objects.py to create the snow:
    a. However, in the setup, rather than use 0 for the initial y value, use a random value
    b. In the main loop, when iterating over the circles, check if the y value is greater than the window width (see screen_wrap.py)
    c. If the y value is greater... then bring the circle back up to the top
3. (INTERMEDIATE) Incorporate random lateral motion.  Try adding a unique velocity for x and y for each circle by expanding your two element list!  You can also use a dictionary if it makes more sense than a list with indexes.

"""
import pygame
import random

FRAME_RATE = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Black Forest"
NUM_CIRCLES = 50
large = 7
circles = []
Large = []
r = 20
r2 = 12

for c in range(NUM_CIRCLES):
    circles.append([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), random.randint(1,3), random.randint(-2,1)])

for c in range(large):
    Large.append([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), random.randint(1,3), random.randint(-2,1)])

background_color = (145,145,145)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

treeb = pygame.image.load("bfb.png").convert_alpha()
graphicrectb = treeb.get_rect()
bigb = pygame.transform.scale(treeb, (int(graphicrectb.right*1.37), int(graphicrectb.bottom*1.37)))

treef = pygame.image.load("bff.png").convert_alpha()
graphicrectf = treef.get_rect()
bigf = pygame.transform.scale(treef, (int(graphicrectf.right*1.37), int(graphicrectf.bottom*1.37)))

small_flake = pygame.image.load("sf.png").convert_alpha()
large_flake= pygame.image.load("lf.png").convert_alpha()
"""
color = tree.get_at((0,0))
tree.set_colorkey(color)
color2 = tree.get_at((0,0))
bigb.set_colorkey(color)
"""
"""
def set_alphas(color):
    if color == (255,255,255): # magenta means clear
        return (0,0,0,0)
    if color == (0,255,255): # cyan means shadow
        return (0,0,0,128)
    r,g,b = color
    return (r,g,b,255) # otherwise use the solid color from the image.
for row in range(smallgraphic.get_height()):
    for col in range(smallgraphic.get_width()):
        smallgraphic.set_at((row, col), set_alphas(smallgraphic.get_at((row, col))[:3]))
"""

while running == True:

    # stop the main loop when window is closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)
    # draw here
    
    
    screen.blit(bigb, (graphicrectb.right - 703, 0))
    for c in circles:
        #pygame.draw.ellipse(screen, (200,200,200), [c[0],c[1],r,20])
        #pygame.draw.ellipse(screen, (205, 140, 149), [c[0]+4,c[1]+4,r2,12])
        screen.blit(small_flake, (c[0], c[1]))
        #pygame.draw.circle(screen, (200, 200, 200), (c[0], c[1]), 10)
        #pygame.draw.circle(screen, (205, 140, 149), (c[0], c[1]), 6)
        screen.blit(bigf, (graphicrectf.right - 703, 0))
        
        c[1] += c[2] #velocity_y
        c[0] += c[3] #random lateral motion
        """
        for i in Large:
            screen.blit(large_flake, (c[0], c[1]))
            i[0] += i[2]
            i[1] += i[3]
            if (i[1] >= WINDOW_HEIGHT):
                i[1] = 0
            elif (i[0] >= WINDOW_WIDTH or i[0] <= 0):
                i[1] = -5
                i[0] = random.randint(WINDOW_WIDTH/5, WINDOW_WIDTH)
        """
        if (c[1] >= WINDOW_HEIGHT):
            c[1] = 0
        elif (c[0] >= WINDOW_WIDTH or c[0] <= 0):
            c[1] = -5
            c[0] = random.randint(WINDOW_WIDTH/5, WINDOW_WIDTH)
            
            """
        while r != 9:
            r-=1
            r2-=1
            """
    #pygame.draw.arc(screen, (0,0,0), [500,300,100,200], 0, 0.8, 3)
    #pygame.draw.arc(screen, (0,0,0), [WINDOW_WIDTH-300,WINDOW_HEIGHT-300,300,100], 0, 1.6)
    #screen.blit(tree, (0,0))
    
    clock.tick(FRAME_RATE)
    pygame.display.flip()
