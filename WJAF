import pygame
import sys
import random

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

    def rotateBlockCCW(self, shape, start_x, start_y):
        CCW = [[0, -1],
               [1, 0]]
        #[x'] = [xcos(theta) - ysin(theta)]
        #[y'] = [xsin(theta) + ycos(theta)]
        
        # new_shape = [[0, 0, 0],
        #              [0, 0, 0],
        #              [0, 0, 0]]

        for i in range(len(self.shape)):
            #i is row
            for j in range(len(self.shape[i])):
                #j is column

                # j is the x value 
                # i is y value
    
                self.shape[i] = self.shape[i]*CCW[0][0] - self.shape[i]*CCW[0][1]
                self.shape[j] = self.shape[j]*CCW[1][0] - self.shape[i]*CCW[1][1]

    def rotateBlockCW(self):
        CW = [[0, 1],
              [-1, 0]]
        #[x'] = [xcos(theta) - ysin(theta)]
        #[y'] = [xsin(theta) + ycos(theta)]

            

#CODE NEEDS REVIEW/FIXING
# def deleteRow(grid):
#     for i in range(len(gridHeight)):
#             if grid[i] > 0:
#                 grid.pop[i]
#                 grid.append([(0, 0, 0) for _ in range(gridWidth)])
                

IBlock = block("I", lightBlue5, [[1, 1, 1, 1, 1]], 3, -1)
JBlock = block("J", darkBlue6, [[1, 0, 0], 
                                [1, 1, 1],
                                [0, 0, 0]], 3, -1)
LBlock = block("L", orange2, [[0, 0, 1], 
                              [1, 1, 1],
                              [0, 0, 0]], 3, -1)
Oblock = block("O", yellow3, [[1, 1, 0], 
                              [1, 1, 0],
                              [0, 0, 0]], 4, -1)
Sblock = block("S", green4, [[0, 1, 1], 
                             [1, 1, 0],
                             [0, 0, 0]], 3, -1)
Tblock = block("T", purple7, [[0, 1, 0], 
                              [1, 1, 1],
                              [0, 0, 0]], 3, -1)
ZBlock = block("Z", red1, [[1, 1, 0], 
                           [0, 1, 1],
                           [0, 0 ,0]], 3, -1)
blocks = [IBlock, JBlock, LBlock, Oblock, Sblock, Tblock, ZBlock]






d_y = 1
d_x = 1
currentBlock = blocks[random.randint(0,6)]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            currentBlock.start_x += d_x
        if event.key == pygame.K_LEFT:
            currentBlock.start_x -= d_x
        if event.key == pygame.K_DOWN:
            currentBlock.start_y += d_y
        if event.key == pygame.K_UP:
            if currentBlock != blocks[0]  or blocks[3]:
                currentBlock.rotateBlockCCW

    
    grid=[]
    for i in range(gridHeight):
        grid.append([(0, 0, 0) for _ in range(gridWidth)])

    screen.fill((0,0,0))

    currentBlock.start_y += d_y
    currentBlock.updateGrid()

    
    for y in range(gridHeight):
        for x in range(gridWidth):
            color = grid[y][x]
            pygame.draw.rect(screen, color, pygame.Rect(x * blockWidth, y * blockWidth, blockWidth, blockWidth),
            )

    pygame.display.update()
    clock.tick(5)

pygame.quit()
sys.exit()
