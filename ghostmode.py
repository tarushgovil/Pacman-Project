#112 Term Project
#Name: Tarush Govil
#Section: N
#andrew ID: tarushg
#Comment:contains the logic for moving the pacmans across the board for ghostmode


from image_util import *
import random
from tkinter import *


def pacman1NewGhostInteract(data):
    # if ((abs((data.imageXPac - data.imageXGhost1)) <= 0.001) and (abs(data.imageYPac - data.imageYGhost1) <= 0.001)):
    if ((abs((data.imageXPac - data.imageXGhost1)) <= 10) and (abs(data.imageYPac - data.imageYGhost1) <= 10)):
        data.pacman1 = False
        
        
def pacman2NewGhostInteract(data):
    #if ((abs((data.imageXPac2New - data.imageXGhost1)) <= 0.001) and (abs(data.imageYPac2New - data.imageYGhost1) <= 0.001)):
    if ((abs((data.imageXPac2New - data.imageXGhost1)) <= 10) and (abs(data.imageYPac2New - data.imageYGhost1) <= 10)):

        data.pacman2 = False
        

def pacman3NewGhostInteract(data):
    # if ((abs((data.imageXPac3 - data.imageXGhost1)) <= 0.001) and (abs(data.imageYPac3 - data.imageYGhost1) <= 0.001)):
    if ((abs((data.imageXPac3 - data.imageXGhost1)) <= 10) and (abs(data.imageYPac3 - data.imageYGhost1) <= 10)):

        data.pacman3 = False
        
        
def allPacmanGhostInteract(data):
    if data.pacman1 == False and data.pacman2 == False and data.pacman3 == False:
        data.mode = "winGameSingle"
        
def timeRemaining(data):
    if data.timeLeft == 0:
        data.mode = "youLose"
        

