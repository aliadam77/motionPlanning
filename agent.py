from CSpace import *
from point1 import*
import random
radiusO = 60
radiusA = 15 
MAXspeed =0.9

class Agent:
    
    def __init__(self,id,start,goal):
        self.id = id
        self.start = Point1(start)
        self.goal = Point1(goal)
        self.pos = [self.start.pos[0],self.start.pos[1]]
        self.path=[]
        self.done= 0
        self.v= [0,0]
        self.gv = [0,0]
        self.F = [0,0]
        self.neighbor = []
        self.next = 1
        
        
        
    def Astar(self,PRM):    
        for i in PRM:
            i.H = distance(i.pos ,self.goal.pos)
            i.parent =None
        open_list = []
        closed_list = []
        sNode = minDis(self.start,PRM)
        gNode = minDis(self.goal,PRM)
        open_list.append(sNode)
        while(open_list):
            open_list.sort(key= lambda x: x.f)
            curNode = open_list[0]
            del(open_list[0])
            closed_list.append(curNode)
            if curNode is gNode :
                self.path.append(self.goal)
                startNode = curNode
                while(startNode):
                    self.path.append(startNode)
                    startNode = startNode.parent  
                self.path.append(self.start)
                open_list = []
                
                
            for i in curNode.adjP:
                if i in closed_list:
                    continue
                if i in open_list:
                    tempg = curNode.g + distance(curNode.pos,i.pos)
                    if tempg < i.g:
                        i.g = tempg
                        i.f = i.g + i.H
                        i.parent = curNode    
                else:
                    i.g = curNode.g + distance(curNode.pos,i.pos)
                    i.f = i.g +i.H
                    i.parent = curNode      
                    open_list.append(i)
        self.path.reverse()  
        if len(self.path) > 1:
            Next_point = self.path[self.next]
            deltaX = Next_point.pos[0] - self.pos[0]
            deltaY = Next_point.pos[1] - self.pos[1]
            x = (deltaX*1 ,deltaY*1)
            nor = sqrt(x[0]**2 + x[1]**2)
            self.gv = [(x[0]/nor)*MAXspeed ,(x[1]/nor)*MAXspeed]
            
            
            
    def transition(self,PRM):
        self.path = []
        self.stop = 1
        self.start = self.goal
        self.pos = [self.start.pos[0],self.start.pos[1]]
        g = genNumber()
        self.goal = Point1(g)
        self.next = 1
        self.Astar(PRM)
        self.done = 0
        
        
    def pathFinder(self):
        for i in range(len(self.path)):
            if i < len(self.path)-1:
                pushMatrix()
                strokeWeight(3)
                stroke(255,255,0)
                line(self.path[i].pos[0],self.path[i].pos[1],self.path[i+1].pos[0],self.path[i+1].pos[1])
                popMatrix()
        
            
        
     
        
    

def genNumber():
    x = (random.randint(-300,300),random.randint(-300,300))
    c = x[0]**2 + x[1]**2 
    if c > (((radiusA+radiusO)//2)**2):
        return x
    else:
       x = genNumber()
    return x

def minDis(p,listP):
    mini = 1000000
    node = p
    for i in listP: 
        if checkEdge(p,i):
            temp = distance(i.pos,p.pos)
            if mini > temp:
                mini = temp
                node = i
                
    return node    
