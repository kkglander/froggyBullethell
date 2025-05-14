#Name:      Karl Glander
#Drexel ID: kg3338
#Date:      05/13/2025
#Purpose:   This file holds the frog class, which is the only enemy that will attack the player

import pygame, math
from drawable import Drawable
from projectile import projectile
from lazer import lazer


#TODO:
# [x] - Make Frog attack Frameworks
# [x] - make wave/shape bullet cluster
# [ ] - If I have time, I could beef up the standardatt by making it shoot where the player is going to be 
# Sweeping attacks seem to be very popular as they can be difficult while making use of the dodge mechanic


class Frog(Drawable):
    def __init__(self, x=0, y=0, size=20, color=(0, 255, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__size = size
        self.__rads = 0

    def get_rect(self):
        x, y = self.getLoc()
        return pygame.Rect(x - self.__size // 2, y - self.__size // 2, self.__size, self.__size)

    def getPoly(self):
        return self.__points


    def draw(self, surface, trackedLoc):
        #can't decide if I want to have a square that tracks or a circle that just has the eyes follow you
        x, y = self.getLoc()
        rad = self.radianCalculations(trackedLoc)

        length = 15

        p2X = x + length * math.cos(rad + math.radians(45))
        p2Y = y - length * math.sin(rad + math.radians(45))

        p3X = x + length * math.cos(rad - math.radians(45))
        p3Y = y - length * math.sin(rad - math.radians(45))

        p4X = x + length * math.cos(rad + math.radians(135))
        p4Y = y - length * math.sin(rad + math.radians(135))

        p5X = x + length * math.cos(rad - math.radians(135))
        p5Y = y - length * math.sin(rad - math.radians(135))
        
        self.__points = [(p2X, p2Y), (p3X, p3Y), (p5X, p5Y), (p4X, p4Y)]

        pygame.draw.polygon(surface, self.__color, self.__points)#body
        pygame.draw.circle(surface, (0, 0, 0), (p2X, p2Y), 4)#eye
        pygame.draw.circle(surface, (0, 0, 0), (p3X, p3Y), 4)#eye


    def drawTrackLine(self, surface, trackedLoc):
        x,y = self.getLoc()
        rad = self.radianCalculations(trackedLoc)

        #find the x and y of the endpoint using sin and cos
        length = 50
        endX = x + length * math.cos(rad)
        endY = y - length * math.sin(rad)

        pygame.draw.line(surface, (0, 0, 0), (x, y), (endX, endY))


    def standardAtt(self, target, array, frame,vel=8):
        #this is going to spawn in a projectile object that is shooting at the player
        #projectile takes (x, y, direction)
        if frame % 30 == 0:
            x,y = self.getLoc()
            length = 30
            rad = self.radianCalculations(target.getLoc())
            x += length * math.cos(rad)
            y -= length * math.sin(rad)
            
            array.append(projectile(x,y,rad,vel))        

    def attack2(self, array):
        #spinning lazers
        for lazer in array:
            lazer.spin()
            
    def attack3(self, target, array, frame, vel=7):
        # circle
        if frame % 50 == 0:
            length = 30
            rad = self.radianCalculations(target.getLoc())

            i = 0 
            while i < 6.28:
                x,y = self.getLoc()
                x += length * math.cos(rad + i)
                y -= length * math.sin(rad + i)

                array.append(projectile(x, y, rad, vel))
                i += 0.628

    def attack4(self, array, frame):
        #classic projectal double Spiral
        if frame % 2 == 0:
            self.__rads %= 360
            self.__rads += 0.13

            x, y = self.getLoc()

            distance = 30
            x2 = x + distance * math.cos(self.__rads - 3.14)
            y2 = y - distance * math.sin(self.__rads - 3.14)

            x += distance * math.cos(self.__rads)
            y -= distance * math.sin(self.__rads)

            array.append(projectile(x,y,self.__rads, 4))
            array.append(projectile(x2,y2,self.__rads-3.14, 4))
        
    def attack5(self, target, array, frame, vel=5):
        #some shape of projectiles going at that player
        #prolly just a simple wave
         if frame % 50 == 0:
            x,y = self.getLoc()
            length = 30
            rad = self.radianCalculations(target.getLoc())
            x += length * math.cos(rad)
            y -= length * math.sin(rad)

            i = rad - 1
            while i < (rad + 1):
                array.append(projectile(x,y,i, vel))
                i += 0.1


    def attack6(self, surface):
        #Cool Idea but only if I have time
        #the cool sin wave one that is made by having two projectiles rotate around a point while also shooting in a spiral
        pass

#   ===[[MATH TIME]]===

    def radianCalculations(self,trackedLoc):
        #seperate the targets x and y
        targetX, targetY = trackedLoc

        #seperate the fogs x and y
        x,y = self.getLoc()
        
        #get the distance from the frog to the target
        dx = targetX - x
        dy = y - targetY

        #calculate the radians using atan2 which deals with the quadrans for me
        rad = math.atan2(dy,dx)
        # print(math.degrees(rad)) #degrees for debugging :P

        return rad

#  ===[[SETTERS AND GETTERS]]===

    def setRad(self, value):
        self.__rads = value

