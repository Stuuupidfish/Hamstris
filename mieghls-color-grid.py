import pygame
import sys

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
            for j in range(len(self.shape[i])):
                if self.shape[i][j] > 0:
                    grid[self.start_y + i][self.start_x + j] = self.color


IBlock = block("I", lightBlue5, [[5, 5, 5, 5, 5]], 3, 0)
JBlock = block("J", darkBlue6, [[6, 0, 0], [6, 6, 6]], 3, 0)
LBlock = block("L", orange2, [[0, 0, 2], [2, 2, 2]], 3, 0)
Oblock = block("O", yellow3, [[3, 3], [3, 3]], 4, 0)
Sblock = block("S", green4, [[0, 4, 4], [4, 4, 0]], 3, 0)
Tblock = block("T", purple7, [[0, 7, 0], [7, 7, 7]], 3, 0)
ZBlock = block("Z", red1, [[1, 1, 0], [0, 1, 1]], 3, 0)
blocks = [IBlock, JBlock, LBlock, Oblock, Sblock, Tblock, ZBlock]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for block in blocks:
        # block.start_y += blockWidth
        block.updateGrid()

    for y in range(gridHeight):
        for x in range(gridWidth):
            color = grid[y][x]
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(x * blockWidth, y * blockWidth,
                            blockWidth, blockWidth),
            )

    pygame.display.update()
    clock.tick(1)

pygame.quit()
sys.exit()
