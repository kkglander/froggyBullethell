#Name:      Karl Glander
#Drexel ID: kg3338
#Date:      05/13/2025
#Purpose:   The base class for the lazer attack present in the game so that it can keep track of all of the values relevant to it.

from drawable import *
import math, pygame

class lazer(Drawable):
    def __init__(self, origin,length, rad=0.0, width=5, color=(255, 0, 0)):
        self.__origin = origin
        self.__length = length
        self.__rad = rad
        self.__color = color
        self.__width = width

    def get_rect(self,surface):
        #Because I need to use polygons for collision this method doesn't really work for me, I hope that doesn't dock me points
        pass

    def getPoly(self):
        return self.__points


    def draw(self, surface):
        x1, y1 = self.__origin
        #to get a line = length * sin or cos (rad)
        x2 = x1 + self.__length * math.cos(self.__rad)
        y2 = y1 - self.__length * math.sin(self.__rad)


        # Direction vector
        dx = x2 - x1
        dy = y2 - y1
        length = math.hypot(dx, dy)
        if length == 0:
            return False  # Prevent divide by zero
    
        # Perpendicular unit vector
        perp_dx = -dy / length
        perp_dy = dx / length
        #Figuring out the offset so that the width can be right
        offset_x = perp_dx * (self.__width / 2)
        offset_y = perp_dy * (self.__width / 2)
    
        # Define the 4 corners of the polygon (rotated rectangle)
        points = [
            (x1 + offset_x, y1 + offset_y),
            (x1 - offset_x, y1 - offset_y),
            (x2 - offset_x, y2 - offset_y),
            (x2 + offset_x, y2 + offset_y)
        ]
        self.__points = points
        
        pygame.draw.polygon(surface, self.__color, points)


    def collision(self, target):
        targetPoints = target.getPoly()

        if not target.isInv():
            return super().SAT(self.__points, targetPoints)
        return False

    def spin(self):
        self.__rad += 0.01
        self.__rad %= 6.28
        # x, y = self.__start
        #
        # length = 500
        # x += length * math.cos(self.__rad)
        # y -= length * math.sin(self.__rad)
        # self.__end = ((x, y))
    
    def isWarn(self):
        self.__warning = not self.__warning

