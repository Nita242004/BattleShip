import math, copy, random

from cmu_112_graphics import *
import random  


# ship class and different ship types
class ship():
    def __init__(self, app, shipCoord, outline, shipType):
        self.shipCoord = shipCoord #actual coords of the ship
        self.outline = outline #outline which other ships cant enter
        self.app = app
        self.shipType = shipType

    def getCoordinates(self):
        return self.shipCoord
    
    def getShipType(self):
        return self.shipType

    def moveShip(self, drow, dcol):
        oldCoord = copy.deepcopy(self.shipCoord)
        oldOutline = copy.deepcopy(self.outline)
        
        # creates temp ship to test
        newCoord = []
        for coord in self.shipCoord:
            row, col = coord

            newRow = row + drow
            newCol = col + dcol

            newCoord.append((newRow, newCol))
            
        removeOldOutline(self.app, oldOutline)
        removeOldCoords(self.app, oldCoord)
        addOtherOutlines(self.app)

        newOutline = getOutline(self.app, newCoord)
        if newOutline == False:
            print("outline false")
            self.shipCoord = oldCoord
            self.outline = oldOutline
        else:
            # tests if new coords are legal
            if isShipLegal(self.app, newCoord, newOutline) == False:
                print("ship not legal = didnt move")
                self.shipCoord = oldCoord
                self.outline = oldOutline
                addOutline(self.app, oldOutline)
            elif isShipLegal(self.app, newCoord, newOutline):
                print("moved")
                removeOldCoords(self.app, oldCoord)
                removeOldOutline(self.app, oldOutline)
                addOutline(self.app, newOutline)
                addCoords(self.app, newCoord, self.shipType)
                self.shipCoord = newCoord
                self.outline = newOutline
        
        print(f"moveship coords{self.shipCoord}")
        print(f"updated board = {self.app.turn.boardShips}")
    
    def draw(self):
        pass


# FIX ROTATED
    def rotate(self, app):
        oldCoord = copy.deepcopy(self.shipCoord)
        oldRowLenCoord = len(self.shipCoord)
        oldColLenCoord = len(self.shipCoord[0])

        oldOutline = copy.deepcopy(self.outline)
        oldRowLenOutline= len(self.outline)
        oldColLenOutline= len(self.outline[0])

        newRowLenCoord = oldColLenCoord
        newColLenCoord = oldRowLenCoord

        newRowLenOutline = oldColLenOutline
        newColLenOutline = oldRowLenOutline

        rotatedShip = []
        for i in range(oldColLenCoord):
            tempRow = []
            for j in range(oldRowLenCoord):
                tempRow.append(None)
            rotatedShip.append(tempRow)

        for i in range(0, oldRowLenCoord):
            for j in range(oldColLenCoord-1, -1, -1):
                temp = oldCoord[i][j]
                rotatedShip[oldColLenCoord-j-1][i] = temp

        self.shipCoord = copy.deepcopy(rotatedShip)

        # # centering
        # newRow = app.fallingPieceRow + oldRowLen//2 - newRowLen//2
        # newCol = app.fallingPieceCol + oldColLen//2 - newColLen//2

        # app.fallingPieceRow = newRow
        # app.fallingPieceCol = newCol

        # if fallingPieceIsLegal(app) == False:
        #     app.fallingPiece = oldPiece
        #     app.fallingPieceRow = oldRow
        #     app.fallingPieceCol = oldCol
# ==============

        # oldPiece = copy.deepcopy(app.fallingPiece)
        # oldRowLen = len(app.fallingPiece)
        # oldColLen = len(app.fallingPiece[0])

        # newRowLen = oldColLen
        # newColLen = oldRowLen

        # oldRow = app.fallingPieceRow
        # oldCol = app.fallingPieceCol

        # rotatedPiece = []
        # for i in range(oldColLen):
        #     tempRow = []
        #     for j in range(oldRowLen):
        #         tempRow.append(None)
        #     rotatedPiece.append(tempRow)

        # for i in range(0, oldRowLen):
        #     for j in range(oldColLen-1, -1, -1):
        #         temp = oldPiece[i][j]
        #         rotatedPiece[oldColLen-j-1][i] = temp

        # app.fallingPiece = copy.deepcopy(rotatedPiece)
        
        # # centering
        # newRow = app.fallingPieceRow + oldRowLen//2 - newRowLen//2
        # newCol = app.fallingPieceCol + oldColLen//2 - newColLen//2

        # app.fallingPieceRow = newRow
        # app.fallingPieceCol = newCol

        # if fallingPieceIsLegal(app) == False:
        #     app.fallingPiece = oldPiece
        #     app.fallingPieceRow = oldRow
        #     app.fallingPieceCol = oldCol

