import math

listObstacles = [(0,0)]
list_of_points = []
PRM = []
listAgents = []

def distance (x, y):
    if x == None or y == None:
        return 1000000
    t = sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)
    return t
def checkEdge(P1,P2):

    x1 = P1.pos[0]
    x2 = P2.pos[0]
    y1 = P1.pos[1]
    y2 = P2.pos[1]
    
    a = y1-y2
    b = x2-x1
    if b == 0:
         b = 0.001
    c = (x1-x2)*y1 + (y2-y1)*x1
    
    for i in range(50):
        if x1 < x2:
            x = random(x1,x2)
        else:
            x = random(x2,x1)
        y = (-1*(a*x) - c)/ b
        p = (x,y)
        for i in range(len(listObstacles)):
            origin = listObstacles[i]             
            temp = distance(origin, p)
            if temp < 40:
                return False
    return True
class Point1:
    def __init__(self,pos):
        self.pos = pos
        self.parent = None
        self.adjP = []
        self.H = 0
        self.g = 0
        self.f = 0
    def findAdj (self,listP):
        for i in listP:
            if i != self:
                if checkEdge(self,i)==True:
                    self.adjP.append(i)  
                else:  
                    if self in i.adjP:
                        i.adjP.remove(self)
                 
                    
    def displayPoints(self):
        pushMatrix()
        point(self.pos[0],self.pos[1])
        popMatrix()
        for i in self.adjP:
            pushMatrix()
            stroke(222,255,255,30)
            line(self.pos[0],self.pos[1],i.pos[0],i.pos[1])
            popMatrix()
    
                
        
