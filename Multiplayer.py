#112 Term Project
#Name: Tarush Govil
#Section: N
#andrew ID: tarushg
#Comment:contains the chasing algorithm for the ghosts 
#in multiplayer mode, keeps track of coin count, 
#and includes the code for pacman hitting a power up


from image_util import *
import random
from tkinter import *

def pacman2CoinInteract(data):
    
    row2 = int((data.imageYPac2-data.margin)//data.cellSize)
    col2 = int((data.imageXPac2-data.margin)//data.cellSize) 
    if data.grid[row2][col2] == 7 and (data.imageYPac2, data.imageXPac2) not in (data.coinsVisited2 and data.coinsVisited):
        data.coinsVisited2.append((data.imageYPac2,data.imageXPac2))
        
        data.coinCount2 += 1
        
def totalCoinCount2(data):
    if data.coinCount + data.coinCount2 == 177:
        if data.coinCount > data.coinCount2:
            data.mode = "winGame"
        elif data.coinCount2 > data.coinCount:
            data.mode = "winGame2"
            
def pacman2GhostInteract(data):
    row2 = int((data.imageYPac2-data.margin)//data.cellSize)
    col2 = int((data.imageXPac2-data.margin)//data.cellSize)
    data.Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    data.Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
    
    
    if (data.ghost1Image != data.scatterGhostImage and data.ghost2Image != data.scatterGhostImage and data.ghost3Image != data.scatterGhostImage and \
        data.ghost4Image != data.scatterGhostImage): 
        if (data.imageXPac2 == data.imageXGhost1 and data.imageYPac2 == data.imageYGhost1) or (data.imageXPac2 == data.imageXGhost2 and data.imageYPac2 == data.imageYGhost2) \
        or (data.imageXPac2 == data.imageXGhost3 and data.imageYPac2 == data.imageYGhost3) or (data.imageXPac2 == data.imageXGhost4 and data.imageYPac2 == data.imageYGhost4):
            print(abs(data.imageXPac -data.imageXGhost1))
            data.mode = "winGame"
            
            
            
def pacman2Fruit1Interact(data):
    if (data.imageXPac2 == data.imageXFruit1 and data.imageYPac2 == data.imageYFruit1 and data.fruit1Image != data.blackSquareImage):
        data.pacman2Image = data.biggerpacman2Image
        data.fruit1Image = data.blackSquareImage
        data.scatter = True


def pacman2Fruit2Interact(data):
    if (data.imageXPac2 == data.imageXFruit2 and data.imageYPac2 == data.imageYFruit2 and data.fruit2Image != data.blackSquareImage):
        data.pacman2Image = data.biggerpacman2Image
        data.fruit2Image = data.blackSquareImage
        data.scatter = True
        
        
def pacman2Fruit3Interact(data):
    if (data.imageXPac2 == data.imageXFruit3 and data.imageYPac2 == data.imageYFruit3 and data.fruit3Image != data.blackSquareImage):
        data.pacman2Image = data.biggerpacman2Image
        data.fruit3Image = data.blackSquareImage
        data.scatter = True
        

def pacman2Fruit4Interact(data):
    if (data.imageXPac2 == data.imageXFruit4 and data.imageYPac2 == data.imageYFruit4 and data.fruit4Image != data.blackSquareImage):
        data.pacman2Image = data.biggerpacman2Image
        data.fruit4Image = data.blackSquareImage
        data.scatter = True
    
    
def pacmanpacman2Interact(data):
    if (data.imageXPac2 == data.imageXPac and data.imageYPac2 == data.imageYPac):
        if (data.pacmanImage == data.biggerpacmanImage and data.pacman2Image != data.biggerpacman2Image):
            data.mode = "winGame"
        elif (data.pacman2Image == data.biggerpacman2Image and data.pacmanImage != data.biggerpacmanImage):
            data.mode = "winGame2"
            
            
def ghost1Scatter(data):
    data.ghost1Image = data.scatterGhostImage
    data.Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    data.Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
    

    if abs(data.imageYPac2 - data.imageYGhost1) >= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageYGhost1 <= data.imageYPac2):
        if data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1:
            data.imageYGhost1 -= data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col+1] !=1:
                data.imageXGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col-1]!= 1:
                data.imageXGhost1 -= data.cellSize
            
    elif abs(data.imageYPac2 - data.imageYGhost1) >= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageYGhost1 >= data.imageYPac2):
        if data.grid[data.Ghost1Row + 1][data.Ghost1Col]!=1:
            data.imageYGhost1 += data.cellSize
        else:
            if data.grid[data.Ghost1Row][data.Ghost1Col-1] !=1:
                data.imageXGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row][data.Ghost1Col+1]!=1:
                data.imageXGhost1 += data.cellSize
    
    elif abs(data.imageYPac2 - data.imageYGhost1) <= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageXGhost1 <= data.imageXPac2):
        if data.grid[data.Ghost1Row][data.Ghost1Col - 1]!=1:
            data.imageXGhost1 -= data.cellSize
        else: 
            if data.grid[data.Ghost1Row + 1][data.Ghost1Col]!=1:
                data.imageYGhost1 += data.cellSize
            elif data.grid[data.Ghost1Row-1][data.Ghost1Col]!=1:
                data.imageYGhost1 -= data.cellSize
    elif abs(data.imageYPac2 - data.imageYGhost1) <= abs(data.imageXPac2 - data.imageXGhost1) and (data.imageXGhost1 >= data.imageXPac2):
        if data.grid[data.Ghost1Row][data.Ghost1Col + 1]!=1:
            data.imageXGhost1 += data.cellSize
        else: 
            if data.grid[data.Ghost1Row-1][data.Ghost1Col]!= 1:
                data.imageYGhost1 -= data.cellSize
            elif data.grid[data.Ghost1Row+1][data.Ghost1Col]!=1:
                data.imageYGhost1 += data.cellSize
                
                

