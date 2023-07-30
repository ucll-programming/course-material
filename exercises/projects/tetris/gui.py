from tetris import Tetris
from position import Position
from renderer import Renderer
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
                if key == pygame.K_LEFT:
                    tetris.move_left()
                elif key == pygame.K_RIGHT:
                    tetris.move_right()
                elif key == pygame.K_UP:
                    tetris.rotate_shape()
                elif key == pygame.K_DOWN:
                    tetris.drop()
                elif key == pygame.K_SPACE:
                    tetris.full_drop()

    pygame.init()

    surface = _create_main_surface()
    # font = pygame.font.SysFont(None, 48)
    clock = _create_clock()
    tetris = Tetris(10, 20)
    renderer = Renderer(surface, tetris)

    while True:
        process_events()

        elapsed_seconds = clock.tick(25) / 1000
        tetris.tick(elapsed_seconds)
        renderer.render()

        pygame.display.flip()


if __name__ == '__main__':
    main()
