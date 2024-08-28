
import pygame
import sys
import random
import copy
 
# import time

pygame.init()

blockWidth = 30
gridWidth = 10
gridHeight = 20

screen = pygame.display.set_mode(
    (gridWidth * blockWidth, gridHeight * blockWidth))
# 10 cells wide & 20 tall
# each 30 px


clock = pygame.time.Clock()

run = True

def init_grid():
    return [[(0, 0, 0) for _ in range(gridWidth)] for _ in range(gridHeight)]


grid = init_grid()

collisionGrid = init_grid()


def drawGridLines():
    for i in range(gridWidth):
        pygame.draw.line(screen, (90, 90, 90), (blockWidth*i, 0), (blockWidth*i, gridHeight*blockWidth))
    for j in range(gridHeight):
        pygame.draw.line(screen, (90, 90, 90), (0, blockWidth*j), (gridWidth*blockWidth, blockWidth*j))

red1 = (255, 0, 0)  # Ztetromino
orange2 = (255, 180, 0)  # Ltetromino
yellow3 = (255, 255, 0)  # Otetromino
green4 = (0, 255, 0)  # Stetromino
lightBlue5 = (0, 255, 255)  # Itetromino
darkBlue6 = (0, 0, 255)  # Jtetromino
purple7 = (180, 0, 255)  # Ttetromino

# movement = True
#test

