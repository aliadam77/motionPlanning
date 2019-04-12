from point1 import *
from CSpace import *
from agent import*
radiusO = 60
radiusA = 15 
start= PVector(-270, -270,0)
keyPress= None
def setup():
    size(600,600,P2D)
    Cspace()
    

def draw ():
    translate(width/2,height/2)
    background(10)
    global keyPress

    if keyPress == 'w':
        for i in range(len(listObstacles)):
                pushMatrix()
                strokeWeight(5)
                stroke(0,123,250)
                noFill()
                ellipse(listObstacles[i][0],listObstacles[i][1], radiusO,radiusO)
                popMatrix()
            
        checkCollision(listAgents,0.7)
        disAgents ()
    elif keyPress == 'd':  #display the cSpace
        disCspace()
        checkCollision(listAgents,0.7)
        disAgents ()
    elif keyPress == 'p': #pause
         disAgents ()
         for i in range(len(listObstacles)):
                pushMatrix()
                strokeWeight(5)
                stroke(0,123,250)
                noFill()
                ellipse(listObstacles[i][0],listObstacles[i][1], radiusO,radiusO)
                popMatrix()
                
    elif keyPress == 'a': #add obstacles
        for i in range(len(listObstacles)):
                pushMatrix()
                strokeWeight(5)
                stroke(0,123,250)
                noFill()
                ellipse(listObstacles[i][0],listObstacles[i][1], radiusO,radiusO)
                popMatrix()
                
    elif keyPress == 'c':  #generate the Cspace
        Cspace()
        print("Please press "+"w")
        keyPress = 'r'            
        
def keyPressed():
    global keyPress
    if key == 'w' :
         keyPress = 'w'
    elif key == 'd':
        keyPress = 'd'
        
    elif key == 'p':
        keyPress = 'p'
       
    elif key == 'a':
        keyPress = 'a'
        
    elif key == 'c':
        keyPress = 'c'
    elif keyCode == UP:
        if listAgents > 5:
            listAgents[5].pos[1] -= 5
    elif keyCode == DOWN:
        if listAgents > 5:
            listAgents[5].pos[1] += 5
    elif keyCode == LEFT:
        if listAgents > 5:
            listAgents[5].pos[0] -= 5
    elif keyCode == RIGHT:
        if listAgents > 5:
            listAgents[5].pos[0] += 5
def mousePressed():
    global keyPress
    global listObstacles
    if keyPress == 'a':
        o = (mouseX-width/2,mouseY-height/2)
        if o not in listObstacles:
            listObstacles.append(o)
    
    
