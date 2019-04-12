from point1 import *
from agent import *
import random
import math 


num_of_points =100
num_of_agents = 30
radiusO = 60
radiusA = 15
 


tH = 10000
maxF = 1
def genNumber():
    x = (random.randint(-300,300),random.randint(-300,300))
    c = x[0]**2 + x[1]**2 
    for i in range(len(listObstacles)):
        if c > (((radiusA+radiusO)//2)**2 + listObstacles[i][0]**2 + listObstacles[i][1]**2 +60):
            continue
        else:
            x = genNumber()
            return x        
    return x
    

def Cspace():
    del listAgents[:]
    del PRM[:]
    del list_of_points [:]
    for i in range (num_of_points):
        x =genNumber()
        list_of_points.append(x)
        p = Point1(x)
        PRM.append(p)
    for P in PRM:
        P.findAdj(PRM)
    for i in range (num_of_agents):
        s = genNumber()
        g = genNumber()
        A = Agent(i,s,g)
        A.Astar(PRM)
        listAgents.append(A)
            
def disCspace():
    for i in range(len(listObstacles)):
                pushMatrix()
                strokeWeight(5)
                stroke(0,123,250)
                noFill()
                ellipse(listObstacles[i][0],listObstacles[i][1], radiusA+radiusO,radiusA+radiusO)
                popMatrix()
    for i in PRM:
            pushMatrix()
            stroke(0)
            point(i.pos[0],i.pos[1])
            popMatrix()
    for i in PRM:
            i.displayPoints()            

def ttc(i,j):
    r = radiusA * 2
    w = (j.pos[0] - i.pos[0],j.pos[1] - i.pos[1])
    c = (w[0]**2+w[1]**2) - r * r*r
    if (c < 0): #agents are colliding
        return 0
    v = (i.v[0] - j.v[0],i.v[0] - j.v[0])
    a = (v[0]**2+v[1]**2)
    b = (w[0]*v[0]+w[1]*v[1])
    discr = b*b - a*c
    if (discr <= 0):
        return float('inf')
    tau = (b - sqrt(discr)) / a
    if (tau < 0):
        return float('inf')
    return tau

def checkCollision(listAgents,dt):
    #Precompute all neighbors for all agents 
    for i in listAgents:
        if i.done == 1:
            i.transition(PRM)
            i.pathFinder()
            continue
        if len(i.path) > 1 :
            Next_point = i.path[i.next]
            deltaX = Next_point.pos[0] - i.pos[0]
            deltaY = Next_point.pos[1] - i.pos[1]
            x = (deltaX*1 ,deltaY*1)
            nor = sqrt(x[0]**2 + x[1]**2)
            i.gv = [(x[0]/nor)*MAXspeed ,(x[1]/nor)*MAXspeed]
        
            if((i.next != len(i.path)-1) and distance(i.pos,Next_point.pos) < radiusA/2):
                i.next+=1 
            elif(distance(i.pos,Next_point.pos) < radiusA/2):
                i.done = 1
    #find all neighbors within sensing radius
        i.neighbor = []
        for j in listAgents :
            if i!= j:
                if distance(i.pos,j.pos)< 10:
                    i.neighbor.append(j)
                    
    for i in listAgents:
        i.F = [(i.gv[0]-i.v[0])*2,(i.gv[1]-i.v[1])*2] #Compute goal force 
        for  j in i.neighbor:
        #Compute time-to-collision 
            t = ttc(i,j)
            #Compute collision avoidance force 
            #Force Direction 
            FAvoid = [i.pos[0] + i.v[0]*t - j.pos[0] - j.v[0]*t, i.pos[1] + i.v[1]*t - j.pos[1] - j.v[1]*t]
            if (FAvoid[0] != 0 and FAvoid[1] != 0):
                FA = sqrt(FAvoid[0]**2+FAvoid[1]**2)
                FAvoid = [FAvoid[0]/FA,FAvoid[1]/FA]
            #Force Magnitude 
            Mag = 0
            if (t >= 0 and t <= tH):
                Mag = (tH-t)/(t + 0.001)
            if (Mag > maxF): Mag = maxF
            FAvoid *= Mag
    
            i.F[0] += FAvoid[0]
            i.F[1] += FAvoid[1]
            
    #Apply forces 
    for i in listAgents:
        if i.id == 5:
            continue    
        i.v[0] += i.F[0] * dt
        i.v[1] += i.F[1] * dt
        i.pos[0] += i.v[0] * dt
        i.pos[1] += i.v[1] * dt
def disAgents ():
    for i in listAgents:
        
        if i.id == 5:
            pushMatrix()
            noFill();
            noStroke();
            stroke(200,0,200)
            ellipse(i.pos[0] ,i.pos[1] , radiusA,radiusA)
            popMatrix()
        else:
            
            pushMatrix()
            strokeWeight(6)
            stroke(0,255,0)
            noFill()
            point(i.start.pos[0],i.start.pos[1])
            popMatrix()
            
            pushMatrix()
            strokeWeight(6)
            stroke(0,0,255)
            point(i.goal.pos[0],i.goal.pos[1])
            popMatrix()
        
            pushMatrix()
            noFill();
            noStroke();
            stroke(132,3,0)
            ellipse(i.pos[0] ,i.pos[1] , radiusA,radiusA)
            popMatrix()