class tetromino:
    def __init__(self, color, shape, originalShape, start_x, start_y):
        self.shape = shape
        self.originalShape = originalShape
        self.color = color
        self.start_x = start_x
        self.start_y = start_y

    
    def updateGrid(self):
        # draws in the grid / updates the grid
        for i in range(len(self.shape)):
            #i is row
            for j in range(len(self.shape[i])):
                #j is column
                if self.shape[i][j] == 1:
                    x = self.start_x + j
                    y = self.start_y + i
                    grid[y][x] = self.color 
                    

    def collides(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    x = self.start_x + j
                    y = self.start_y + i
                    if x < 0 or x >= gridWidth or y >= gridHeight or y < 0:
                        return True
                    if y >= 0 and collisionGrid[y][x] != (0, 0, 0):
                        return True
        return False
    
        # collision = pygame.sprite.collide_rect(self, self.shape)
        # if collision:
        #     return True
        # return

#REVIEW
    def rotateTetrominoCCW(self):
        oldShape = self.shape
        #[[0,1,0],
        # [1,1,1],
        # [0,0,0]]
        #Store the current shape of the tetromino before modification
        newShape = list(zip(*oldShape[::-1]))  # Rotate counterclockwise
            #[::-1] reverses the order of rows in the matrix (180 turn)
            #he double colon (::) is used in slicing to specify the step value. 
                #For example, list[::2] will return every second element in the list
            #in this case it will return every element in the list backwards which produces:
                #[[0,0,0],
                # [1,1,1],
                # [0,1,0]]
            #* unpacks the reversed rows into the zip function. 
            # zip function takes the unpacked rows and groups corresponding elements from each row into tuples
            # The first tuple is (0, 1, 0) (first element of each row).
            # The second tuple is (0, 1, 1) (second element of each row).
            # The third tuple is (0, 1, 0) (third element of each row)
            #(0,1,0)
            #(0,1,1)
            #(0,1,0)
            #list(zip(*oldShape[::-1])) converts the tuples into a list of lists.
            #[[0,1,0],
            # [0,1,1],
            # [0,1,0]]
        self.shape = newShape

    #reverse rows and then transpose

    def rotateTetrominoCW(self):
        oldShape = self.shape
        #[[0,1,0],
        # [1,1,1],
        # [0,0,0]]
        newShape = list(zip(*oldShape))[::-1]  # Rotate clockwise
        #first it unpacks and zips
        #The first tuple is (0, 1, 0) (first element of each row).
        # The second tuple is (1, 1, 0) (second element of each row)
        # The third tuple is (0, 1, 0) (third element of each row
        # (0,1,0)
        # (1,1,0)
        # (0,1,0)
        # then it turns it into a list and flips it 180
        # [[0,1,0],
        #  [0,1,1],
        #  [0,1,0]]
        self.shape = newShape
        #transpose and then reverse rows

    def clearTetrominoFromGrid(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    x = self.start_x + j
                    y = self.start_y + i
                    if 0 <= x < gridWidth and 0 <= y < gridHeight:
                        grid[y][x] = (0, 0, 0)

                        
        


def deleteRow(grid, row):
    grid.pop(row)
    grid.insert(0, [(0, 0, 0) for _ in range(gridWidth)])

def checkDeleteFullRows(grid):
    for i in range(gridHeight):
        if all(cell != (0, 0, 0) for cell in grid[i]):
            deleteRow(grid, i)




I = tetromino(lightBlue5, [[0, 0, 0, 0],
                                 [1, 1, 1, 1],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]], [[0, 0, 0, 0],
                                                [1, 1, 1, 1],
                                                [0, 0, 0, 0],
                                                [0, 0, 0, 0]], 3, -1)
#fix center of rotation
J = tetromino(darkBlue6, [[1, 0, 0], 
                                [1, 1, 1],
                                [0, 0, 0]], [[1, 0, 0], 
                                            [1, 1, 1],
                                            [0, 0, 0]],3, 0)
L = tetromino(orange2, [[0, 0, 1], 
                              [1, 1, 1],
                              [0, 0, 0]], [[0, 0, 1], 
                                            [1, 1, 1],
                                            [0, 0, 0]],3, 0)
O = tetromino(yellow3, [[1, 1], 
                              [1, 1]], [[1, 1], 
                                        [1, 1]],4, 0)
S = tetromino(green4, [[0, 1, 1], 
                             [1, 1, 0],
                             [0, 0, 0]], [[0, 1, 1], 
                                        [1, 1, 0],
                                        [0, 0, 0]],3, 0)
T = tetromino(purple7, [[0, 1, 0], 
                              [1, 1, 1],
                              [0, 0, 0]], [[0, 1, 0], 
                                            [1, 1, 1],
                                            [0, 0, 0]],3, 0)
Z = tetromino(red1, [[1, 1, 0], 
                           [0, 1, 1],
                           [0, 0 ,0]], [[1, 1, 0], 
                                        [0, 1, 1],
                                        [0, 0 ,0]],3, 0)


tetrominoes = [I, J, L, O, S, T, Z]



d_y = 1
d_x = 1

def getNewTetromino():
    return tetrominoes[random.randint(0, len(tetrominoes) - 1)]
currentTetromino = getNewTetromino()

def grabNewTetromino():
    global collisionGrid
    global currentTetromino
    currentTetromino.updateGrid()
    checkDeleteFullRows(grid)
    
    collisionGrid = copy.deepcopy(grid)

    currentTetromino = getNewTetromino()
    currentTetromino.start_x = 3
    currentTetromino.start_y = 0
    currentTetromino.shape = currentTetromino.originalShape
    if currentTetromino == I:
        currentTetromino.start_y = -1
    if currentTetromino == O:
        currentTetromino.start_x = 4
    # return collisionGrid, currentTetromino


def gameOver():
    isAtTop = False
    for i in range(len(currentTetromino.shape)):
            for j in range(len(currentTetromino.shape[i])):
                if currentTetromino.shape[i][j] == 1:
                    x = currentTetromino.start_x + j
                    y = currentTetromino.start_y + i
                    if y == 0 and collisionGrid[y][x] != (0, 0, 0):
                        isAtTop = True
    if currentTetromino.collides() and isAtTop == True:
        # print("game over")
        return True



fallTime = pygame.time.get_ticks() #returns the number of milliseconds since Pygame  initialized-- tracks elapsed time
#records the time when the tetromino last moved down

fallSpeed = 500
#fall_speed defines how often the tetromino should fall, in milliseconds

while run:
    for event in pygame.event.get():

        #OIHSCNAUXJIAKLXBICAHOIJKCGIHOJA

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                currentTetromino.rotateTetrominoCW()
                if currentTetromino.collides():
                    currentTetromino.rotateTetrominoCCW()
            if event.key == pygame.K_z:
                # print("z key pressed")
                currentTetromino.rotateTetrominoCCW()
                if currentTetromino.collides():
                    currentTetromino.rotateTetrominoCW()
            if event.key == pygame.K_SPACE:
                #hard drops
                # movement == False
                while not currentTetromino.collides():
                    currentTetromino.start_y += d_y
                currentTetromino.start_y -= d_y  # Move back one step since the last move caused a collision
                grabNewTetromino()
            # else:
            #     movement == True
    if event.type == pygame.KEYDOWN:
        # print("a key has been pressed")
        # if movement == True:
        if event.key == pygame.K_RIGHT:
            currentTetromino.start_x += d_x
            if currentTetromino.collides():
                currentTetromino.start_x -= d_x
                # print("right collision")
        if event.key == pygame.K_LEFT:
            currentTetromino.start_x -= d_x
            if currentTetromino.collides():
                currentTetromino.start_x += d_x
                # print("left collision")
        if event.key == pygame.K_DOWN:
            currentTetromino.start_y += d_y
            if currentTetromino.collides():
                currentTetromino.start_y -= d_y
        

        # print(currenttetromino.start_y, currenttetromino.start_x, currenttetromino.shape, currenttetromino.collides())

    


    now = pygame.time.get_ticks()
    #now gets the current time ( returns the number of milliseconds that have passed since Pygame was initialized)
    if now - fallTime > fallSpeed:
        #If this condition is True, it means enough time has passed for the tetromino to fall by one row.
        # if movement == True:
        currentTetromino.start_y += 1
        if currentTetromino.collides():
            currentTetromino.start_y -= 1
            # print("bottom collision")
            grabNewTetromino()


            #make sure to give 0.5 sec for user input
        fallTime = now
        #Sets fallTime to the *current time*
        #that way it ensures that we can always find the difference that will tracpyk elapsed

    if gameOver() == True:
        sys.exit()

        
    # grid=[]
    # for i in range(gridHeight):
    #     grid.append([(0, 0, 0) for _ in range(gridWidth)])

    grid = copy.deepcopy(collisionGrid)
    #clears the grid


    currentTetromino.updateGrid()

    #pygame.version.ver

    #screen.fill((0,0,0))

    for y in range(gridHeight):
        for x in range(gridWidth):
            color = grid[y][x]
            pygame.draw.rect(screen, color, pygame.Rect(x * blockWidth, y * blockWidth, blockWidth, blockWidth))

    drawGridLines()
    currentTetromino.clearTetrominoFromGrid()
    pygame.display.update()
    clock.tick(10)

# print(collisionGrid)
# print(grid)

pygame.quit()
sys.exit()

