
import math
import pygame
import os

class board:
    board = [None]*(8*8);
    background = pygame.image.load("chessbg.png");

    def __init__(self):
        self.board = [None]*(8*8);






def main():
    pygame.init()
    pygame.display.list_modes()
    

    b = board;

    screenSize = 360,360;
    display = pygame.display.set_mode(screenSize);
    pygame.display.set_caption("Sjakk");
    pygame.display.update()
    print(b)


if __name__ == "__main__":
    main();