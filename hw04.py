#Name:      Karl Glander
#Drexel ID: kg3338
#Date:      05/13/2025
#Purpose:   The main document for my game, includes the initialization of most of the important variables as well as the main game loop 

import pygame, time, random
from fly import *
from frog import *
from text import *
from projectile import *
from lazer import *

pygame.init()
surface = pygame.display.set_mode((800,600))

#Instantiating Important Classes 
mayFly = Fly(400, 400, 10, (0, 0, 0))
froggy = Frog(400,300)
scoreboard = Text("Score: 0",10,10)
gameover = Text("Game Over", 280, 200,(255,255,255),40)
score = Text("Score: 0",300,250,(255,255,255),25)
health = Text("Health: 10", 10, 40)

#Instantiating essential variables
numEaten = 0
frame = 0
startTime = 0
attack = 0
projectiles = []# an array to hold all of the currently active projectiles, pass this into a function for choosing and excecuting attacks
lazers = []


fpsClock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mayFly.getHealth() < 1:
        surface.fill((200,0,0))
        score.setMessage(f"Score: {frame}")
        gameover.draw(surface)
        score.draw(surface)

    else:
        frame += 1
        surface.fill((0,100,255))#Drawing the Surface
        pygame.draw.circle(surface, (0,100,0),(400,300),300)
        pygame.draw.circle(surface, (0,50,0), (400,300),300, 5)
    
    
        if mayFly.isInv():
            mayFly.dashTimer()
    
        #---------------MOVEMENT!!!!-----------------------
        #Its possible that I could move this into the mayFly class
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if keys[pygame.K_w] or keys[pygame.K_s]:
                mayFly.keyMove(-0.7,0)
            else:
                mayFly.keyMove(-1, 0)
        if keys[pygame.K_d]:
            if keys[pygame.K_w] or keys[pygame.K_s]:
                mayFly.keyMove(0.7, 0)
            else:
                mayFly.keyMove(1, 0)
        if keys[pygame.K_w]:
            if keys[pygame.K_a] or keys[pygame.K_d]:
                mayFly.keyMove(0, -0.7)
            else:
                mayFly.keyMove(0, -1)
        if keys[pygame.K_s]:
            if keys[pygame.K_a] or keys[pygame.K_d]:
                mayFly.keyMove(0, 0.7)
            else:
                mayFly.keyMove(0, 1)
    
        if keys[pygame.K_SPACE]:
            mayFly.dash()
    
    
        #---------------FROG ATTACKS-----------------------
    
        def choose(num):
            return random.randint(1,num)
    
        if time.perf_counter() - startTime > 10 and frame > 200:
            startTime = time.perf_counter()
            lazers = []
            attack = choose(4)
            if attack == 1:
                #instantiating lazers for attack 2 so that it can just focus on spinning them
                lazers.append(lazer((400,300),(500,300), False,0))
                lazers.append(lazer((400,300),(300,300), False,3.14))
                lazers.append(lazer((400,300),(500,300), False,1.57))
                lazers.append(lazer((400,300),(300,300), False,-1.57))
                    
    
        if attack == 0:
            froggy.standardAtt(mayFly, projectiles, frame)
        elif attack == 1:
            froggy.attack2( lazers)
            froggy.standardAtt(mayFly, projectiles, frame)
        elif attack ==2:
            froggy.attack3(mayFly, projectiles, frame)
        elif attack == 3:
            froggy.attack4(projectiles, frame)
        elif attack ==4: 
            froggy.attack5(mayFly, projectiles, frame)
    
    
        #--------------PROJECTIlES-------------------------
        for projectile in projectiles:
            projectile.check(projectiles)
            projectile.move()
            projectile.draw(surface)
            damage = projectile.collision(mayFly)
            if damage:
                projectiles.remove(projectile)
                health.setMessage(f"Health: {mayFly.getHealth()}")
                mayFly.damage()
        for lazAtt in lazers:
            lazAtt.draw(surface)
            damage = lazAtt.collision(mayFly)
            if damage:
                health.setMessage(f"Health: {mayFly.getHealth()}")
                mayFly.damage()
    
        #--------------DRAWING TIME------------------------
        mayFly.draw(surface)
        froggy.drawTrackLine(surface,mayFly.getLoc())
        froggy.draw(surface,mayFly.getLoc())


        scoreboard.setMessage(f"Score: {frame}")
        scoreboard.draw(surface)
        health.draw(surface)
    
        
    
    #don't change anything below here 
    #----------------------------------------------------
    
    pygame.display.update()
    fpsClock.tick(60)
    
    
exit()