def removeOldOutline(app, outline):
    for coord in outline:
        rowCoord, colCoord = coord
        app.turn.boardShips[rowCoord][colCoord] = -1

def addOutline(app, outline):
    for coord in outline:
        rowCoord, colCoord = coord
        app.turn.boardShips[rowCoord][colCoord] = 0

def removeOldCoords(app, oldCoord):
    for coord in oldCoord:
        rowCoord, colCoord = coord
        app.turn.boardShips[rowCoord][colCoord] = -1

def addCoords(app, coords, shipType):
    for coord in coords:
        rowCoord, colCoord = coord
        app.turn.boardShips[rowCoord][colCoord] = shipType
    
def addOtherOutlines(app):
    for ship in app.turn.ships:
        if ship == app.selectedShip:
            continue
        else:
            coords = ship.getCoordinates()
            outline = getOutline(app, coords)
            addOutline(app, outline)

    # if app.player == 0:
    #     for ship in app.ships1:
    #         if ship == app.selectedShip:
    #             continue
    #         else:
    #             coords = ship.getCoordinates()
    #             outline = getOutline(app, coords)
    #             addOutline(app, outline)
    # elif app.player == 1:
    #     for ship in app.ships2:
    #         if ship == app.selectedShip:
    #             continue
    #         else:
    #             coords = ship.getCoordinates()
    #             outline = getOutline(app, coords)
    #             addOutline(app, outline)




# have drawing function for ship class --> ship.draw
# home grown algorithm
# monte carlo: most likey to put where --> learn to put in certain places
# 1. be able to play with two players
# 2. set up AI class (rand) 
# 3. 3rd AI should do something smarter --> find patterns in what people play
# look at expecamax (likely to do this, so i chose something to do that will make me max my score)
# level/board generation --> make backtracker to make a board that can fit the different ships

# draw directly on screen --> draw what your trying to print in canvas
# have two board for two players --> screen switches when player switches (call board1, or board2 --> depends on player)
# model view controler so don need more than 2 boards

class smallShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): #shipcoord and outline will be sent from create ships
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()    

class medShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): 
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()

class bigShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): 
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()

class lShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): 
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()
    
class oShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): 
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()

class uShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): 
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()

class tShip(ship):
    def __init__(self, app, shipCoord, outline, shipType): 
        super().__init__(app, shipCoord, outline, shipType)
        super().getCoordinates()
        super().draw()
        super().getShipType()


# model and view functions
# -----------------------------------------------------------------------------------------------

        
# canvas.create_rectangle(col*app.cellSize + app.margin, 
#                         row*app.cellSize + app.margin*(5/2),
#                         (col + 1)*app.cellSize + app.margin, 
#                         (row + 1)*app.cellSize + app.margin*(5/2), 
#                         fill = color, 
#                         width = 2)
        
def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.cols*app.cellSize+app.margin) and
            (app.margin*(5/2) <= y <= app.rows*app.cellSize+app.margin*(5/2)))