def pacmanRandom(data):
    if data.pacman1 != False:
        row = int((data.imageYPac-data.margin)//data.cellSize)
        col = int((data.imageXPac-data.margin)//data.cellSize)
       
        if data.pacmanDirection == "u":
            
            if data.newGrid[row-1][col]!= 1:
                
                data.imageYPac -= data.cellSize
                
                row = int((data.imageYPac-data.margin)//data.cellSize)
                col = int((data.imageXPac-data.margin)//data.cellSize)
                
                if data.newGrid[row][col + 1] !=1 and data.newGrid[row][col+1]!= 7:
                    data.pacmanDirection =  random.choice(["u","r"])
                if data.newGrid[row][col - 1] !=1 and data.newGrid[row][col-1]!= 7:
                    data.pacmanDirection = random.choice(["l",data.pacmanDirection])
            elif data.newGrid[row][col + 1] !=1 and data.newGrid[row][col -1] !=1 and data.newGrid[row][col-1]!= 7 and data.newGrid[row][col+1]!= 7:
                
                data.pacmanDirection = random.choice(["l","r"])
            elif data.newGrid[row][col + 1] !=1 and data.newGrid[row][col+1]!= 7:
               
                data.pacmanDirection = "r"
            elif data.newGrid[row][col - 1] !=1 and data.newGrid[row][col-1]!= 7:
                
                data.pacmanDirection = "l"
            elif data.newGrid[row + 1][col] !=1 and data.newGrid[row + 1][col]!= 7:
               
                data.pacmanDirection = "d"
                
            else:
                
                data.pacmanDirection = random.choice(["l","d","r","u"])
    
                    
        
        elif data.pacmanDirection == "d":
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
            if data.newGrid[row+1][col]!=1:
                data.imageYPac +=data.cellSize
                row = int((data.imageYPac-data.margin)//data.cellSize)
                col = int((data.imageXPac-data.margin)//data.cellSize)
                if data.newGrid[row][col + 1] !=1 and data.newGrid[row][col+1]!= 7:
                    data.pacmanDirection =  random.choice(["d","r"])
                if data.newGrid[row][col - 1] !=1 and data.newGrid[row][col-1]!= 7:
                    data.pacmanDirection = random.choice(["l",data.pacmanDirection])
            elif data.newGrid[row][col + 1] !=1 and data.newGrid[row][col -1] !=1 and data.newGrid[row][col -1]!= 7 and data.newGrid[row][col + 1]!= 7:
 
                data.pacmanDirection = random.choice(["l","r"])
            elif data.newGrid[row][col + 1] !=1 and data.newGrid[row + 1][col]!= 7 :
               
                
                data.pacmanDirection = "r"
            elif data.newGrid[row][col - 1] !=1 and data.newGrid[row][col - 1]!= 7:
                
                data.pacmanDirection = "l"
            elif data.newGrid[row  - 1][col] !=1 and data.newGrid[row - 1][col]!= 7:
                
                data.pacmanDirection = "u"
            else:
               
                data.pacmanDirection = random.choice(["l","d","r","u"])
                
                
        elif data.pacmanDirection == "l":
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
            if data.newGrid[row][col-1]!=1:
               
                data.imageXPac -=data.cellSize
                row = int((data.imageYPac-data.margin)//data.cellSize)
                col = int((data.imageXPac-data.margin)//data.cellSize)
                if data.newGrid[row + 1][col] !=1 and data.newGrid[row + 1][col+1]!= 7:
                    data.pacmanDirection =  random.choice(["l","d"])
                if data.newGrid[row - 1][col] !=1 and data.newGrid[row - 1][col-1]!= 7:
                    data.pacmanDirection = random.choice(["u",data.pacmanDirection])
            elif data.newGrid[row +1][col] !=1 and data.newGrid[row -1][col] != 1 and data.newGrid[row -1][col]!= 7 and data.newGrid[row -1 ][col]!= 7:
                
                data.pacmanDirection = random.choice(["u","d"])
            elif data.newGrid[row +1][col] !=1 and data.newGrid[row + 1][col]!= 7:
                
                data.pacmanDirection = "d"
            elif data.newGrid[row -1][col] !=1 and data.newGrid[row-1][col]!= 7:
               
                data.pacmanDirection = "u"
            elif data.newGrid[row][col + 1]!=1 and data.newGrid[row][col+1]!= 7:
                
                data.pacmanDirection = "r"
    
            else:
                data.pacmanDirection = random.choice(["l","d","r","u"])
            
        elif data.pacmanDirection == "r":
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
           
            if data.newGrid[row][col+1] != 1:
              
                data.imageXPac += data.cellSize
                row = int((data.imageYPac-data.margin)//data.cellSize)
                col = int((data.imageXPac-data.margin)//data.cellSize)
                if data.newGrid[row + 1][col] !=1 and data.newGrid[row + 1][col+1]!= 7:
                    data.pacmanDirection =  random.choice(["r","d"])
                if data.newGrid[row - 1][col] !=1 and data.newGrid[row - 1][col-1]!= 7:
                    data.pacmanDirection = random.choice(["u",data.pacmanDirection])
            elif data.newGrid[row + 1][col] != 1 and data.newGrid[row -1][col] != 1 and data.newGrid[row-1][col]!= 7 and data.newGrid[row + 1][col]!= 7:
              
                data.pacmanDirection = random.choice(["u","d"])
            elif data.newGrid[row - 1][col] != 1 and data.newGrid[row-1][col]!= 7:
                
                data.pacmanDirection = "u"
            elif data.newGrid[row + 1][col] != 1 and data.newGrid[row + 1][col]!= 7:
               
                data.pacmanDirection = "d"
            elif data.newGrid[row][col - 1]!=1 and data.newGrid[row][col-1]!= 7:
               
                data.pacmanDirection = "l"
            else:
                
                data.pacmanDirection = random.choice(["l","d","r","u"])
            
            
            
            
def pacman2Random(data):
    if data.pacman2 != False:
        row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
        col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
        
        if data.pacman2Direction == "u":
            if data.newGrid[row2-1][col2]!= 1:

                data.imageYPac2New -= data.cellSize
                 
                row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
                col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
                
                if data.newGrid[row2][col2 + 1] !=1 and data.newGrid[row2][col2+1]!= 7:
                    data.pacman2Direction =  random.choice(["u","r"])
                if data.newGrid[row2][col2 - 1] !=1 and data.newGrid[row2][col2-1]!= 7:
                    data.pacman2Direction = random.choice(["l",data.pacman2Direction])
            elif data.newGrid[row2][col2 + 1] !=1 and data.newGrid[row2][col2 -1] !=1 and data.newGrid[row2][col2-1]!= 7 and data.newGrid[row2][col2+1]!= 7:
             
                data.pacman2Direction = random.choice(["l","r"])
            elif data.newGrid[row2][col2 + 1] !=1 and data.newGrid[row2][col2+1]!= 7:
                
                data.pacman2Direction = "r"
            elif data.newGrid[row2][col2 - 1] !=1 and data.newGrid[row2][col2-1]!= 7:
              
                data.pacman2Direction = "l"
            elif data.newGrid[row2 + 1][col2] !=1 and data.newGrid[row2 + 1][col2]!= 7:
        
                data.pacman2Direction = "d"
                
            else:
     
                data.pacman2Direction = random.choice(["l","d","r","u"])
    
                    
        
        elif data.pacman2Direction == "d":
            row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
            if data.newGrid[row2+1][col2]!=1:
           
                data.imageYPac2New +=data.cellSize
                row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
                col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
                if data.newGrid[row2][col2 + 1] !=1 and data.newGrid[row2][col2+1]!= 7:
                    data.pacman2Direction =  random.choice(["d","r"])
                if data.newGrid[row2][col2 - 1] !=1 and data.newGrid[row2][col2-1]!= 7:
                    data.pacman2Direction = random.choice(["l",data.pacman2Direction])
            elif data.newGrid[row2][col2 + 1] !=1 and data.newGrid[row2][col2 -1] !=1 and data.newGrid[row2][col2 -1]!= 7 and data.newGrid[row2][col2 + 1]!= 7:
                
                data.pacman2Direction = random.choice(["l","r"])
            elif data.newGrid[row2][col2 + 1] !=1 and data.newGrid[row2 + 1][col2]!= 7 :
            
                data.pacman2Direction = "r"
            elif data.newGrid[row2][col2 - 1] !=1 and data.newGrid[row2][col2 - 1]!= 7:
              
                data.pacman2Direction = "l"
            elif data.newGrid[row2  - 1][col2] !=1 and data.newGrid[row2 - 1][col2]!= 7:
               
                data.pacman2Direction = "u"
            else:
                
                data.pacman2Direction = random.choice(["l","d","r","u"])
                
                
        elif data.pacman2Direction == "l":
            row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2New-data.margin)//data.cellSize)

            if data.newGrid[row2][col2-1]!=1:
              
                data.imageXPac2New -=data.cellSize
                row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
                col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
                if data.newGrid[row2 + 1][col2] !=1 and data.newGrid[row2 + 1][col2+1]!= 7:
                    data.pacman2Direction =  random.choice(["l","d"])
                if data.newGrid[row2 - 1][col2] !=1 and data.newGrid[row2 - 1][col2-1]!= 7:
                    data.pacman2Direction = random.choice(["u",data.pacman2Direction])
            elif data.newGrid[row2 +1][col2] !=1 and data.newGrid[row2 -1][col2] != 1 and data.newGrid[row2 -1][col2]!= 7 and data.newGrid[row2 -1 ][col2]!= 7:
              
                data.pacman2Direction = random.choice(["u","d"])
            elif data.newGrid[row2 +1][col2] !=1 and data.newGrid[row2 + 1][col2]!= 7:
           
                data.pacman2Direction = "d"
            elif data.newGrid[row2 -1][col2] !=1 and data.newGrid[row2-1][col2]!= 7:
          
                data.pacman2Direction = "u"
            elif data.newGrid[row2][col2 + 1]!=1 and data.newGrid[row2][col2+1]!= 7:
               
                data.pacman2Direction = "r"
    
            else:
                data.pacman2Direction = random.choice(["l","d","r","u"])
            
        elif data.pacman2Direction == "r":
            row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
           
            if data.newGrid[row2][col2+1] != 1:
                
                data.imageXPac2New += data.cellSize
                row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
                col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
                if data.newGrid[row2 + 1][col2] !=1 and data.newGrid[row2 + 1][col2+1]!= 7:
                    data.pacman2Direction =  random.choice(["r","d"])
                if data.newGrid[row2 - 1][col2] !=1 and data.newGrid[row2 - 1][col2-1]!= 7:
                    data.pacman2Direction = random.choice(["u",data.pacman2Direction])
            elif data.newGrid[row2 + 1][col2] != 1 and data.newGrid[row2 -1][col2] != 1 and data.newGrid[row2-1][col2]!= 7 and data.newGrid[row2 + 1][col2]!= 7:
              
                data.pacman2Direction = random.choice(["u","d"])
            elif data.newGrid[row2 - 1][col2] != 1 and data.newGrid[row2-1][col2]!= 7:
               
                data.pacman2Direction = "u"
            elif data.newGrid[row2 + 1][col2] != 1 and data.newGrid[row2 + 1][col2]!= 7:
              
                data.pacman2Direction = "d"
            elif data.newGrid[row2][col2 - 1]!=1 and data.newGrid[row2][col2-1]!= 7:
                
                data.pacman2Direction = "l"
            else:
               
                data.pacman2Direction = random.choice(["l","d","r","u"])
            
            
def pacman3Random(data):
    if data.pacman3 != False:
        row3 = int((data.imageYPac3-data.margin)//data.cellSize)
        col3 = int((data.imageXPac3-data.margin)//data.cellSize)
        if data.pacman3Direction == "u":
            
            if data.newGrid[row3-1][col3]!= 1:
              
                data.imageYPac3 -= data.cellSize
                
                row3 = int((data.imageYPac3-data.margin)//data.cellSize)
                col3 = int((data.imageXPac3-data.margin)//data.cellSize)
                
                if data.newGrid[row3][col3 + 1] !=1 and data.newGrid[row3][col3+1]!= 7:
                    data.pacman3Direction =  random.choice(["u","r"])
                if data.newGrid[row3][col3 - 1] !=1 and data.newGrid[row3][col3-1]!= 7:
                    data.pacman3Direction = random.choice(["l",data.pacman3Direction])
            elif data.newGrid[row3][col3 + 1] !=1 and data.newGrid[row3][col3 -1] !=1 and data.newGrid[row3][col3-1]!= 7 and data.newGrid[row3][col3+1]!= 7:
               
                data.pacman3Direction = random.choice(["l","r"])
            elif data.newGrid[row3][col3 + 1] !=1 and data.newGrid[row3][col3+1]!= 7:
                
                data.pacman3Direction = "r"
            elif data.newGrid[row3][col3 - 1] !=1 and data.newGrid[row3][col3-1]!= 7:
            
                data.pacman3Direction = "l"
            elif data.newGrid[row3 + 1][col3] !=1 and data.newGrid[row3 + 1][col3]!= 7:
           
                data.pacman3Direction = "d"
                
            else:
             
                data.pacman3Direction = random.choice(["l","d","r","u"])
    
                    
        
        elif data.pacman3Direction == "d":
            row3 = int((data.imageYPac3-data.margin)//data.cellSize)
            col3 = int((data.imageXPac3-data.margin)//data.cellSize)
            if data.newGrid[row3+1][col3]!=1:
              
                data.imageYPac3 +=data.cellSize
                row3 = int((data.imageYPac3-data.margin)//data.cellSize)
                col3 = int((data.imageXPac3-data.margin)//data.cellSize)
                if data.newGrid[row3][col3 + 1] !=1 and data.newGrid[row3][col3+1]!= 7:
                    data.pacman3Direction =  random.choice(["d","r"])
                if data.newGrid[row3][col3 - 1] !=1 and data.newGrid[row3][col3-1]!= 7:
                    data.pacman3Direction = random.choice(["l",data.pacman3Direction])
            elif data.newGrid[row3][col3 + 1] !=1 and data.newGrid[row3][col3 -1] !=1 and data.newGrid[row3][col3 -1]!= 7 and data.newGrid[row3][col3 + 1]!= 7:
               
                data.pacman3Direction = random.choice(["l","r"])
            elif data.newGrid[row3][col3 + 1] !=1 and data.newGrid[row3 + 1][col3]!= 7 :
              
                
                data.pacman3Direction = "r"
            elif data.newGrid[row3][col3 - 1] !=1 and data.newGrid[row3][col3 - 1]!= 7:
               
                data.pacman3Direction = "l"
            elif data.newGrid[row3  - 1][col3] !=1 and data.newGrid[row3 - 1][col3]!= 7:
                
                data.pacman3Direction = "u"
            else:
              
                data.pacman3Direction = random.choice(["l","d","r","u"])
                
                
        elif data.pacman3Direction == "l":
            row3 = int((data.imageYPac3-data.margin)//data.cellSize)
            col3 = int((data.imageXPac3-data.margin)//data.cellSize)
            if data.newGrid[row3][col3-1]!=1:
            
                data.imageXPac3 -=data.cellSize
                row3 = int((data.imageYPac3-data.margin)//data.cellSize)
                col3 = int((data.imageXPac3-data.margin)//data.cellSize)
                if data.newGrid[row3 + 1][col3] !=1 and data.newGrid[row3 + 1][col3+1]!= 7:
                    data.pacman3Direction =  random.choice(["l","d"])
                if data.newGrid[row3 - 1][col3] !=1 and data.newGrid[row3 - 1][col3-1]!= 7:
                    data.pacman3Direction = random.choice(["u",data.pacman3Direction])
            elif data.newGrid[row3 +1][col3] !=1 and data.newGrid[row3 -1][col3] != 1 and data.newGrid[row3 -1][col3]!= 7 and data.newGrid[row3 -1 ][col3]!= 7:
              
                data.pacman3Direction = random.choice(["u","d"])
            elif data.newGrid[row3 +1][col3] !=1 and data.newGrid[row3 + 1][col3]!= 7:
              
                data.pacman3Direction = "d"
            elif data.newGrid[row3 -1][col3] !=1 and data.newGrid[row3-1][col3]!= 7:
              
                data.pacman3Direction = "u"
            elif data.newGrid[row3][col3 + 1]!=1 and data.newGrid[row3][col3+1]!= 7:
               
                data.pacman3Direction = "r"
    
            else:
                data.pacman3Direction = random.choice(["l","d","r","u"])
            
        elif data.pacman3Direction == "r":
            row3 = int((data.imageYPac3-data.margin)//data.cellSize)
            col3 = int((data.imageXPac3-data.margin)//data.cellSize)
            if data.newGrid[row3][col3+1] != 1:
             
                data.imageXPac3 += data.cellSize
                row3 = int((data.imageYPac3-data.margin)//data.cellSize)
                col3 = int((data.imageXPac3-data.margin)//data.cellSize)
                if data.newGrid[row3 + 1][col3] !=1 and data.newGrid[row3 + 1][col3+1]!= 7:
                    data.pacman3Direction =  random.choice(["r","d"])
                if data.newGrid[row3 - 1][col3] !=1 and data.newGrid[row3 - 1][col3-1]!= 7:
                    data.pacman3Direction = random.choice(["u",data.pacman3Direction])
            elif data.newGrid[row3 + 1][col3] != 1 and data.newGrid[row3 -1][col3] != 1 and data.newGrid[row3-1][col3]!= 7 and data.newGrid[row3 + 1][col3]!= 7:
                
                data.pacman3Direction = random.choice(["u","d"])
            elif data.newGrid[row3 - 1][col3] != 1 and data.newGrid[row3-1][col3]!= 7:
             
                data.pacman3Direction = "u"
            elif data.newGrid[row3 + 1][col3] != 1 and data.newGrid[row3 + 1][col3]!= 7:
                
                data.pacman3Direction = "d"
            elif data.newGrid[row3][col3 - 1]!=1 and data.newGrid[row3][col3-1]!= 7:
             
                data.pacman3Direction = "l"
            else:
                
                data.pacman3Direction = random.choice(["l","d","r","u"])