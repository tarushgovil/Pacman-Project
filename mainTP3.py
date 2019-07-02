#112 Term Project
#Name: Tarush Govil
#Section: N
#andrew ID: tarushg
#contains the initialization of data,timerfired, 
#and all things drawn on the board


from tkinter import *
from image_util import *
from ghostmode import *
from Singleplayer import *
from Multiplayer import*
import random


def init(data):
    #Citations: http://wxec.info/yellow-circle-s-on-a-black-background.html
    data.pacmanImage = PhotoImage(file = "canva-photo-editor-6.gif")
    data.biggerpacmanImage = PhotoImage(file = "canva-photo-editor-9.gif")
    #Citations: https://www.kisspng.com/png-pac-man-games-ghosts-blue-ghost-cliparts-160316/
    data.ghost1Image = PhotoImage(file = "canva-photo-editor-3.gif")
    #Citations: https://www.kisspng.com/png-pac-man-adventures-in-time-pac-mania-pac-man-games-582853/
    data.ghost2Image = PhotoImage(file = "ghost3.gif")
    #Citations: https://www.kisspng.com/png-ms-pac-man-ghosts-class-board-4186180/
    data.ghost3Image = PhotoImage(file = "canva-photo-editor.gif")
    #Citations: https://www.kisspng.com/png-pac-man-ghosts-pac-man-972380/
    data.ghost4Image = PhotoImage(file = "canva-photo-editor-2.gif")
    #Citations: https://www.flickr.com/photos/johannes-p-osterhoff/4544827697
    data.blackSquareImage = PhotoImage(file = "canva-photo-editor-11.gif")
    #Citations: https://dev.to/code2bits/pac-man-patterns--ghost-movement-strategy-pattern-1k1a
    data.scatterGhostImage = PhotoImage(file = "canva-photo-editor-24.png")
    #Citations: https://www.dotit.com/dark-purple-3-4-dissolve-it-solid-color-1000-rl.html
    data.pacman2Image = PhotoImage(file = "canva-photo-editor-17.gif")
    #Citations: http://octattoogabe.com/2012/wp-#content/uploads/2012/07/f_1_black_flag_with_orange_circle_tattoo_tatoo-999px.png
    #?fbclid=IwAR15Gnj7AC_uJOAioEj0Yiv42OcAjjqMkEUv4PrApYrjKxPdCr7oU72m0TE
    data.pacman3Image = PhotoImage(file = "canva-photo-editor-66.png")
    data.biggerpacman2Image = PhotoImage(file = "canva-photo-editor-18.gif")
    #Citations:https://www.gmkfreelogos.com/15379-Pac-Man.html
    data.pacmanTitle = PhotoImage(file ="canva-photo-editor-39.png")
    #Citations: https://bjhoughtonblog.wordpress.com/2016/12/21/high-score/
    data.highScoreTitle = PhotoImage(file ="canva-photo-editor-62.png")
    #Citations: https://gamejolt.com/games/pacman-i-reborn/158025
    data.youWinTitle = PhotoImage(file ="canva-photo-editor-89.png")
    #Citations:http://adventuretime.wikia.com/wiki/File:S2e16_You_lose.png
    data.youLoseTitle = PhotoImage(file ="canva-photo-editor-72.png")
    #Citations: https://www.shutterstock.com/video/clip-22752961-pixel-art-game-style-message-over-hd
    data.gameOverTitle = PhotoImage(file ="canva-photo-editor-44.png")
    data.rows = 21
    data.cols = 19
    data.margin = 25
    data.cellSize = 20
    #Citations:(same image used for all 4) https://www.clipartmax.com/middle/m2i8G6A0b1G6H7N4_grapes-clipart-pacman-fruit-pac-man-strawberry/)
    data.fruit1Image = PhotoImage(file = "canva-photo-editor-21.png")
    data.fruit2Image = PhotoImage(file = "canva-photo-editor-22.png")
    data.fruit3Image = PhotoImage(file = "canva-photo-editor-22.png")
    data.fruit4Image = PhotoImage(file = "canva-photo-editor-22.png")
    data.pacmanUpNew = False
    data.pacmanDownNew = False
    data.pacmanRightNew = False
    data.pacmanLeftNew = False
    data.pacmanDirection = "u"
    data.pacman2Direction = "d"
    data.pacman3Direction = "r"
    data.highscore = 0
    #Citations: https://imgur.com/gallery/obojRZ5
    data.pacmanGif = PhotoImage(file = "obojRZ5.gif")
    data.counterLives = 3
    data.ghostCounter = 0
    data.timeLeft = 90
    data.pacman1 = True
    data.pacman2 = True
    data.pacman3 = True

    data.grid = [[1]*19,
                [1,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3,1],\
                [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],\
                [1,0,0,8,0,0,0,0,0,0,0,0,0,0,0,12,0,0,1],\
                [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],\
                [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],\
                [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,10,0,0,0,0,0,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1],\
                [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],\
                [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,0,1,1,1,0,1,0,1,1,1,9,1,1,0,1],\
                [1,11,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],\
                [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],\
                [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,6,1],\
                [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],\
                [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1],\
                [1]*19]
                
                
    data.newGrid = [[1]*19,
                [1,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],\
                [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,11,0,1],\
                [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],\
                [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],\
                [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1],\
                [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],\
                [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],\
                [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],\
                [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],\
                [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],\
                [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,6,1],\
                [1,0,10,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1]*19]
                
                
                

    data.pacmanUp = False
    data.pacmanDown = False
    data.pacmanLeft = False
    data.pacmanRight = False
    data.pacman2Up = False
    data.pacman2Down = False
    data.pacman2Left = False
    data.pacman2Right = False
    data.pacManSpeed = 1
    data.imageXPac = 17*data.cellSize+data.margin + data.cellSize/2
    data.imageYPac = 17*data.cellSize + data.margin + data.cellSize/2
    data.imageXPac2 = 7*data.cellSize+data.margin + data.cellSize/2
    data.imageYPac2 = 7*data.cellSize+data.margin + data.cellSize/2
    data.imageXPac2New = 2*data.cellSize+data.margin + data.cellSize/2
    data.imageYPac2New = 18*data.cellSize+data.margin + data.cellSize/2
    data.imageXPac3 = 16*data.cellSize+data.margin + data.cellSize/2
    data.imageYPac3 = 3*data.cellSize+data.margin + data.cellSize/2
    
    data.mode = "startGame"
    data.coinCount = 0
    data.coinCount2 = 0
    data.coinsVisited = []
    data.coinsVisited2 = []
    data.collision = False
    data.scatterCount = 50
    data.pacmanGifX = data.width/2 
    data.pacmanGifY = data.height/2 + 20 
    data.listOfHighScores = eval(open("highscore.txt","rt").read())
    

    data.timerCalls = 0
    
    
    
    data.imageXFruit1 = 3*data.cellSize + data.margin + data.cellSize/2
    data.imageYFruit1 = 3*data.cellSize + data.margin + data.cellSize/2
    
    data.imageXFruit2 = 14*data.cellSize + data.margin + data.cellSize/2
    data.imageYFruit2 = 14*data.cellSize + data.margin + data.cellSize/2
    
    data.imageXFruit3 = 15*data.cellSize + data.margin + data.cellSize/2
    data.imageYFruit3 = 3*data.cellSize + data.margin + data.cellSize/2
    
    data.imageXFruit4 = 1*data.cellSize + data.margin + data.cellSize/2
    data.imageYFruit4 = 15*data.cellSize + data.margin + data.cellSize/2
    
    data.imageXGhost1 = 1*data.cellSize + data.margin + data.cellSize/2
    data.imageYGhost1 = 1*data.cellSize + data.margin + data.cellSize/2

    data.imageXGhost2 = 17*data.cellSize + data.margin + data.cellSize/2
    data.imageYGhost2 = 1*data.cellSize + data.margin + data.cellSize/2

    data.imageXGhost3 = 1*data.cellSize + data.margin + data.cellSize/2
    data.imageYGhost3 = 19*data.cellSize + data.margin + data.cellSize/2

    data.imageXGhost4 = 17*data.cellSize + data.margin + data.cellSize/2
    data.imageYGhost4 = 19*data.cellSize + data.margin + data.cellSize/2
    
    data.Ghost1Up = False
    data.Ghost1Down = False
    data.Ghost1Left = True
    data.Ghost1Right = False
    
    data.canMoveRight = True
    data.canMoveLeft = True
    data.count = 0
    data.scatter = False
    data.randomTimer = 0
    data.previousDirection = ""
   


    