def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        print("not in grid")
        return (-1, -1)
    print("ingrid")
    gridWidth  = app.cols*app.cellSize
    gridHeight = app.rows*app.cellSize
    cellWidth  = app.cellSize
    cellHeight = app.cellSize

    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin*(5/2)) // cellHeight)
    col = int((x - app.margin) // cellWidth)

    return (row, col)

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.cols*app.cellSize
    gridHeight = app.rows*app.cellSize
    cellWidth  = app.cellSize
    cellHeight = app.cellSize
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin*(5/2) + row * cellHeight
    y1 = app.margin*(5/2) + (row+1) * cellHeight
    return (x0, y0, x1, y1)

def mousePressed(app, event):   # use event.x and event.y
    print("mousepressed")
    # select ship
    (row, col) = getCell(app, event.x, event.y)
    app.selection = (row, col)
    print(f"mousepressed row col = {row, col}")
    checkWhichShip(app)

    # finish setup button
    if (event.x >= app.margin*2 + app.cols*app.cellSize and 
        event.x <= app.margin*2 + app.cellSize*5 + app.cols*app.cellSize and
        event.y >= app.margin*(5/2) + app.rows*app.cellSize - 50 and
        event.y <= app.margin*(5/2) + app.rows*app.cellSize):
        print("finishSetup button")
        print(f"initial = {app.turn.id}")
        print(app.setup)
        if app.turn.id == 1 and app.setup == True:
            app.setup = True
            app.gameStarted = False
            app.turn = app.player2
            initialShips(app)
        elif app.turn.id == 2 and app.setup == True:
            app.setup = False
            app.gameStarted = True
            app.turn = app.player1
        print(f"final = {app.turn.id}")
        

def checkWhichShip(app):
    # playerShips = None
    playerShips = app.turn.ships
    for ship in playerShips:
        print("newSHIP")
        coords = ship.getCoordinates()
        print(f"ship coords{coords}, slected = {app.selection}")
        if app.selection in coords:
            app.selectedShip = ship
            break
    return None

def keyPressed(app, event):
    print("keypressed")

    if app.setup == True:
        ship = app.selectedShip
        print(f"key pressed ship = {ship}")
        if ship != None:
            if event.key == "Up":
                ship.moveShip(-1, 0)
            if event.key == "Down":
                ship.moveShip(1, 0)
            if event.key == "Left":
                ship.moveShip(0, -1)
            if event.key == "Right":
                ship.moveShip(0, 1)

            if event.key == "Space":
                ship.rotate(app)

# checks selected box for which ship, returns the ship from app.ship in the selected location
    

#gui and graphics
# -----------------------------------------------------------------------------------------------

def gameDimensions():
    margin = 40
    # users can change this (make adjustable)
    rows = 20
    cols = 20
    cellSize = 35
    return (rows, cols, cellSize, margin) 

def appStarted(app):            # initialize the model (app.xyz)
    app.setup = True
    app.gameStarted = False
    (app.rows, app.cols, app.cellSize, app.margin) = gameDimensions()
    
    app.boardWidth = app.cols+app.cellSize

    app.emptyColor = "light blue"
    app.selection = (-1, -1)
    
    bigShip = [
        [  True,  True,  True,  True ]
    ]
    medShip = [
        [  True,  True,  True]
    ]
    smallShip = [
        [  True,  True ]
    ]
    lShip = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]
    oShip = [
        [  True,  True ],
        [  True,  True ]
    ]
    uShip = [
        [  True,  False,  True ],
        [  True,  True,   True ]
    ]
    tShip = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    app.shipTypes = {1:bigShip, 2:medShip, 3:smallShip, 4:lShip, 5:oShip, 6:uShip, 7:tShip}
    app.shipNames = ["Big Ship", "Medium Ship", "Small Ship", "L Ship", "O Ship", "U Ship", "T Ship"]
    app.selectedShip = None

    #user can change this (make adjustable)  
    app.allShips = {1:1, 2:2, 3:3, 4:1, 5:2, 6:2, 7:1}

    app.player1 = player(app, 1, app.rows, app.cols, app.emptyColor, app.allShips)
    app.player2 = player(app, 2, app.rows, app.cols, app.emptyColor, app.allShips)
    app.turn = app.player1
    
    initialShips(app)

def initialShips(app):
    if app.setup == True and app.turn.id == 1:
        for key in app.allShips:
            createShips(app, app.allShips[key], key, app.player1.ships)
    elif app.setup == True and app.turn.id == 2:
        for key in app.allShips:
            createShips(app, app.allShips[key], key, app.player2.ships)

class player():
    def __init__(self, app, id, boardRows, boardCols, emptyColor, allShips):
        self.app = app
        self.rows = boardRows
        self.cols = boardCols
        self.id = id

        self.board = []
        for i in range(self.rows):
            newRow = []
            for j in range(self.cols):
                newRow.append(emptyColor)
            self.board.append(newRow)

        self.boardShips = []
        for i in range(self.rows):
            newRow = []
            for j in range(self.cols):
                newRow.append(-1)
            self.boardShips.append(newRow)

        # the places you chose to hit
        self.boardHits = []
        for i in range(self.rows):
            newRow = []
            for j in range(self.cols):
                newRow.append(False)
            self.boardHits.append(newRow)

        self.allShips = allShips
        self.ships = []
    
    def id(self):
        return self.id
    def board(self):
        return self.board
    def boardShips(self):
        return self.boardShips
    def boardHits(self):
        return self.boardHits
    def ships(self):
        return self.ships