def ghost2Helper(data):
    
    data.ghost2Image = PhotoImage(file = "ghost3.gif")
    data.Ghost2Col = int((data.imageXGhost2-data.margin)//data.cellSize)
    data.Ghost2Row = int((data.imageYGhost2-data.margin)//data.cellSize)

    

    
    if data.count % 2 == 0:
        
        if data.grid[data.Ghost2Row + 1][data.Ghost2Col]!=1 and data.grid[data.Ghost2Row - 1][data.Ghost2Col]!=1:

            data.imageYGhost2 += random.choice([-1*data.cellSize,data.cellSize])
    
        elif data.grid[data.Ghost2Row + 1][data.Ghost2Col]!=1:

            data.imageYGhost2 += data.cellSize
      
        elif data.grid[data.Ghost2Row - 1][data.Ghost2Col]!=1:

            data.imageYGhost2 -= data.cellSize
    
        else:

            data.imageYGhost2 = data.imageYGhost2


    else:

        if data.grid[data.Ghost2Row][data.Ghost2Col + 1]!=1 and data.grid[data.Ghost2Row][data.Ghost2Col - 1]!=1:

            data.imageXGhost2 += random.choice([-1*data.cellSize,data.cellSize])

        elif data.grid[data.Ghost2Row][data.Ghost2Col + 1]!=1:

            data.imageXGhost2 += data.cellSize

        elif data.grid[data.Ghost2Row][data.Ghost2Col - 1]!=1:

            data.imageXGhost2 -= data.cellSize

        else:

            data.imageXGhost2 = data.imageXGhost2
            
            
def ghost2Scatter(data):
    
    data.ghost2Image = data.scatterGhostImage
    data.Ghost2Col = int((data.imageXGhost2-data.margin)//data.cellSize)
    data.Ghost2Row = int((data.imageYGhost2-data.margin)//data.cellSize)
    if abs(data.imageYPac2 - data.imageYGhost2) >= abs(data.imageXPac2 - data.imageXGhost2) and (data.imageYGhost2 <= data.imageYPac2):
        if data.grid[data.Ghost2Row-1][data.Ghost2Col]!=1:
            data.imageYGhost2 -= data.cellSize
        else:
            if data.grid[data.Ghost2Row][data.Ghost2Col-1]!= 1:
                data.imageXGhost2 -= data.cellSize
            elif data.grid[data.Ghost2Row][data.Ghost2Col+1] !=1:
                data.imageXGhost2 += data.cellSize
            
            
            
            
    elif abs(data.imageYPac2 - data.imageYGhost2) >= abs(data.imageXPac2 - data.imageXGhost2) and (data.imageYGhost2 >= data.imageYPac2):
        if data.grid[data.Ghost2Row + 1][data.Ghost2Col]!=1:
            data.imageYGhost2 += data.cellSize
        else:
            if  data.grid[data.Ghost2Row][data.Ghost2Col+1]!=1:
                data.imageXGhost2 += data.cellSize
            elif data.grid[data.Ghost2Row][data.Ghost2Col-1] !=1:
                data.imageXGhost2 -= data.cellSize
            
    
    elif abs(data.imageYPac2 - data.imageYGhost2) <= abs(data.imageXPac2 - data.imageXGhost2) and (data.imageXGhost2 <= data.imageXPac2):
        if data.grid[data.Ghost2Row][data.Ghost2Col - 1]!=1:
            data.imageXGhost2 -= data.cellSize
        else: 
            if data.grid[data.Ghost2Row-1][data.Ghost2Col]!=1:
                data.imageYGhost2 -= data.cellSize
            elif data.grid[data.Ghost2Row + 1][data.Ghost2Col]!=1:
                data.imageYGhost2 += data.cellSize
            
    
    elif abs(data.imageYPac2 - data.imageYGhost2) <= abs(data.imageXPac2 - data.imageXGhost2) and (data.imageXGhost2 >= data.imageXPac2):
        if data.grid[data.Ghost2Row][data.Ghost2Col + 1]!=1:
            data.imageXGhost2 += data.cellSize
        else: 
            if data.grid[data.Ghost2Row+1][data.Ghost2Col]!=1:
                data.imageYGhost2 += data.cellSize
            elif data.grid[data.Ghost2Row-1][data.Ghost2Col]!= 1:
                data.imageYGhost2 -= data.cellSize
                
                
                
def ghost3Helper(data):
    
    data.ghost3Image = PhotoImage(file = "canva-photo-editor.gif")
    data.Ghost3Col = int((data.imageXGhost3-data.margin)//data.cellSize)
    data.Ghost3Row = int((data.imageYGhost3-data.margin)//data.cellSize)
    

    
   
    if abs(data.imageYPac - data.imageYGhost3) >= abs(data.imageXPac - data.imageXGhost3) and (data.imageYGhost3 <= data.imageYPac):
        if data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row + 1) < 20 and 1 <= data.Ghost3Col < 18:
            data.imageYGhost3 += data.cellSize
        else:
            if data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1 and 1 <= data.Ghost3Row < 20 and 1 <= (data.Ghost3Col + 1) < 18:
                data.imageXGhost3 += data.cellSize
            elif data.grid[data.Ghost3Row][data.Ghost3Col-1]!=1 and 1 <= data.Ghost3Row < 20 and 1<= (data.Ghost3Col -1) < 18:
                data.imageXGhost3 -= data.cellSize
            
            
    elif abs(data.imageYPac - data.imageYGhost3) >= abs(data.imageXPac - data.imageXGhost3) and (data.imageYGhost3 >= data.imageYPac):
        if data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row - 1)< 20 and 1 <= data.Ghost3Col < 18:
            data.imageYGhost3 -= data.cellSize
        else:
            if data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1 and 1 <= data.Ghost3Row < 20 and 1 <= (data.Ghost3Col + 1) < 18:
                data.imageXGhost3 += data.cellSize
            elif data.grid[data.Ghost3Row][data.Ghost3Col-1]!=1 and 1 <= data.Ghost3Row < 20 and 1<= (data.Ghost3Col -1) < 18:
                data.imageXGhost3 -= data.cellSize
            
    
    elif abs(data.imageYPac - data.imageYGhost3) <= abs(data.imageXPac - data.imageXGhost3) and (data.imageXGhost3 <= data.imageXPac):
        if data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1 and 1 <= data.Ghost3Row < 20 and 1 <= (data.Ghost3Col + 1) < 18:
            data.imageXGhost3 += data.cellSize
        else: 
            if data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row - 1)< 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 -= data.cellSize
            elif data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row + 1) < 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 += data.cellSize
            
    elif abs(data.imageYPac - data.imageYGhost3) <= abs(data.imageXPac - data.imageXGhost3) and (data.imageXGhost3 >= data.imageXPac):
        if data.grid[data.Ghost3Row][data.Ghost3Col-1]!=1 and 1 <= data.Ghost3Row < 20 and 1<= (data.Ghost3Col -1) < 18:
            data.imageXGhost3 -= data.cellSize
        else: 
            if data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row - 1)< 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 -= data.cellSize
            elif data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1 and 1 <= (data.Ghost3Row + 1) < 20 and 1 <= data.Ghost3Col < 18:
                data.imageYGhost3 += data.cellSize
                
                
def ghost3Scatter(data):
    
    data.ghost3Image = data.scatterGhostImage
    data.Ghost3Col = int((data.imageXGhost3-data.margin)//data.cellSize)
    data.Ghost3Row = int((data.imageYGhost3-data.margin)//data.cellSize)
    
    if abs(data.imageYPac - data.imageYGhost3) >= abs(data.imageXPac - data.imageXGhost3) and (data.imageYGhost3 <= data.imageYPac):
        if data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1:
            data.imageYGhost3 -= data.cellSize
        else:
            if data.grid[data.Ghost3Row][data.Ghost3Col+1] !=1:
                data.imageXGhost3 += data.cellSize
            elif data.grid[data.Ghost3Row][data.Ghost3Col-1]!= 1:
                data.imageXGhost3 -= data.cellSize
            
    elif abs(data.imageYPac - data.imageYGhost3) >= abs(data.imageXPac - data.imageXGhost3) and (data.imageYGhost3 >= data.imageYPac):
        if data.grid[data.Ghost3Row + 1][data.Ghost3Col]!=1:
            data.imageYGhost3 += data.cellSize
        else:
            if data.grid[data.Ghost3Row][data.Ghost3Col-1] !=1:
                data.imageXGhost3 -= data.cellSize
            elif data.grid[data.Ghost3Row][data.Ghost3Col+1]!=1:
                data.imageXGhost3 += data.cellSize
    
    elif abs(data.imageYPac - data.imageYGhost3) <= abs(data.imageXPac - data.imageXGhost3) and (data.imageXGhost3 <= data.imageXPac):
        if data.grid[data.Ghost3Row][data.Ghost3Col - 1]!=1:
            data.imageXGhost3 -= data.cellSize
        else: 
            if data.grid[data.Ghost3Row + 1][data.Ghost3Col]!=1:
                data.imageYGhost3 += data.cellSize
            elif data.grid[data.Ghost3Row-1][data.Ghost3Col]!=1:
                data.imageYGhost3 -= data.cellSize
    elif abs(data.imageYPac - data.imageYGhost3) <= abs(data.imageXPac - data.imageXGhost3) and (data.imageXGhost3 >= data.imageXPac):
        if data.grid[data.Ghost3Row][data.Ghost3Col + 1]!=1:
            data.imageXGhost3 += data.cellSize
        else: 
            if data.grid[data.Ghost3Row-1][data.Ghost3Col]!= 1:
                data.imageYGhost3 -= data.cellSize
            elif data.grid[data.Ghost3Row+1][data.Ghost3Col]!=1:
                data.imageYGhost3 += data.cellSize
                
                
def ghost4Helper(data):

    data.Ghost4Row = int((data.imageYGhost4-data.margin)//data.cellSize)
    data.Ghost4Col = int((data.imageXGhost4-data.margin)//data.cellSize)
    data.ghost4Image = PhotoImage(file = "canva-photo-editor-2.gif")
    
    if data.count % 2 == 0:
        
        if data.grid[data.Ghost4Row + 1][data.Ghost4Col]!=1 and data.grid[data.Ghost4Row - 1][data.Ghost4Col]!=1:

            data.imageYGhost4 += random.choice([-1*data.cellSize,data.cellSize])
    
        elif data.grid[data.Ghost4Row + 1][data.Ghost4Col]!=1:

            data.imageYGhost4 += data.cellSize
      
        elif data.grid[data.Ghost4Row - 1][data.Ghost4Col]!=1:

            data.imageYGhost4 -= data.cellSize
    
        else:

            data.imageYGhost4 = data.imageYGhost4

    else:

        if data.grid[data.Ghost4Row][data.Ghost4Col + 1]!=1 and data.grid[data.Ghost4Row][data.Ghost4Col - 1]!=1:

            data.imageXGhost4 += random.choice([-1*data.cellSize,data.cellSize])

        elif data.grid[data.Ghost4Row][data.Ghost4Col + 1]!=1:

            data.imageXGhost4 += data.cellSize

        elif data.grid[data.Ghost4Row][data.Ghost4Col - 1]!=1:

            data.imageXGhost4 -= data.cellSize

        else:

            data.imageXGhost4 = data.imageXGhost4
            
            
def ghost4Scatter(data):
    data.ghost4Image = data.scatterGhostImage
    data.Ghost4Col = int((data.imageXGhost4-data.margin)//data.cellSize)
    data.Ghost4Row = int((data.imageYGhost4-data.margin)//data.cellSize)
    
    if abs(data.imageYPac - data.imageYGhost4) >= abs(data.imageXPac - data.imageXGhost4) and (data.imageYGhost4 <= data.imageYPac):
        if data.grid[data.Ghost4Row-1][data.Ghost4Col]!=1:
            data.imageYGhost4 -= data.cellSize
        else:
            if  data.grid[data.Ghost4Row][data.Ghost4Col-1]!= 1:
                data.imageXGhost4 -= data.cellSize
            elif data.grid[data.Ghost4Row][data.Ghost4Col+1] !=1:
                data.imageXGhost4 += data.cellSize
            
            
            
    elif abs(data.imageYPac - data.imageYGhost4) >= abs(data.imageXPac - data.imageXGhost4) and (data.imageYGhost4 >= data.imageYPac):
        if data.grid[data.Ghost4Row + 1][data.Ghost4Col]!=1:
            data.imageYGhost4 += data.cellSize
        else:
            if data.grid[data.Ghost4Row][data.Ghost4Col+1]!=1:
                data.imageXGhost4 += data.cellSize
            elif data.grid[data.Ghost4Row][data.Ghost4Col-1] !=1:
                data.imageXGhost4 -= data.cellSize
            
            
    elif abs(data.imageYPac - data.imageYGhost4) <= abs(data.imageXPac - data.imageXGhost4) and (data.imageXGhost4 <= data.imageXPac):
        if data.grid[data.Ghost4Row][data.Ghost4Col - 1]!=1:
            data.imageXGhost4 -= data.cellSize
        else: 
            if data.grid[data.Ghost4Row-1][data.Ghost4Col]!=1:
                data.imageYGhost4 -= data.cellSize
            elif data.grid[data.Ghost4Row + 1][data.Ghost4Col]!=1:
                data.imageYGhost4 += data.cellSize

    elif abs(data.imageYPac - data.imageYGhost4) <= abs(data.imageXPac - data.imageXGhost4) and (data.imageXGhost4 >= data.imageXPac):
        if data.grid[data.Ghost4Row][data.Ghost4Col + 1]!=1:
            data.imageXGhost4 += data.cellSize
        else: 
            if data.grid[data.Ghost4Row+1][data.Ghost4Col]!=1:
                data.imageYGhost4 += data.cellSize
            elif data.grid[data.Ghost4Row-1][data.Ghost4Col]!= 1:
                data.imageYGhost4 -= data.cellSize