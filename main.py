import pygame, sys
from pygame.locals import *

# Set Global var
WINDOWWIDTH = 540
WINDOWHEIGHT = 650
FPS = 30

# RGB
BACKGROUND = (255,255,255) # RGB

def main():
    pygame.init()
    
    # Set FPS, window dimension and background
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    DISPLAYSURF.fill(BACKGROUND)
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


if __name__ == '__main__':
    main()