def createShips(app, numberOfShips, shipType, playerShip):
    type = app.shipTypes[shipType]
    row = len(type)
    col = len(type[0])

    names = []

    count = 0
    while True:
        while True:
            randRow = random.randint(0, app.rows-1)
            randCol = random.randint(0, app.cols-1)

            # creates Coords of current ship (rand on board)
            shipCoord = []
            for i in range(0, row):
                for j in range(0, col):
                    if type[i][j] == True:
                        shipCoord.append((randRow + i,randCol + j))
            
            # gets outline of ship
            outline = getOutline(app, shipCoord)
            if outline == False:
                break
            
            # checks if coords of point are legal, if legal add to app.ships
            if isShipLegal(app, shipCoord, outline) == True:
                if shipType == 1:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = bigShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)

                if shipType == 2:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = medShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)
                
                if shipType == 3:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = smallShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)

                if shipType == 4:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = lShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)

                if shipType == 5:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = oShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)

                if shipType == 6:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = uShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)

                if shipType == 7:
                    names.append(str(int(shipType)*10 + count))
                    names[0] = tShip(app, shipCoord, outline, shipType)
                    playerShip.append(names[0])

                    addCoords(app, shipCoord, shipType)
                    addOutline(app, outline)
                
                count += 1
                break
            else:
                break
        if count >= numberOfShips:
            break

# gets outline coords of ship
def getOutline(app, shipCoord):
    print(f"get outline ship coord = {shipCoord}")
    directions = [(-1, -1), (0, -1), (1, -1), 
                    (-1, 0), (1, 0), 
                    (-1, 1), (0, 1), (1, 1)]

    outline = []
    for coord in shipCoord:
        row, col = coord
        for d in directions:
            rowD, colD = d
            newRow = row + rowD
            newCol = col + colD

            # checks if legal, if not, returns false
            if newRow > app.rows or newCol > app.cols:
                return False
            # checks if out of boarder by one, should still be ok since only ship cant exceed, thus wont append
            elif (newRow == app.rows or newCol == app.cols 
                    or (newRow, newCol) in shipCoord
                    or newRow == -1 or newCol == -1 ):
                continue
            # satisfy all constraints, appends coord of outline
            elif app.turn.id == 1:
                if app.player1.boardShips[newRow][newCol] < 0 and (newRow, newCol) not in outline:
                    outline.append((newRow, newCol)) 
            elif app.turn.id == 2:
                if app.player2.boardShips[newRow][newCol] < 0 and (newRow, newCol) not in outline:
                    outline.append((newRow, newCol)) 
    return outline

# draws all ships
def drawShips(app, canvas):
    if app.setup == True:

        for ship in app.turn.ships:
                coords = ship.getCoordinates()
                for coord in coords:
                    row, col = coord
                    drawCell1(app, canvas, row, col, "grey")
        
        for row in range(len(app.turn.boardShips)):
            for col in range(len(app.turn.boardShips[0])):
                if app.turn.boardShips[row][col] == 0:
                    drawCell1(app, canvas, row, col, "red")
                
    
    elif app.gameStarted == True:
        for ship in app.turn.ships:
            coords = ship.getCoordinates()
            for coord in coords:
                row, col = coord
                drawCell1(app, canvas, row, col, "grey")

# checks if entire ship is legal      
def isShipLegal(app, shipCoord, outline):
    # checks if ship coords are legal
    for coordS in shipCoord:
        print("ship false")
        rowS, colS = coordS
        if rowS < 0:
            print("f1")
            return False
        if colS < 0:
            print("f2")
            return False
        if rowS >= app.rows:
            print("f3")
            return False
        if colS >= app.cols:
            print("f4")
            return False
        if app.turn.boardShips[rowS][colS] >= 0:
            print("f5")
            return False

    # checks if outline coords are legal
    for coordO in outline:
        print("outline False")
        rowO, colO = coordO
        if rowO < -1:
            return False
        if colO < -1:
            return False
        if rowO > app.rows:
            return False
        if colO > app.cols:
            return False
        if app.turn.boardShips[rowS][colS] > 0:
            print("f5")
            return False

    return True

#all general draws
# -----------------------------------------------------------------------------------------------

