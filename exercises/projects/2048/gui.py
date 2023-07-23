import pygame
from game import *
import grid
import sys


screen_width = 640
screen_height = 640


def _create_main_surface():
    screen_size = (screen_width, screen_height)
    return pygame.display.set_mode(screen_size)


def _create_clock():
    return pygame.time.Clock()


def main():
    def process_events():
        nonlocal tiles
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                has_changed = False
                if event.key == pygame.K_LEFT:
                    tiles, has_changed = shift_grid_left(tiles)
                elif event.key == pygame.K_RIGHT:
                    tiles, has_changed = shift_grid_right(tiles)
                elif event.key == pygame.K_UP:
                    tiles, has_changed = shift_grid_up(tiles)
                elif event.key == pygame.K_DOWN:
                    tiles, has_changed = shift_grid_down(tiles)
                if has_changed:
                    add_random_tile(tiles)

    def render():
        w = grid.width(tiles)
        h = grid.height(tiles)
        tile_size = min(screen_width // w, screen_height // h)
        for x in range(grid.width(tiles)):
            for y in range(grid.height(tiles)):
                rectangle = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, (0, 0, 0), rectangle)
                rectangle.inflate_ip(-2, -2)
                pygame.draw.rect(surface, (192, 192, 192), rectangle)
                caption = tiles[y][x]
                if caption is not None:
                    text_surface = font.render(str(tiles[y][x]), True, (0, 0, 0))
                    px, py = rectangle.center
                    px -= text_surface.get_width() // 2
                    py -= text_surface.get_height() // 2
                    surface.blit(text_surface, (px, py))


    pygame.init()

    surface = _create_main_surface()
    font = pygame.font.SysFont(None, 48)
    clock = _create_clock()
    tiles = create_empty_grid(4)
    add_random_tile(tiles)
    add_random_tile(tiles)


    while True:
        process_events()

        clock.tick(25)
        render()

        pygame.display.flip()


main()
