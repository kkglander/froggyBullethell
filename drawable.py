#Name:      Karl Glander
#Drexel ID: kg3338
#Date:      05/13/2025
#Purpose:   The main drawable that serves as the abstract base class for all objects drawn

from abc import ABC, abstractmethod

class Drawable(ABC):

    def __init__(self, x=0, y=0):
        self.__visible = True
        self.__x = x
        self.__y = y

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def get_rect(self):
        pass

    @abstractmethod
    def getPoly(self):
        pass

    def getLoc(self):
        return (self.__x, self.__y)
    
    def setLoc(self, newloc):
        self.__x, self.__y = newloc

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
    
    def isVisible(self):
        return self.__visible

    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False

    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) \
and (rect2.height + rect1.y > rect2.y):
            return True
        return False

    def SAT(self, poly1, poly2):#SEPERATING AXIS THEROM
        #The comments below is not only to demonstate that I understand what the code is doing but also for myself so that by writing it, I might understand it better

        #poly1, poly2 = lists of points that creates some sort of polygon
        #for every edge of the polygon we treat it as an axis
        #   grab the normal of that axis
        #   loop through all of the vertices of poly2 and 'project' them onto the normal line
        #   this will leave us with two intervals on the normal axis that represent the shapes on our axis
        #   if the lines don't intersect, they the shapes cannot be colliding and we can return False
        #   if the lines do intersect, then we must keep looking until we find an axis where they don't collide, and if we can't, they must be colliding
        #
        # what to 'project' means:
        #   we are going to take the current normal line and find the dot product
        #   Using the biggest and the smallest value from the dot product we can then have the min and max
        #

        for polygon in [poly1, poly2]: #go through both lists of points ( polygons )
            for i1 in range(len(polygon)):
                i2 = (i1 + 1) % len(polygon)
                p1 = polygon[i1]
                p2 = polygon[i2]

                vert = (p2[0] - p1[0], p2[1] - p1[1]) #getting the vector
                norm = (-vert[1],vert[0]) #getting the normal of that vector

                def dotties(poly): #dot product or 'projecting' them
                    dots = []
                    for points in poly:
                        dots.append(points[0] * norm[0] + points[1] * norm[1])
                    return min(dots), max(dots)

                min1, max1 = dotties(poly1)
                min2, max2 = dotties(poly2)


                #if theres no overlap detected then we have found a seperation and can return false 
                if max1 < min2 or max2 < min1:
                    return False
        #if we run through everything and cannot find a vertex without overlap, they are colliding
        #and we can return true
        return True
