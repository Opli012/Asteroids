# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        delta = clock.tick(60)
        dt = delta / 1000

        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