# draws board
def drawBoard1(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell1(app, canvas, row, col, app.turn.board[row][col])
                
def drawBoard2(app, canvas): 
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell2(app, canvas, row, col, app.turn.board[row][col])
    
# draws cell
def drawCell1(app, canvas, row, col, color):
    if app.setup == True:
        # canvas.create_rectangle(col*app.cellSize + app.width/2 - app.cellSize, 
        #                         row*app.cellSize + app.margin*(5/2),
        #                         (col + 1)*app.cellSize + app.width/2 + 35*app.cols/2, 
        #                         (row + 1)*app.cellSize + app.margin*(5/2), 
        #                         fill = color, 
        #                         width = 2)
        canvas.create_rectangle(col*app.cellSize + app.margin, 
                                row*app.cellSize + app.margin*(5/2),
                                (col + 1)*app.cellSize + app.margin, 
                                (row + 1)*app.cellSize + app.margin*(5/2), 
                                fill = color, 
                                width = 2)
    elif app.gameStarted == True:
        canvas.create_rectangle(col*app.cellSize + app.margin, 
                                row*app.cellSize + app.margin*(5/2), 
                                (col + 1)*app.cellSize + app.margin, 
                                (row + 1)*app.cellSize + app.margin*(5/2), 
                                fill = color, 
                                width = 2)

        
def drawCell2(app, canvas, row, col, color):
    canvas.create_rectangle(col*app.cellSize + app.margin*2 + app.cols*app.cellSize, 
                            row*app.cellSize + app.margin*(5/2), 
                            (col + 1)*app.cellSize + app.margin*2 + app.cols*app.cellSize, 
                            (row + 1)*app.cellSize + app.margin*(5/2), 
                            fill = color, 
                            width = 2)
# everything in setup
# -----------------------------------------------------------------------------------------------

# draws side bar of setup (shud put in app.setup)
def sideBar(app, canvas):
    #create buttons for all Ships (say how many Ships there are)
    #when press button, will generate ship on board, 
        #then can move ship with arrow keys or drag idk
    
    canvas.create_text(app.margin*2 + app.cols*app.cellSize + app.cellSize*5/2,
                        app.margin*2 + app.margin*(1/2) + 50/2,
                        text = "Your Ships!",
                        font = "arial 25 bold",
                        fill = "black")
    
    canvas.create_rectangle(app.margin*2 + app.cols*app.cellSize, 
                            app.margin*2 + app.margin*(1/2) + 60,
                            app.margin*2 + app.cellSize*5 + app.cols*app.cellSize,
                            app.margin*2 + app.margin*(1/2) + (app.cellSize+30)*len(app.shipNames),
                            fill = "light gray")
    
    for i in range(len(app.shipNames)):
        canvas.create_text(app.margin*2 + app.cols*app.cellSize + app.cellSize*5/2,
                            (app.margin + 50/3)*(i+1) + 60 + app.margin*(3/2),
                            text = (f"{app.shipNames[i]} = {app.allShips[i+1]}"), 
                            font = "arial 15",
                            fill = "black")
    
    # button height = 50
    canvas.create_rectangle(app.margin*2 + app.cols*app.cellSize, 
                            app.margin*2 + app.margin*(1/2) + app.rows*app.cellSize - 50,
                            app.margin*2 + app.cellSize*5 + app.cols*app.cellSize,
                            app.margin*2 + app.margin*(1/2) + app.rows*app.cellSize,
                            fill = "light green",
                            outline = "black",
                            width = 2) 
                            
    canvas.create_text(app.margin*2 + app.cols*app.cellSize + app.cellSize*5/2,
                            app.margin*(5/2) + app.rows*app.cellSize - 25,
                            text = "Start Game", 
                            font = "arial 18 bold",
                            fill = "black")

def generalTitles(app, canvas):
    canvas.create_text(app.width/2, 
                        app.margin*(5/4), 
                        text = f"Player {app.turn.id}'s Turn",
                        font = "arial 30 bold", 
                        fill = "black")
    
# -----------------------------------------------------------------------------------------------
def redrawAll(app, canvas):
    if app.setup == True:
        generalTitles(app, canvas)
        drawBoard1(app,canvas)
        sideBar(app, canvas)
        drawShips(app, canvas)
    elif app.gameStarted == True:
        generalTitles(app, canvas)
        drawBoard1(app,canvas)
        drawBoard2(app, canvas)
        drawShips(app, canvas)


def playBattleship():
    rows, cols, cellSize, margin = gameDimensions()
    
    width = (cols*cellSize)*2 + margin*3
    height = (rows*cellSize) + margin*4
    runApp(width=width, height=height)

def main():
    playBattleship()

if __name__ == '__main__':
    main()


# def appStopped(app): 

# def keyPressed(app, event):     # use event.key

# def keyReleased(app, event):



# def mousePressed(app, event):   # use event.x and event.y

# def mouseReleased(app, event): 


# def mouseMoved(app, event):     # use event.x and event.y

# def mouseDragged(app, event):