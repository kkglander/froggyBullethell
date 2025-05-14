# WINTER WONDERLAND!!!!!!!
# Matt Flynn; mf3422; Karl Glander kg3338

# import necessary modules and classes
import pygame
import random as r

from drawable import *

# initialize Pygame and create window
pygame.init()
width = 500
height = 500
surface = pygame.display.set_mode((width, height))

ground = Rectangle(0, 300, 500, 300, (0, 255, 0))  # use to test Rectangle - may need to remove later
sky = Rectangle(0, 000, 500, 300, (0, 0, 255))  # use to test Rectangle - may need to remove later
snowflakes = []
stuck = []
snowflakes.append(Snowflake(50, 50))  # use to test Rectangle - may need to remove later
# the game loop
moving = True
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (
            event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_q
        ):
            pygame.quit()
            exit()
        if (event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_SPACE):
            moving = not moving
    if moving:
        snowflakes.append(Snowflake(r.randint(0,500)))

    ground.draw(surface)  # use to test Rectangle - may need to remove later
    sky.draw(surface)  # use to test Rectangle - may need to remove later
    for snowflake in snowflakes:
        x,y = snowflake.getLoc()
        if moving:
            snowflake.setLoc((x,y+1))
        if y+1 > snowflake.getMaxY():
            stuck.append(snowflake)
            snowflakes.remove(snowflake)
        else:
            snowflake.draw(surface)

    for snowflake in stuck:
        snowflake.draw(surface)


    pygame.display.update()
