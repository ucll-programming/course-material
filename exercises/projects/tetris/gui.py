from tetris import Tetris
from position import Position
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

    def render():
        screen_width, screen_height = surface.get_size()
        pit_width, pit_height = tetris.pit.size
        block_pixel_size = min(screen_width / pit_width, screen_height / pit_height)
        pit_pixel_width = block_pixel_size * pit_width
        pit_pixel_height = block_pixel_size * pit_height
        horizontal_margin = (screen_width - pit_pixel_width) // 2
        vertical_margin = (screen_height - pit_pixel_height) // 2

        for y in range(pit_height):
            for x in range(pit_width):
                position = Position(x, y)
                block = tetris.pit[position]
                color = pygame.Color(block) if block is not None else pygame.Color('black')
                rectangle = pygame.Rect(
                    horizontal_margin + x * block_pixel_size,
                    vertical_margin + y * block_pixel_size,
                    block_pixel_size,
                    block_pixel_size,
                )
                pygame.draw.rect(surface, color, rectangle)

        for y in range(tetris.current_shape.height):
            for x in range(tetris.current_shape.width):
                position = Position(x, y)
                block = tetris.current_shape[position]
                if block is not None:
                    color = pygame.Color(block)
                    rectangle = pygame.Rect(
                        horizontal_margin + (tetris.current_shape_position.x + x) * block_pixel_size,
                        vertical_margin + (tetris.current_shape_position.y + y) * block_pixel_size,
                        block_pixel_size,
                        block_pixel_size,
                    )
                    pygame.draw.rect(surface, color, rectangle)


    pygame.init()

    surface = _create_main_surface()
    # font = pygame.font.SysFont(None, 48)
    clock = _create_clock()
    tetris = Tetris(8, 20)


    while True:
        process_events()

        elapsed_seconds = clock.tick(25) / 1000
        tetris.tick(elapsed_seconds)
        render()

        pygame.display.flip()


if __name__ == '__main__':
    main()
