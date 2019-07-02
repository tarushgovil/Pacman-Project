#112 Term Project
#Name: Tarush Govil
#Section: N
#andrew ID: tarushg
#Comment:contains the logic for the chasing algorithm for the ghosts in 
#singleplayer mode, as well as keeping track of coin count and powerups

from image_util import *
import random
from tkinter import *

def pacmanCoinInteract(data):

    row = int((data.imageYPac-data.margin)//data.cellSize)
    col = int((data.imageXPac-data.margin)//data.cellSize)
    if data.grid[row][col] == 7 and (data.imageYPac, data.imageXPac) not in (data.coinsVisited):
        data.coinsVisited.append((data.imageYPac,data.imageXPac))
        data.coinCount += 1
        
def pacmansCoinInteract(data):
    row = int((data.imageYPac-data.margin)//data.cellSize)
    col = int((data.imageXPac-data.margin)//data.cellSize)
    row2 = int((data.imageYPac2-data.margin)//data.cellSize)
    col2 = int((data.imageXPac2-data.margin)//data.cellSize) 
    if data.grid[row][col] == 7 and (data.imageXPac,data.imageYPac) not in (data.coinsVisited):
        data.coinsVisited.append((data.imageXPac,data.imageYPac))
        data.coinCount += 1
    elif data.grid[row2][col2] == 7 and (data.imageXPac2,data.imageYPac2) not in (data.coinsVisited):
        data.coinsVisited.append((data.imageXPac2,data.imageYPac2))
        data.coinCount2 += 1
        
def totalCoinCount(data):
    if data.coinCount == 178:
        data.mode = "winGameSingle"
        
        
def pacmanGhostInteract(data):
    
    row = int((data.imageYPac-data.margin)//data.cellSize)
    col = int((data.imageXPac-data.margin)//data.cellSize)
    data.Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    data.Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
    
    
    if (data.ghost1Image != data.scatterGhostImage and
        data.ghost2Image != data.scatterGhostImage and
        data.ghost3Image != data.scatterGhostImage and
        data.ghost4Image != data.scatterGhostImage): 
        if ((abs((data.imageXPac - data.imageXGhost1)) <= 0.001) and (abs(data.imageYPac - data.imageYGhost1) <= 0.001))  or ((abs(data.imageXPac - data.imageXGhost2) <= 0.001) \
        and (abs(data.imageYPac -data.imageYGhost2) <=0.001)) or ((abs(data.imageXPac -data.imageXGhost3) <= 0.001) and (abs(data.imageYPac - data.imageYGhost3) <=0.001))     \
        or ((abs(data.imageXPac - data.imageXGhost4) <= 0.001) and (abs(data.imageYPac - data.imageYGhost4) <= 0.001)):
            print("hi")
            print(abs(data.imageXPac -data.imageXGhost1))
            if data.mode == "playGameSingle":
                data.counterLives -= 1
                if data.counterLives <= 0:
                    data.mode = "youLose"
                    data.listOfHighScores.append(data.coinCount)
                    data.listOfHighScores.sort()
                    data.listOfHighScores.pop(0)
                    open("highscore.txt","wt").write(str(data.listOfHighScores))
                else:
                    data.imageXPac = 17*data.cellSize+data.margin + data.cellSize/2
                    data.imageYPac = 17*data.cellSize + data.margin + data.cellSize/2
            elif data.mode == "playGame":
                data.mode = "winGame2"
                
                
                
def pacmanFruit1Interact(data):
    if (data.imageXPac == data.imageXFruit1 and data.imageYPac == data.imageYFruit1 and data.fruit1Image != data.blackSquareImage):
        data.pacmanImage = data.biggerpacmanImage
        data.fruit1Image = data.blackSquareImage
        data.scatter = True
    
        
def pacmanFruit2Interact(data):
    if (data.imageXPac == data.imageXFruit2 and data.imageYPac == data.imageYFruit2 and data.fruit2Image != data.blackSquareImage):
        data.pacmanImage = data.biggerpacmanImage
        data.fruit2Image = data.blackSquareImage
        data.scatter = True
    
def pacmanFruit3Interact(data):
    if (data.imageXPac == data.imageXFruit3 and data.imageYPac == data.imageYFruit3 and data.fruit3Image != data.blackSquareImage):
        data.pacmanImage = data.biggerpacmanImage
        data.fruit3Image = data.blackSquareImage
        data.scatter = True
        
def pacmanFruit4Interact(data):
    if (data.imageXPac == data.imageXFruit4 and data.imageYPac == data.imageYFruit4 and data.fruit4Image != data.blackSquareImage):
        data.pacmanImage = data.biggerpacmanImage
        data.fruit4Image = data.blackSquareImage
        data.scatter = True
        
        
def ghost1HelperSingle(data):
    data.ghost1Image = PhotoImage(file = "canva-photo-editor-3.gif")
    data.count+=1
    
    data.Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    data.Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
    

    if abs(data.imageYPac - data.imageYGhost1) >= abs(data.imageXPac - data.imageXGhost1) and (data.imageYGhost1 <= data.imageYPac):
        if data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row + 1) < 20 and 1 <= data.Ghost1Col < 18:
            data.imageYGhost1 += data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col+1]!=1 and 1 <= data.Ghost1Row < 20 and 1 <= (data.Ghost1Col + 1) < 18:
                data.imageXGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col-1]!=1 and 1 <= data.Ghost1Row < 20 and 1<= (data.Ghost1Col -1) < 18:
                data.imageXGhost1 -= data.cellSize
            
            
    elif abs(data.imageYPac - data.imageYGhost1) >= abs(data.imageXPac - data.imageXGhost1) and (data.imageYGhost1 >= data.imageYPac):
        if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row - 1)< 20 and 1 <= data.Ghost1Col < 18:
            data.imageYGhost1 -= data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col+1]!= 1 and 1 <= data.Ghost1Row < 20 and 1 <= (data.Ghost1Col + 1) < 18:
                data.imageXGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col-1] != 1 and 1 <= data.Ghost1Row < 20 and 1<= (data.Ghost1Col -1) < 18:
                data.imageXGhost1 -= data.cellSize
            
    
    elif abs(data.imageYPac - data.imageYGhost1) <= abs(data.imageXPac - data.imageXGhost1) and (data.imageXGhost1 <= data.imageXPac):
        if data.grid[data.Ghost1Row][data.Ghost1Col+1]!=1 and 1 <= data.Ghost1Row < 20 and 1 <= (data.Ghost1Col + 1) < 18:
            data.imageXGhost1 += data.cellSize
        else: 
            if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row - 1)< 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row + 1) < 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 += data.cellSize
            
    elif abs(data.imageYPac - data.imageYGhost1) <= abs(data.imageXPac - data.imageXGhost1) and (data.imageXGhost1 >= data.imageXPac):
        if data.grid[data.Ghost1Row][data.Ghost1Col-1]!=1 and 1 <= data.Ghost1Row < 20 and 1<= (data.Ghost1Col -1) < 18:
            data.imageXGhost1 -= data.cellSize
        else: 
            if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row - 1)< 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row + 1) < 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 += data.cellSize
                
                