def drawCell(canvas,data,row,col):
  
                                      

    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_rectangle(leftMost,topMost,leftMost + data.cellSize,
                    topMost + data.cellSize,fill="blue")
    
def drawBoard2(canvas,data):
    
    row = int((data.imageYPac-data.margin)//data.cellSize)
    col = int((data.imageXPac-data.margin)//data.cellSize)
    row2 = int((data.imageYPac2-data.margin)//data.cellSize)
    col2 = int((data.imageXPac2-data.margin)//data.cellSize)
    

    if data.grid[row][col] == 0:
        
        data.grid[row][col] = 7
        
    if data.grid[row2][col2] == 0:
        data.grid[row2][col2] = 7
    
    for i in range(len(data.grid)):
        for j in range(len(data.grid[0])):
            if data.grid[i][j] == 1:
                drawCell(canvas,data,i,j)
            if data.grid[i][j] == 0:
                drawCoins(canvas,data,i,j)
            if data.grid[i][j] == 8:
                drawFruit1(canvas,data,i,j)
            if data.grid[i][j] == 9:
                drawFruit2(canvas,data,i,j)
            if data.grid[i][j] == 12:
                drawFruit3(canvas,data,i,j)
            if data.grid[i][j] == 11:
                drawFruit4(canvas,data,i,j)
            if data.grid[i][j] == 7:
                drawBlackBox(canvas,data,i,j)
                drawPacman2(canvas,data,i,j)
                drawPacman(canvas,data,i,j)
                drawGhost1(canvas,data,i,j)
                drawGhost2(canvas,data,i,j)
                drawGhost3(canvas,data,i,j)
                drawGhost4(canvas,data,i,j)
            if data.grid[i][j] == 6:
                drawPacman(canvas,data,i,j)
            if data.grid[i][j] == 10:
                drawPacman2(canvas,data,i,j)
            if data.grid[i][j] == 2:
                drawGhost1(canvas,data,i,j)
            if data.grid[i][j] == 3:
                drawGhost2(canvas,data,i,j)
            if data.grid[i][j] == 4:
                drawGhost3(canvas,data,i,j)
            if data.grid[i][j] == 5:
                drawGhost4(canvas,data,i,j)
           
            
            
            
            
            
def drawBoard1(canvas,data):
    row = int((data.imageYPac-data.margin)//data.cellSize)
    col = int((data.imageXPac-data.margin)//data.cellSize)

    if data.grid[row][col] == 0:
        data.grid[row][col] = 7
        
    if  data.grid[row][col] == 10:
         data.grid[row][col] = 7
    
    for i in range(len(data.grid)):
        for j in range(len(data.grid[0])):
            if data.grid[i][j] == 1:
                drawCell(canvas,data,i,j)
            if data.grid[i][j] == 0:
                drawCoins(canvas,data,i,j)
            if data.grid[i][j] == 10:
                drawCoins(canvas,data,i,j)
            if data.grid[i][j] == 8:
                drawFruit1(canvas,data,i,j)
            if data.grid[i][j] == 9:
                drawFruit2(canvas,data,i,j)
            if data.grid[i][j] == 12:
                drawFruit3(canvas,data,i,j)
            if data.grid[i][j] == 11:
                drawFruit4(canvas,data,i,j)
            if data.grid[i][j] == 7:
                drawBlackBox(canvas,data,i,j)
                drawPacman(canvas,data,i,j)
                drawGhost1(canvas,data,i,j)
                drawGhost2(canvas,data,i,j)
                drawGhost3(canvas,data,i,j)
                drawGhost4(canvas,data,i,j)
            if data.grid[i][j] == 6:
                drawPacman(canvas,data,i,j)
            if data.grid[i][j] == 2:
                drawGhost1(canvas,data,i,j)
            if data.grid[i][j] == 3:
                drawGhost2(canvas,data,i,j)
            if data.grid[i][j] == 4:
                drawGhost3(canvas,data,i,j)
            if data.grid[i][j] == 5:
                drawGhost4(canvas,data,i,j)
            
            
            
def drawBoard3(canvas,data):
    row = int((data.imageYPac-data.margin)//data.cellSize)
    col = int((data.imageXPac-data.margin)//data.cellSize)
    row2 = int((data.imageYPac2New-data.margin)//data.cellSize)
    col2 = int((data.imageXPac2New-data.margin)//data.cellSize)
    row3 = int((data.imageYPac3-data.margin)//data.cellSize)
    col3 = int((data.imageXPac3-data.margin)//data.cellSize)

    if data.newGrid[row][col] == 0:
        
        data.newGrid[row][col] = 7
    
    if data.newGrid[row2][col2] == 0:
        data.newGrid[row2][col2] = 7
        
    if data.newGrid[row3][col3] == 0:
        data.newGrid[row3][col3] = 7
        
    
    
    for i in range(len(data.newGrid)):
        for j in range(len(data.newGrid[0])):
            if data.newGrid[i][j] == 1:
                drawCell(canvas,data,i,j)
            if data.newGrid[i][j] == 0:
                drawCoins(canvas,data,i,j)
            if data.newGrid[i][j] == 7:
                drawBlackBox(canvas,data,i,j)
                drawPacman3(canvas,data,i,j)
                drawPacman2New(canvas,data,i,j)
                drawPacmanNew(canvas,data,i,j)
                drawGhost1(canvas,data,i,j)
            if data.newGrid[i][j] == 6:
                drawPacmanNew(canvas,data,i,j)
            if data.newGrid[i][j] == 10:
                drawPacman2New(canvas,data,i,j)
            if data.newGrid[i][j] == 11:
                drawPacman3(canvas,data,i,j)
            if data.newGrid[i][j] == 2:
                drawGhost1(canvas,data,i,j)
    

def drawPacman(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXPac,data.imageYPac,image = data.pacmanImage)
    
def drawPacmanNew(canvas,data,row,col):
    if data.pacman1 == True:
        leftMost = col*data.cellSize+data.margin 
        topMost = row*data.cellSize +data.margin
        canvas.create_image(data.imageXPac,data.imageYPac,image = data.pacmanImage)
    
    
def drawPacman2(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXPac2,data.imageYPac2,image = data.pacman2Image)
    
def drawPacman2New(canvas,data,row,col):
    if data.pacman2 == True:
        leftMost = col*data.cellSize+data.margin 
        topMost = row*data.cellSize +data.margin
        canvas.create_image(data.imageXPac2New,data.imageYPac2New,image = data.pacman2Image)
    
    
def drawPacman3(canvas,data,row,col):
    if data.pacman3 == True:
        leftMost = col*data.cellSize+data.margin 
        topMost = row*data.cellSize +data.margin
        canvas.create_image(data.imageXPac3,data.imageYPac3,image = data.pacman3Image)
    
def drawGhost1(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXGhost1,data.imageYGhost1,image = data.ghost1Image)        

def drawGhost2(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXGhost2,data.imageYGhost2,image = data.ghost2Image) 
    
    
                    
def drawGhost3(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXGhost3,data.imageYGhost3,image = data.ghost3Image)
                    
def drawGhost4(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXGhost4,data.imageYGhost4,image = data.ghost4Image) 
    
        
def drawCoins(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_oval(leftMost + 5,topMost + 5,leftMost + (data.cellSize - 10),
                    topMost + (data.cellSize - 10),fill="yellow")
                    

def drawFruit1(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXFruit1,data.imageYFruit1,image = data.fruit1Image) 
    
def drawFruit2(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXFruit2,data.imageYFruit2,image = data.fruit2Image)
    

def drawFruit3(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXFruit3,data.imageYFruit3,image = data.fruit3Image)
    

def drawFruit4(canvas,data,row,col):
    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_image(data.imageXFruit4,data.imageYFruit4,image = data.fruit4Image)
    
    
    
def movePacmanGif(data):
    data.pacmanGifX -= 30
    if data.pacmanGifX + (data.pacmanGif.width()//2) <= 0:
        data.pacmanGifX %= (data.width + 100)


def drawBlackBox(canvas,data,row,col):

    leftMost = col*data.cellSize+data.margin 
    topMost = row*data.cellSize +data.margin
    canvas.create_rectangle(leftMost,topMost,leftMost + data.cellSize,
                    topMost + data.cellSize,fill="black") 



###Citations: Taken from my code from Tetris assignment (Hw 6) and modified                    
def playPacman():
    width = (2*25) + (19*20) 
    height = (2*25) + (21*20) + 50
    run(width,height)
    
    
    
def timerFired(data):
    if data.mode == "startGame":
        movePacmanGif(data)
        
    
    if data.mode == "playGameNew":
        data.ghostCounter +=1 
        data.timerDelay = 200
        
        data.randomTimer +=1 
        data.timeLeft -= 1
        pacman1NewGhostInteract(data)
        pacman2NewGhostInteract(data)
        pacman3NewGhostInteract(data)
        allPacmanGhostInteract(data)
       
        pacmansCoinInteract(data)
        totalCoinCount2(data)
        pacmanRandom(data)
        pacman2Random(data)
        pacman3Random(data)
        timeRemaining(data)
        if data.Ghost1Up == True:
    
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
        
            
            if data.newGrid[Ghost1Row-1][Ghost1Col]!=1:
        
                data.imageYGhost1 -= data.cellSize
                
        if data.Ghost1Left == True:
    
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
           
            
            if data.newGrid[Ghost1Row][Ghost1Col-1]!=1:
    
                data.imageXGhost1 -=data.cellSize
                
            
        if data.Ghost1Right == True:
    
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
           
    
            if data.newGrid[Ghost1Row][Ghost1Col+1]!=1:
    
                data.imageXGhost1 += data.cellSize
        
        if data.Ghost1Down == True:
    
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    
            if data.newGrid[Ghost1Row+1][Ghost1Col]!=1:
    
                data.imageYGhost1 +=data.cellSize
               
    
    
    if data.mode == "playGameSingle":
        
        row = int((data.imageYPac-data.margin)//data.cellSize)
        col = int((data.imageXPac-data.margin)//data.cellSize)
        
        
        pacmanCoinInteract(data)
        totalCoinCount(data)
        pacmanGhostInteract(data)
        pacmanFruit1Interact(data)
        pacmanFruit2Interact(data)
        pacmanFruit3Interact(data)
        pacmanFruit4Interact(data)
        if data.scatter == True:
            
            ghost1ScatterSingle(data)
            ghost2ScatterSingle(data)
            ghost3Scatter(data)
            ghost4Scatter(data)
           
            data.scatterCount -=1
            if data.scatterCount == 0:
                data.scatter = False
                data.pacmanImage = PhotoImage(file = "canva-photo-editor-6.gif")
                data.scatterCount = 50
                print(data.scatter)
        else:
            ghost1HelperSingle(data)
            ghost2Helper(data)
            ghost3HelperSingle(data)
            ghost4Helper(data)
            
            
        if data.pacmanUp == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
           
            
            if data.grid[row-1][col]!=1:
                
                data.imageYPac -= data.cellSize
                
        if data.pacmanLeft == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
            
            if data.grid[row][col-1]!=1:
                
    
                data.imageXPac -=data.cellSize
            
        if data.pacmanRight == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
           
    
            if data.grid[row][col+1]!=1:
                
    
                data.imageXPac += data.cellSize
                
        
        if data.pacmanDown == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
    
            if data.grid[row+1][col]!=1:
                
    
                data.imageYPac +=data.cellSize
               
                
        
    
    
    
    if data.mode == "playGame":
        data.timerCalls +=1
        
        row = int((data.imageYPac-data.margin)//data.cellSize)
        col = int((data.imageXPac-data.margin)//data.cellSize)
        row2 = int((data.imageYPac2-data.margin)//data.cellSize)
        col2 = int((data.imageXPac2-data.margin)//data.cellSize)
        
        
        pacmanGhostInteract(data)
        pacman2GhostInteract(data)
        pacmansCoinInteract(data)
        totalCoinCount2(data)
        pacmanFruit1Interact(data)
        pacmanFruit2Interact(data)
        pacmanFruit3Interact(data)
        pacmanFruit4Interact(data)
        pacman2Fruit1Interact(data)
        pacman2Fruit2Interact(data)
        pacman2Fruit3Interact(data)
        pacman2Fruit4Interact(data)
        pacmanpacman2Interact(data)
        if data.scatter == True:
            
            ghost1Scatter(data)
            ghost2Scatter(data)
            ghost3Scatter(data)
            ghost4Scatter(data)


            data.scatterCount -=1
            if data.scatterCount == 0:
                data.scatter = False
                data.pacmanImage = PhotoImage(file = "canva-photo-editor-6.gif")
                data.pacman2Image = PhotoImage(file = "canva-photo-editor-17.gif")
                data.scatterCount = 50
                print(data.scatter)
        else:
            ghost1Helper(data)
            ghost2Helper(data)
            ghost3Helper(data)
            ghost4Helper(data)
            
       
        if data.pacmanUp == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
           
            
            if data.grid[row-1][col]!=1:
        
                data.imageYPac -= data.cellSize
                
        if data.pacmanLeft == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
            
            
            if data.grid[row][col-1]!=1:
    
                data.imageXPac -=data.cellSize
               
            
        if data.pacmanRight == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
          
    
            if data.grid[row][col+1]!=1:
    
                data.imageXPac += data.cellSize
                
        if data.pacmanDown == True:
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
    
            if data.grid[row+1][col]!=1:
    
                data.imageYPac +=data.cellSize
                
                
                
        if data.pacman2Up == True:
    
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
           
            
            if data.grid[row2-1][col2]!=1:
        
                data.imageYPac2 -= data.cellSize
                
        if data.pacman2Left == True:
    
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
            
            
            if data.grid[row2][col2-1]!=1:
    
                data.imageXPac2 -=data.cellSize
               
            
        if data.pacman2Right == True:
    
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
           
    
            if data.grid[row2][col2+1]!=1:
    
                data.imageXPac2 += data.cellSize
              
        
        if data.pacman2Down == True:
    
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
    
            if data.grid[row2+1][col2]!=1:
    
                data.imageYPac2 +=data.cellSize
              
            
            
def startGamekeyPressed(event,data):
    pass
        


def keyPressed(event,data):
    if data.mode == "startGame":
        startGamekeyPressed(event,data)
        
    if data.mode == "highScores":
        if event.keysym == "b":
            data.mode = "startGame"
        
    
    elif data.mode == "playGameNew":
        if event.keysym == "Up":
    
            data.Ghost1Down = False
            data.Ghost1Left = False
            data.Ghost1Right = False
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
        
            if data.newGrid[Ghost1Row-1][Ghost1Col]!=1:
    
                data.Ghost1Up = True
    
        if event.keysym == "Down":
    
            data.Ghost1Up = False
            data.Ghost1Left = False
            data.Ghost1Right = False
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
            
            if data.newGrid[Ghost1Row+1][Ghost1Col]!=1:
    
                data.Ghost1Down = True 
    
        if event.keysym == "Left":
            data.Ghost1Up = False
            data.Ghost1Down = False
            data.Ghost1Right = False
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    
           
    
            if data.newGrid[Ghost1Row][Ghost1Col-1]!=1: 
    
                data.Ghost1Left = True
    
        if event.keysym == "Right":
            
            data.Ghost1Up = False
            data.Ghost1Left = False
            data.Ghost1Down = False
    
            Ghost1Row = int((data.imageYGhost1-data.margin)//data.cellSize)
            Ghost1Col = int((data.imageXGhost1-data.margin)//data.cellSize)
    
            if data.newGrid[Ghost1Row][Ghost1Col+1]!=1:
                data.Ghost1Right = True
    elif data.mode == "playGame":
        if event.keysym == "Up":
    
            data.pacmanDown = False
            data.pacmanLeft = False
            data.pacmanRight = False
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
        
            if data.grid[row-1][col]!=1:
    
                data.pacmanUp = True
    
        if event.keysym == "Down":
    
            data.pacmanUp = False
            data.pacmanLeft = False
            data.pacmanRight = False
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
            
            if data.grid[row+1][col]!=1:
    
                data.pacmanDown = True 
    
        if event.keysym == "Left":
            data.pacmanUp = False
            data.pacmanDown = False
            data.pacmanRight = False
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
    
            if data.grid[row][col-1]!=1: 
    
                data.pacmanLeft = True
    
        if event.keysym == "Right":
            
            data.pacmanUp = False
            data.pacmanLeft = False
            data.pacmanDown = False
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
    
            if data.grid[row][col+1]!=1:
                data.pacmanRight = True
                
                
                
        if event.char == "w":
    
            data.pacman2Down = False
            data.pacman2Left = False
            data.pacman2Right = False
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
        
            if data.grid[row2-1][col2]!=1:
    
                data.pacman2Up = True
    
        if event.char == "s":
    
            data.pacman2Up = False
            data.pacman2Left = False
            data.pacman2Right = False
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
            
            if data.grid[row2+1][col2]!=1:
    
                data.pacman2Down = True 
    
        if event.char == "a":
            data.pacman2Up = False
            data.pacman2Down = False
            data.pacman2Right = False
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
    
            if data.grid[row2][col2-1]!=1: 
    
                data.pacman2Left = True
    
        if event.char == "d":
            
            data.pacman2Up = False
            data.pacman2Left = False
            data.pacman2Down = False
    
            row2 = int((data.imageYPac2-data.margin)//data.cellSize)
            col2 = int((data.imageXPac2-data.margin)//data.cellSize)
    
            if data.grid[row2][col2+1]!=1:
                data.pacman2Right = True
                
    elif data.mode == "playGameSingle":
        if event.keysym == "Up":
    
            data.pacmanDown = False
            data.pacmanLeft = False
            data.pacmanRight = False
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
        
            if data.grid[row-1][col]!=1:
    
                data.pacmanUp = True
    
        if event.keysym == "Down":
    
            data.pacmanUp = False
            data.pacmanLeft = False
            data.pacmanRight = False
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
            
            if data.grid[row+1][col]!=1:
    
                data.pacmanDown = True 
    
        if event.keysym == "Left":
            data.pacmanUp = False
            data.pacmanDown = False
            data.pacmanRight = False
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)

    
            if data.grid[row][col-1]!=1: 
    
                data.pacmanLeft = True
    
        if event.keysym == "Right":
            
            data.pacmanUp = False
            data.pacmanLeft = False
            data.pacmanDown = False
    
            row = int((data.imageYPac-data.margin)//data.cellSize)
            col = int((data.imageXPac-data.margin)//data.cellSize)
    
            if data.grid[row][col+1]!=1:
                data.pacmanRight = True
                
        

def mousePressed(event,data): 
    if data.mode == "startGame":
        if (data.width - 105 <= event.x and event.x <= data.width - 5) and (5<= event.y and event.y <= 100):
            data.mode = "playGame"
        elif (5 <= event.x and event.x <= 100) and (5<= event.y and event.y <= 100):
            data.mode = "playGameSingle"
        elif (data.width - 105 <= event.x and event.x <= data.width - 5) and (data.height - 105<= event.y and event.y <= data.height - 5):
            data.mode = "highScores"
        elif (5 <= event.x and event.x <= 100) and (data.height - 105<= event.y and event.y <= data.height - 5):
            data.mode = "playGameNew"
    
    
def startGameredrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_image(data.pacmanGifX,data.pacmanGifY,image = data.pacmanGif)
    canvas.create_image(data.width/2,data.height/2 - 100,image = data.pacmanTitle)
    canvas.create_rectangle(5,5,100,100,outline = "red")
    canvas.create_text(52,50,text = "SinglePlayer",fill = "white")
    canvas.create_rectangle(data.width - 105,data.height - 105,data.width - 5,data.height-5,outline = "red")
    canvas.create_text(data.width - 52, data.height - 50, text = "High Scores",fill = "white")
    canvas.create_rectangle(5,data.height - 105,100,data.height-5,outline = "red")
    canvas.create_text(52,data.height - 50,text = "Ghost Mode",fill = "white")
    canvas.create_rectangle(data.width - 105,5,data.width - 5,100,outline = "red")
    canvas.create_text(data.width - 52,53,text = "Multiplayer",fill = "white")

def winGameredrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_text(data.width/2,data.height/2, text = "Player1  Wins!", fill = "red",font = "consoleas 60")
    
def winGame2redrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_text(data.width/2,data.height/2, text = "Player2  Wins!", fill = "red",font = "consoleas 60")
    
    
def winGameSingleredrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_image(data.width/2,data.height/2, image = data.youWinTitle)
    
    
def youLoseredrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_image(data.width/2,data.height/2, image = data.youLoseTitle)
    
def gotemredrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_text(data.width/2,data.height/2, text = "Got Em!", fill = "red", font = "consoleas 60")
    
def highScoresredrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    canvas.create_image(data.width/2,50,image = data.highScoreTitle)
    s= ""
    for i in range(5):
        HS = data.listOfHighScores[i]
        
        s = str(5 - i) +  ".        " + str(HS) + "\n" + s
        
    canvas.create_text((data.width/2,data.height/2), text = s,fill = "white", font = "Times 28 bold")
    
    
def redrawAll(canvas,data):
    if data.mode == "startGame":
        startGameredrawAll(canvas,data)
    elif data.mode == "highScores":
        highScoresredrawAll(canvas,data)
    elif data.mode == "gotem":
        gotemredrawAll(canvas,data)
    elif data.mode == "youLose":
        youLoseredrawAll(canvas,data)
    elif data.mode == "playGame":
        canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
        canvas.create_text(data.width/2,495,text = "Score: %d" % (data.coinCount), fill = "red")
        canvas.create_text(data.width/2 - 100,495, text = "Score2 %d" % (data.coinCount2), fill = "red")
        drawBoard2(canvas,data)
    elif data.mode == "winGameSingle":
        winGameSingleredrawAll(canvas,data)
    elif data.mode == "playGameSingle":
        canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
        canvas.create_text(data.width/2,465,text = "You Have %d lives left" % (data.counterLives),fill = "white")
        canvas.create_text(data.width/2,495,text = "Score: %d" % (data.coinCount), fill = "red")
        drawBoard1(canvas,data)
       
    elif data.mode == "playGameNew":
        canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
        canvas.create_text(data.width/2,495,text = "Time Remaining: %d" % (data.timeLeft), fill = "red")
        
        drawBoard3(canvas,data)
        
    elif data.mode == "endGame":
        canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
        canvas.create_image(data.width/2,data.height/2, image = data.gameOverTitle)
    elif data.mode == "winGame":
        winGameredrawAll(canvas,data)
    elif data.mode == "winGame2":
        winGame2redrawAll(canvas,data)

   
    
####################################
# use the run function as-is
####################################


###Citations: Taken from course Notes https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def run(width, height): 
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        #pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 250 # milliseconds ##### 
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()

    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)

    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
    
playPacman()