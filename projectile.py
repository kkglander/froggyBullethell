#Name:      Karl Glander
#Drexel ID: kg3338
#Date:      05/13/2025
#Purpose:   The class that is responsible for the bullet-like projectiles in the game

from drawable import *
import math, pygame


class projectile(Drawable):
    def __init__(self,x, y, direction, velocity=7, radius = 10, color = (64, 64, 64)):
        super().__init__(x,y)
        self.__color = color
        self.__direction = direction #in rads
        self.__velocity = velocity
        self.__points = [(x + 0.0, y - 10.0),(x + 9.51, y - 3.09),(x + 5.87, y + 8.09),(x - 5.87, y + 8.09),(x - 9.51, y - 3.09)]

    def get_rect(self):
        #
        pass

    def getPoly(self):
        return self.__points

    def draw(self, surface):
        x, y = super().getLoc()
        self.__points = [(x + 0.0, y - 10.0),(x + 9.51, y - 3.09),(x + 5.87, y + 8.09),(x - 5.87, y + 8.09),(x - 9.51, y - 3.09)]
        pygame.draw.polygon(surface, self.__color, self.__points)
        pygame.draw.polygon(surface, (0,0,0), self.__points, 1)

    def check(self, array):
        x, y = super().getLoc()
        if x < 0 or x > 800:
            array.remove(self)
        elif y < 0 or y > 600:
            array.remove(self)

    def move(self):
        x, y = super().getLoc()
        x += self.__velocity * math.cos(self.__direction)
        y -= self.__velocity * math.sin(self.__direction)
        super().setLoc((x, y))

    def collision(self, target):
        tPoints = target.getPoly()
        if not target.isInv():
            return super().SAT(self.__points, tPoints)
        return False