def ghost1Helper(data):
    data.ghost1Image = PhotoImage(file = "canva-photo-editor-3.gif")
    data.count+=1
    
    data.Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    data.Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
    

    
    
    if abs(data.imageYPac2 - data.imageYGhost1) >= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageYGhost1 <= data.imageYPac2):
        if data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row + 1) < 20 and 1 <= data.Ghost1Col < 18:
            data.imageYGhost1 += data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col+1]!=1 and 1 <= data.Ghost1Row < 20 and 1 <= (data.Ghost1Col + 1) < 18:
                data.imageXGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col-1]!=1 and 1 <= data.Ghost1Row < 20 and 1<= (data.Ghost1Col -1) < 18:
                data.imageXGhost1 -= data.cellSize
            
            
    elif abs(data.imageYPac2 - data.imageYGhost1) >= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageYGhost1 >= data.imageYPac2):
        if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row - 1)< 20 and 1 <= data.Ghost1Col < 18:
            data.imageYGhost1 -= data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col+1]!= 1 and 1 <= data.Ghost1Row < 20 and 1 <= (data.Ghost1Col + 1) < 18:
                data.imageXGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col-1] != 1 and 1 <= data.Ghost1Row < 20 and 1<= (data.Ghost1Col -1) < 18:
                data.imageXGhost1 -= data.cellSize
            
    
    elif abs(data.imageYPac2 - data.imageYGhost1) <= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageXGhost1 <= data.imageXPac2):
        if data.grid[data.Ghost1Row][data.Ghost1Col+1]!=1 and 1 <= data.Ghost1Row < 20 and 1 <= (data.Ghost1Col + 1) < 18:
            data.imageXGhost1 += data.cellSize
        else: 
            if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row - 1)< 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row + 1) < 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 += data.cellSize
            
    elif abs(data.imageYPac2 - data.imageYGhost1) <= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageXGhost1 >= data.imageXPac2):
        if data.grid[data.Ghost1Row][data.Ghost1Col-1]!=1 and 1 <= data.Ghost1Row < 20 and 1<= (data.Ghost1Col -1) < 18:
            data.imageXGhost1 -= data.cellSize
        else: 
            if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row - 1)< 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1 and 1 <= (data.Ghost1Row + 1) < 20 and 1 <= data.Ghost1Col < 18:
                data.imageYGhost1 += data.cellSize
                
                
