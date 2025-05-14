#Name:      Karl Glander
#Drexel ID: kg3338
#Date:      05/13/2025
#Purpose:   This file holds the fly class, which is the player controlled character


import pygame, random, time, math
from drawable import *

#TODO:
# [x] - Perhaps make the Fly hitbox into a pentagon for slightly more accurate hitbox
# [x] - Add I frames
# [x] - Fix dash period so that you can't just hold down
# [x] - Fix the diagonal dashing

class Fly(Drawable):

    def __init__(self,x = 0,y = 0, radius = 10,color = (0, 0, 0)):
        super().__init__(x, y)
        self.__health = 10
        self.__color = color
        self.__radius = radius
        self.__velocity = 5
        self.__damageST = 0.0
        self.__dashInvincible = False
        self.__dashing = False
        self.__dashST = 0.0

    def damage(self):
        if time.perf_counter() - self.__damageST > 0.5:
            self.__damageST = time.perf_counter()
            self.__health -= 1

    def isInv(self):
        return self.__dashInvincible

    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)

    def getPoly(self):#as I'm using a more accurate collision method, I can make the hitbox into a polygon to be slightly more accurate
        x, y= self.getLoc()
        return [(x + 0.0, y - 10.0),(x + 9.51, y - 3.09),(x + 5.87, y + 8.09),(x - 5.87, y + 8.09),(x - 9.51, y - 3.09)]
    
    def get_rect(self):
        location = self.getLoc()
        return pygame.Rect(location[0] - self.__radius, location[1] - self.__radius, 2 * self.__radius, 2 * self.__radius)

    def move_randomly(self):#Could maybe utilize this for some kind of stun?? Or just have it slow the player down?
        x, y = self.getLoc()
        x += random.randint(-5,5)
        y += random.randint(-5,5)
        self.setX(x)
        self.setY(y)

    def keyMove(self,xMove = 0.0, yMove = 0.0):
        x, y = super().getLoc()
        mX, mY = (400,300)
        dx = x - mX
        dy = mY - y

        rad = math.atan2(dy,dx)

        length = math.sqrt((dy**2) + (dx**2))
        #If they fly is farther from the center point than 301 it will be teleported back a little 
        if length < 301:
            if self.__dashing:
                super().setLoc(( x + (self.__velocity * xMove * 3), y + (self.__velocity * yMove * 3) ))
            else:
                super().setLoc((x + (self.__velocity * xMove), y + (self.__velocity * yMove)))
        else:
            Nx = 400 + 300 * math.cos(rad)
            Ny = 300 - 300 * math.sin(rad)
            super().setLoc((Nx,Ny))




    def dash(self):
        if not self.__dashing and time.perf_counter() - self.__dashST > 0.5:#starts a timer that will control the actual duration of the dash and the cool down
            self.__dashST = time.perf_counter()
            self.__dashInvincible = True
            self.__dashing = True
            
    def dashTimer(self):#If this method with the timer becomes annoying I could literally do with frames using a counter in the main loop
        if time.perf_counter() - self.__dashST > 0.1:
            self.__dashInvincible = False
            self.__dashing = False

    def getHealth(self):
        return self.__health
