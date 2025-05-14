#File Name:   drawable.py
#Purpose:     Abstract class that allows us to create drawable objects
#             with different shapes, at a given location (x, y)
#Last update: 4/24/24 - A. Medlock

from random import randint

import pygame
from abc import ABC, abstractmethod

# Abstract Base Class: Drawable
class Drawable(ABC):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    
    @abstractmethod
    def draw(self, surface):
        pass
        
# Rectangle Class: ADD YOUR CODE HERE
class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self, surface):
        shectangle = pygame.Rect(self.getLoc(),(self.__width,self.__height))
        pygame.draw.rect(surface, self.__color, shectangle)

# Snowflake Class: ADD YOUR CODE HERE
class Snowflake(Drawable):
    def __init__(self,x,y=0):
        super().__init__(x,y)
        self.__maxY = randint(300,500)

    def draw(self,surface):
        x, y = super().getLoc()
        pygame.draw.line(surface,(255,255,255),(x-5, y),(x+5,y))
        pygame.draw.line(surface,(255,255,255),(x, y-5),(x,y+5))
        pygame.draw.line(surface,(255,255,255),(x-5, y-5),(x+5,y+5))
        pygame.draw.line(surface,(255,255,255),(x-5, y+5),(x+5,y-5))

    def getMaxY(self):
        return self.__maxY