def ghost1ScatterSingle(data):
    data.ghost1Image = data.scatterGhostImage
    data.Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    data.Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
    

    
    if abs(data.imageYPac - data.imageYGhost1) >= abs(data.imageXPac - data.imageXGhost1) and (data.imageYGhost1 <= data.imageYPac):
        if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1:
            data.imageYGhost1 -= data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col+1] !=1:
                data.imageXGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col-1]!= 1:
                data.imageXGhost1 -= data.cellSize
            
    elif abs(data.imageYPac - data.imageYGhost1) >= abs(data.imageXPac - data.imageXGhost1) and (data.imageYGhost1 >= data.imageYPac):
        if data.grid[data.Ghost1Row + 1][data.Ghost1Col]!=1:
            data.imageYGhost1 += data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col-1] !=1:
                data.imageXGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col+1]!=1:
                data.imageXGhost1 += data.cellSize
    
    elif abs(data.imageYPac - data.imageYGhost1) <= abs(data.imageXPac - data.imageXGhost1) and (data.imageXGhost1 <= data.imageXPac):
        if data.grid[data.Ghost1Row][data.Ghost1Col - 1]!=1:
            data.imageXGhost1 -= data.cellSize
        else: 
            if data.grid[data.Ghost1Row + 1][data.Ghost1Col]!=1:
                data.imageYGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1:
                data.imageYGhost1 -= data.cellSize
    elif abs(data.imageYPac - data.imageYGhost1) <= abs(data.imageXPac - data.imageXGhost1) and (data.imageXGhost1 >= data.imageXPac):
        if data.grid[data.Ghost1Row][data.Ghost1Col + 1]!=1:
            data.imageXGhost1 += data.cellSize
        else: 
            if data.grid[data.Ghost1Row-1][data.Ghost1Col]!= 1:
                data.imageYGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1:
                data.imageYGhost1 += data.cellSize
                
                
