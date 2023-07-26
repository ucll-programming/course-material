from tetris import *
import pygame
import sys


screen_width = 640
screen_height = 480


def _create_main_surface():
    screen_size = (screen_width, screen_height)
    return pygame.display.set_mode(screen_size)

def _create_clock():
    return pygame.time.Clock()



def main():
    def process_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = event.key


    def render():
        ...

    pygame.init()

    surface = _create_main_surface()
    # font = pygame.font.SysFont(None, 48)
    clock = _create_clock()



    while True:
        process_events()

        clock.tick(25)
        render()

        pygame.display.flip()



if __name__ == '__main__':
    main()
