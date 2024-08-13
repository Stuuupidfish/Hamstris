import pygame
import sys
import random
import time

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

grid = []
for i in range(gridHeight):
    grid.append([(0, 0, 0) for _ in range(gridWidth)])

# [[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#  [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],]


red1 = (255, 0, 0)  # ZBlock
orange2 = (255, 180, 0)  # LBlock
yellow3 = (255, 255, 0)  # OBlock
green4 = (0, 255, 0)  # SBlock
lightBlue5 = (0, 255, 255)  # IBlock
darkBlue6 = (0, 0, 255)  # JBlock
purple7 = (180, 0, 255)  # TBlock



class block:
    def __init__(self, name, color, shape, start_x, start_y):
        self.name = name
        self.shape = shape
        self.color = color
        self.start_x = start_x
        self.start_y = start_y

    def updateGrid(self):
        # draws in the grid / updates the grid
        for i in range(len(self.shape)):
            #i is row
            for j in range(len(self.shape[i])):
                #j is column
                if self.shape[i][j] > 0:
                    grid[self.start_y + i][self.start_x + j] = self.color

    def collides(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] > 0:
                    x = self.start_x + j
                    y = self.start_y + i
                    if x < 0 or x >= gridWidth or y >= gridHeight:
                        return True
                    # if grid[y][x] != (0, 0, 0):
                    #     return True
                    #BIG ISSUE
        return False

#REVIEW
    def rotateBlockCCW(self):
        oldShape = self.shape
        #[[0,1,0],
        # [1,1,1],
        # [0,0,0]]
        #Store the current shape of the block before modification
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

    def rotateBlockCW(self):
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



#CODE NEEDS REVIEW/FIXING
# def deleteRow(grid):
#     filledSquares = 0
#     for i in range(len(gridHeight)):
#         for j in range(len(gridWidth)):
#             if grid[i][j] != (0, 0, 0):
#                 filledSquares += 1
#                 if filledSquares == 10:
#                     grid.pop(i)
#                     grid.append([(0, 0, 0) for _ in range(gridWidth)])

# def fullRow(grid):

                

Iblock = block("I", lightBlue5, [[0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [1, 1, 1, 1],
                                 [0, 0, 0, 0]], 3, -2)
#fix center of rotation
Jblock = block("J", darkBlue6, [[1, 0, 0], 
                                [1, 1, 1],
                                [0, 0, 0]], 3, -1)
Lblock = block("L", orange2, [[0, 0, 1], 
                              [1, 1, 1],
                              [0, 0, 0]], 3, -1)
Oblock = block("O", yellow3, [[1, 1], 
                              [1, 1]], 4, -1)
Sblock = block("S", green4, [[0, 1, 1], 
                             [1, 1, 0],
                             [0, 0, 0]], 3, -1)
Tblock = block("T", purple7, [[0, 1, 0], 
                              [1, 1, 1],
                              [0, 0, 0]], 3, -1)
ZBlock = block("Z", red1, [[1, 1, 0], 
                           [0, 1, 1],
                           [0, 0 ,0]], 3, -1)

blocks = [Iblock, Jblock, Lblock, Oblock, Sblock, Tblock, ZBlock]






d_y = 1
d_x = 1

currentBlock = blocks[random.randint(0,6)]

fallTime = pygame.time.get_ticks() #returns the number of milliseconds since Pygame  initialized-- tracks elapsed time
#records the time when the block last moved down

fallSpeed = 500
#fall_speed defines how often the block should fall, in milliseconds

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            currentBlock.start_x += d_x
            if currentBlock.collides():
                currentBlock.start_x -= d_x
                print("right collision")
        if event.key == pygame.K_LEFT:
            currentBlock.start_x -= d_x
            if currentBlock.collides():
                currentBlock.start_x += d_x
                print("left collision")
        if event.key == pygame.K_DOWN:
            currentBlock.start_y += d_y
            if currentBlock.collides():
                currentBlock.start_y -= d_y
        if event.key == pygame.K_UP:
            currentBlock.rotateBlockCW()
            if currentBlock.start_y > gridHeight:
                currentBlock.start_y += d_y
        if event.key == pygame.K_z:
            currentBlock.rotateBlockCCW()
            if currentBlock.start_y > gridHeight:
                currentBlock.start_y += d_y

        


        print(currentBlock.start_y, currentBlock.start_x, currentBlock.shape, currentBlock.collides())

    


    now = pygame.time.get_ticks()
    #now gets the current time ( returns the number of milliseconds that have passed since Pygame was initialized)
    if now - fallTime > fallSpeed:
        #If this condition is True, it means enough time has passed for the block to fall by one row.
        currentBlock.start_y += 1
        if currentBlock.collides():
            currentBlock.start_y -= 1
            print("bottom collision")
            currentBlock.updateGrid()
            #make sure to give 0.5 sec for user input
        fallTime = now
        #Sets fallTime to the *current time*
        #that way it ensures that we can always find the difference that will track elapsed

        
    grid=[]
    for i in range(gridHeight):
        grid.append([(0, 0, 0) for _ in range(gridWidth)])
    #clears the grid
    currentBlock.updateGrid()

    
    screen.fill((0,0,0))
    for y in range(gridHeight):
        for x in range(gridWidth):
            color = grid[y][x]
            pygame.draw.rect(screen, color, pygame.Rect(x * blockWidth, y * blockWidth, blockWidth, blockWidth))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