def ghost2ScatterSingle(data):
    
    data.ghost2Image = data.scatterGhostImage
    data.Ghost2Col = int((data.imageXGhost2-data.margin)//data.cellSize)
    data.Ghost2Row = int((data.imageYGhost2-data.margin)//data.cellSize)
    if abs(data.imageYPac - data.imageYGhost2) >= abs(data.imageXPac - data.imageXGhost2) and (data.imageYGhost2 <= data.imageYPac):
        if data.grid[data.Ghost2Row-1][data.Ghost2Col]!=1:
            data.imageYGhost2 -= data.cellSize
        else:
            if data.grid[data.Ghost2Row][data.Ghost2Col-1]!= 1:
                data.imageXGhost2 -= data.cellSize
            elif data.grid[data.Ghost2Row][data.Ghost2Col+1] !=1:
                data.imageXGhost2 += data.cellSize
            
            
            
            
    elif abs(data.imageYPac - data.imageYGhost2) >= abs(data.imageXPac - data.imageXGhost2) and (data.imageYGhost2 >= data.imageYPac):
        if data.grid[data.Ghost2Row + 1][data.Ghost2Col]!=1:
            data.imageYGhost2 += data.cellSize
        else:
            if  data.grid[data.Ghost2Row][data.Ghost2Col+1]!=1:
                data.imageXGhost2 += data.cellSize
            elif data.grid[data.Ghost2Row][data.Ghost2Col-1] !=1:
                data.imageXGhost2 -= data.cellSize
            
    
    elif abs(data.imageYPac - data.imageYGhost2) <= abs(data.imageXPac - data.imageXGhost2) and (data.imageXGhost2 <= data.imageXPac):
        if data.grid[data.Ghost2Row][data.Ghost2Col - 1]!=1:
            data.imageXGhost2 -= data.cellSize
        else: 
            if data.grid[data.Ghost2Row-1][data.Ghost2Col]!=1:
                data.imageYGhost2 -= data.cellSize
            elif data.grid[data.Ghost2Row + 1][data.Ghost2Col]!=1:
                data.imageYGhost2 += data.cellSize
            
    
    elif abs(data.imageYPac - data.imageYGhost2) <= abs(data.imageXPac - data.imageXGhost2) and (data.imageXGhost2 >= data.imageXPac):
        if data.grid[data.Ghost2Row][data.Ghost2Col + 1]!=1:
            data.imageXGhost2 += data.cellSize
        else: 
            if data.grid[data.Ghost2Row+1][data.Ghost2Col]!=1:
                data.imageYGhost2 += data.cellSize
            elif data.grid[data.Ghost2Row-1][data.Ghost2Col]!= 1:
                data.imageYGhost2 -= data.cellSize 
                
                
def ghost3HelperSingle(data):
    
    data.ghost3Image = PhotoImage(file = "canva-photo-editor.gif")
    data.Ghost3Col = int((data.imageXGhost3-data.margin)//data.cellSize)
    data.Ghost3Row = int((data.imageYGhost3-data.margin)//data.cellSize)
    

    if abs(data.imageYPac - data.imageYGhost3) >= abs(data.imageXPac - data.imageXGhost3) and (data.imageYGhost3 <= data.imageYPac):
        if data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row + 1) < 20 and 1 <= data.Ghost3Col < 18:
            data.imageYGhost3 += data.cellSize
        else:
            if data.grid[data.Ghost3Row][data.Ghost3Col-1]!=1 and 1 <= data.Ghost3Row < 20 and 1<= (data.Ghost3Col -1) < 18:
                data.imageXGhost3 -= data.cellSize
            elif data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1 and 1 <= data.Ghost3Row < 20 and 1 <= (data.Ghost3Col + 1) < 18:
                data.imageXGhost3 += data.cellSize
            
            

            
            
    elif abs(data.imageYPac - data.imageYGhost3) >= abs(data.imageXPac - data.imageXGhost3) and (data.imageYGhost3 >= data.imageYPac):
        if data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row - 1)< 20 and 1 <= data.Ghost3Col < 18:
            data.imageYGhost3 -= data.cellSize
        else:
            if data.grid[data.Ghost3Row][data.Ghost3Col-1]!=1 and 1 <= data.Ghost3Row < 20 and 1<= (data.Ghost3Col -1) < 18:
                data.imageXGhost3 -= data.cellSize
            elif data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1 and 1 <= data.Ghost3Row < 20 and 1 <= (data.Ghost3Col + 1) < 18:
                data.imageXGhost3 += data.cellSize
            
            
            
    
    elif abs(data.imageYPac - data.imageYGhost3) <= abs(data.imageXPac - data.imageXGhost3) and (data.imageXGhost3 <= data.imageXPac):
        if data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1 and 1 <= data.Ghost3Row < 20 and 1 <= (data.Ghost3Col + 1) < 18:
            data.imageXGhost3 += data.cellSize
        else: 
            if  data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row + 1) < 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 += data.cellSize
            elif data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row - 1)< 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 -= data.cellSize
            
            
    elif abs(data.imageYPac - data.imageYGhost3) <= abs(data.imageXPac - data.imageXGhost3) and (data.imageXGhost3 >= data.imageXPac):
        if data.grid[data.Ghost3Row][data.Ghost3Col-1]!=1 and 1 <= data.Ghost3Row < 20 and 1<= (data.Ghost3Col -1) < 18:
            data.imageXGhost3 -= data.cellSize
        else: 
            if  data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row + 1) < 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 += data.cellSize
            elif data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row - 1)< 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 -= data.cellSize
        

