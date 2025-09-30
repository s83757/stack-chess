import pygame
import copy

tileSize = 100

class Piece:
    def __init__(self, color, species, value, image, nickname, killable=False):
        '''__init__ is always run when created.
Self does not have to be named self in particular, but the specific parameter must be
the first parameter in every function in the class'''
        self.color = color
        self.species = species
        self.value = value
        self.image = image
        self.nickname = nickname
        self.killable = killable
class Label:
    def __init__(self, posx, posy, width, height, color, image, visible):
        self.posx = posx
        self.posy = posy
        self.coordRect = pygame.Rect(posx, posy, width, height)
        self.color = color
        self.image = image
        self.visible = visible
class Button:
    def __init__(self, x, y, width, height, color, active, visible, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.coordRect = pygame.Rect(x, y, width, height)
        self.color = color
        self.active = active
        self.visible = visible
        self.text = text
    def onClick(self):
        pass
    def func():
        return 0
def replaceTile(stack, x, y):
    removed = board[x][y][:]
    board[x][y] = stack
    return removed
def addToStack(stack, targetX, targetY):
    #print(targetX, targetY, "000000")
    target = board[targetX][targetY] # make sure I am not modifying a value stored in target.
    captured = None
    if target == []: #move to empty tile
        captured = replaceTile(stack, targetX, targetY)
    elif target[0].color == stack[0].color:
        board[targetX][targetY] += stack
    else: #target is of opposite color
        captured = replaceTile(stack, targetX, targetY)
    return captured
def moveStack(startX, startY, endX, endY):
    stack = replaceTile([], startX, startY) #stack = what is at start tile
    print(board[startX][startY])
    #target = board[endX][endY]
    captured = addToStack(stack, endX, endY)
    return captured
def dismantleStack(piece, startX, startY, endX, endY):
    stack = board[startX][startY]
    if not (piece in stack):
        print("error")
        return "error"
    stack.remove(piece)
    addToStack([piece], endX, endY)
    #captured = stack
    
wp = Piece("white", "pawn", 1, "image", "wp")
bp = Piece("black", "pawn", 1, "image", "bp")
wn = Piece("white", "knight", 3, "image", "wn")
bn = Piece("black", "knight", 3, "image", "bn")
wb = Piece("white", "bishop", 3, "image", "wb")
bb = Piece("black", "bishop", 3, "image", "bb")
wr = Piece("white", "rook", 5, "image", "wr")
br = Piece("black", "rook", 5, "image", "br")
wq = Piece("white", "queen", 9, "image", "wq")
bq = Piece("black", "queen", 9, "image", "bq")
wk = Piece("white", "king", 9, "image", "wk")
bk = Piece("black", "king", 9, "image", "bk")

blueLabel = Label(0, 0, tileSize, tileSize, pygame.Color("blue"), pygame.transform.scale(pygame.image.load("chessImages/" + "bluering" + ".png"), (100, 100)), False)
redLabel = Label(0, 0, tileSize, tileSize, pygame.Color("red"), pygame.transform.scale(pygame.image.load("chessImages/" + "redring" + ".png"), (100, 100)), False)

prompt = Button(900, 0, 200, 50, pygame.Color("white"), False, True, "select a piece")
actionButton1 = Button(1000, 100, 100, 50, pygame.Color("grey"), False, True, "whole stack")
actionButton2 = Button(1000, 300, 100, 50, pygame.Color("grey"), False, True, "one piece")
cancelButton = Button(1000, 700, 100, 50, pygame.Color("grey"), False, True, "cancel")

wkPos = [7, 4]
bkPos = [0, 4]

'''board = [
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""]
]
'''
'''X is vertical, Y is horizontal
Convert to dictionary?
now using row/col system'''
'''moves = {
    "+1-2": "knight",
    "+1+2": "knight",
    "-1+2": "knight",
    "-1-2": "knight",
    "+2+1": "knight",
    "+2-1": "knight",
    "-2+1": "knight",
    "-2-1": "knight",
}'''
#This searches for a corresponding piece based on the attempted move.
def checkValidMove(stack, startX, startY, endX, endY):
    '''dx and dy are in normal coordinates not like the board indices'''
    dx = startX - endX #this order because x decreases as it goes up
    dy = endY - startY
    checkPiece = []
    #note: ignore when dx and dy are both 0.
    if (dx == dy or dx == -dy):
        checkPiece = ["bishop", "queen"]
        if (abs(dx) <= 1 and abs(dy) <= 1):
            checkPiece += ["king"]
    elif (dx == 0 or dy == 0):
        checkPiece = ["rook", "queen"]
        #add pawn double move later.
        if (abs(dx) <= 1 and abs(dy) <= 1):
            checkPiece += ["king"]
        if (dx == 1):
            checkPiece += ["white pawn"]
        elif (dx == -1):
            checkPiece += ["black pawn"]
    elif ((abs(dx) == 1 and abs(dy) == 2) or (abs(dx) == 2 and abs(dy) == 1)):
        checkPiece = ["knight"]
    for piece in stack:
        print(piece.species, piece.color)
        if (piece.species in checkPiece):
            return True
        if piece.species == "pawn":
            if "white pawn" in checkPiece and piece.color == "white":
                print("true")
                return True
            if "black pawn" in checkPiece  and piece.color == "black":
                return True
    return False
        
IMAGES = {}
board = [
    [[br],[bn],[bb],[bq],[bk],[bb],[bn],[br]],
    [[bp],[bp],[bp],[bp],[bp],[bp],[bp],[bp]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[bp, wn, bb, wk, wp, wp],[],[]],
    [[wp],[wp],[wp],[wp],[wp],[wp],[wp],[wp]],
    [[wr],[wn],[wb],[wq],[wk],[wb],[wn],[wr]]
]
'''amogusBoard = [
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[],[],[]],
    [[],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[bp, bn, bb, bk, bq, br],[bp, bn, bb, bk, bq, br],[],[],[]],
    [[],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[],[],[]],
    [[],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[wp, wn, wb, wk, wq, wr],[],[],[]],
    [[],[],[wp, wn, wb, wk, wq, wr],[],[wp, wn, wb, wk, wq, wr],[],[],[]]
]'''
#bp, wn, bb, wk, wp, wp
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


selectedTile = () #check if same tile is pressed twice to deselect
playerClicks = [] #two tuples that keep track of what is pressed
status = "x"
subStatus = "x"

def loadImages():
    pieces = [wp, wr, wn, wb, wq, wk, bp, br, bn, bb, bq, bk]
    for piece in pieces:
        IMAGES[piece.nickname] = pygame.transform.scale(pygame.image.load("chessImages/" + piece.nickname + ".png"), (tileSize, tileSize))
        piece.image = pygame.transform.scale(pygame.image.load("chessImages/" + piece.nickname + ".png"), (tileSize, tileSize))
#note: size will have to be adjusted. Maybe do tileSize / 9.
def getMinSquare(n):
    i = 0
    while i**2 < n:
        i += 1
    return i

def drawBoard(window):
    colors = [pygame.Color("red"), pygame.Color("green")]
    for r in range(8):
        for c in range(8):
            color = colors[(r+c) %2]
            pygame.draw.rect(window, color, pygame.Rect(c*tileSize, r*tileSize, tileSize, tileSize))
def drawStacks(window):
    for r in range(8):
        for c in range(8):
            stack = board[r][c]
            if stack != []:
                amount = len(stack)
                squishSideLen = getMinSquare(amount)
                #print(squishSideLen)
                for a in range(squishSideLen):
                    for b in range(squishSideLen):
                        if a*squishSideLen + b < amount:
                            PosX = c*tileSize + b * tileSize/squishSideLen - tileSize / 2 + tileSize/(2*squishSideLen)
                            PosY = r*tileSize + a * tileSize/squishSideLen - tileSize / 2 + tileSize/(2*squishSideLen)
                            window.blit(stack[a*squishSideLen+b].image, pygame.Rect(PosX, PosY, tileSize, tileSize))
def drawLabels(window):
    if (blueLabel.visible):
        window.blit(blueLabel.image, pygame.Rect(blueLabel.posx*tileSize, blueLabel.posy*tileSize, tileSize, tileSize))
def drawButtons(window):
    pygame.draw.rect(window, prompt.color, prompt.coordRect)
    pygame.draw.rect(window, actionButton1.color, actionButton1.coordRect)
    pygame.draw.rect(window, actionButton2.color, actionButton2.coordRect)
    pygame.draw.rect(window, cancelButton.color, cancelButton.coordRect)

#actionbutton2
targetStack = []
pieceToMove = []

def listPieces(window, stack):
    #print("looping", stack[0].image)
    for i in range(len(stack)):
        window.blit(stack[i].image, pygame.Rect(1100, 100+100*i, tileSize, tileSize))

def drawGame(window, gameState):
    window.fill(pygame.Color("purple"))
    drawBoard(window)
    drawStacks(window)
    #window.blit(IMAGES["bn"], pygame.Rect(3*tileSize - tileSize/4, 3*tileSize + tileSize / 4, tileSize/2, tileSize/2))
    drawButtons(window)
    drawLabels(window)
    #listPieces(window, targetStack)
    if status == "actionButton2" and subStatus == "a2":
        listPieces(window, targetStack)
    pygame.display.flip() #must be last
def checkForCancel(loc):
    return loc[0] >= cancelButton.x\
    and loc[0] <= cancelButton.x + cancelButton.width\
    and loc[1] >= cancelButton.y\
    and loc[1] <= cancelButton.y + cancelButton.height
def cancel():
    actionButton1.color = pygame.Color("grey")
    actionButton2.color = pygame.Color("grey")
    cancelButton.color = pygame.Color("grey")
    blueLabel.visible = False
    redLabel.visible = False #store them in array?
    global status
    global subStatus
    global selectedTile
    global playerClicks
    global targetStack
    status = "x"
    subStatus = "x"
    selectedTile = ()
    playerClicks = []
    targetStack = []
def main():
    global status
    global subStatus
    global selectedTile
    global playerClicks
    global targetStack
    pygame.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("troll")
    screen.fill((100, 100, 100))
    loadImages()
    #pygame.time.delay(50) #stops cpu dying
    running = True
    while running:
        #screen.fill(pygame.Color("purple"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #selectedTile is not clearing
                #print(status, 5, selectedTile)
                location = pygame.mouse.get_pos()
                if selectedTile == () and status == "x":
                    if location[0] <= 8.5*tileSize:
                        col = location[0]//tileSize
                        row = location[1]//tileSize
                        selectedTile = (col, row)
                        if row > 7 or col > 7:
                            continue
                        print(row, col)
                        print(board[row][col])
                        if board[row][col] != []:
                            prompt.text = "select a button"
                            selectedTile = (row, col)
                            playerClicks.append(selectedTile)
                            status = "menuOpen"
                            blueLabel.posx = col #change to normal ring later, x = col
                            blueLabel.posy = row
                            blueLabel.visible = True
                            actionButton1.color = pygame.Color("blue")
                            actionButton2.color = pygame.Color("green")
                            cancelButton.color = pygame.Color("red")
                if status == "menuOpen":
                    print("hee hee haa haa")
                    #Pygame draws rectangles using the coords from the top left
                    if checkForCancel(location):
                        #cancel
                        cancel()
                        print("get canceled lol")
                    elif location[0] >= actionButton1.x\
                    and location[0] <= actionButton1.x + actionButton1.width\
                    and location[1] >= actionButton1.y\
                    and location[1] <= actionButton1.y + actionButton1.height:
                        status = "actionButton1"
                        actionButton2.color = pygame.Color("grey")
                        prompt.text = "select a tile to move to"
                        print(prompt.text)
                    elif location[0] >= actionButton2.x\
                    and location[0] <= actionButton2.x + actionButton2.width\
                    and location[1] >= actionButton2.y\
                    and location[1] <= actionButton2.y + actionButton2.height:
                        status = "actionButton2"
                        subStatus = "a1"
                        actionButton1.color = pygame.Color("grey")
                if status == "actionButton1":
                    print(status)
                    if checkForCancel(location):
                        cancel()
                    if location[0] <= 8.5*tileSize:
                        col = location[0]//tileSize
                        row = location[1]//tileSize
                        if row <= 7 and col <= 7:
                            print(row, col)
                            print(playerClicks)
                            if checkValidMove(board[playerClicks[0][0]][playerClicks[0][1]], playerClicks[0][0], playerClicks[0][1], row, col) == True:
                                moveStack(playerClicks[0][0], playerClicks[0][1], row, col)
                                cancel() #end move
                            else:
                                cancel()
                if status == "actionButton2":
                    global pieceToMove
                    if checkForCancel(location):
                        cancel()
                    if subStatus == "a1":
                        prompt.text = "select a piece to remove"
                        print(prompt.text)
                        col, row = selectedTile
                        targetStack = board[col][row]
                        listPieces(screen, targetStack)
                        subStatus = "a2"
                    elif subStatus == "a2":
                        prompt.text = "select a piece to remove"
                        col = location[0]//tileSize
                        row = location[1]//tileSize
                        print(col, row)
                        if col == 11:
                            pieceToMove = targetStack[row-1]
                            print(pieceToMove.species, "speces")
                            subStatus = "b"
                    elif subStatus == "b":
                        prompt.text = "select tile"
                        #pieceToMove = targetStack
                        col = location[0]//tileSize
                        row = location[1]//tileSize
                        print(col, row)
                        startX, startY = selectedTile #selectedTile = start select
                        print(startX, startY)
                        dismantleStack(pieceToMove, startX, startY, row, col) #convert pieceToMove to array form later, row col is unsafe
                        cancel()#end
                    
            drawGame(screen, 0)

    pygame.quit()
main()
