import pygame, sys
from pygame.locals import *

# Set Global var
WINDOWWIDTH = 540
WINDOWHEIGHT = 650
FPS = 30

# RGB
BACKGROUND = (255,255,255) # RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200,200,200)

# Grid dimension
SQUARESIZE = WINDOWWIDTH//3
CELLSIZE = SQUARESIZE//3


def main():
    global DISPLAYSURF, FPSCLOCK

    pygame.init()
    
    # Set FPS, window dimension and background
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    DISPLAYSURF.fill(BACKGROUND)

    # Display Grid
    drawgrid()

    pygame.display.set_caption('SUDOKU') 

    # Main game loop
    while True:
        for event in pygame.event.get():

            # Catch exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update game
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawgrid():
    # Small Cell lines
    # Vertical
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, GRAY,(x,0), (x,WINDOWWIDTH))

    # Horizontal
    for y in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, GRAY, (0,y), (WINDOWWIDTH,y))


    # Big cell lines
    # Vertical
    for x in range(0, WINDOWWIDTH,SQUARESIZE):
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0), (x,WINDOWWIDTH))
    
    # Horizontal
    for y in range(0, WINDOWWIDTH+1, SQUARESIZE):
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH,y))


if __name__ == '__main__':
    main()