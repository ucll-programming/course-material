from tetris import Tetris
from position import Position
import pygame


class Renderer:
    def __init__(self, surface, tetris):
        self.__surface = surface
        self.__tetris = tetris
        screen_width, screen_height = surface.get_size()
        pit_width, pit_height = tetris.pit.size
        self.__block_pixel_size = min(screen_width / pit_width, screen_height / pit_height)
        pit_pixel_width = self.__block_pixel_size * pit_width
        pit_pixel_height = self.__block_pixel_size * pit_height
        self.__horizontal_margin = (screen_width - pit_pixel_width) // 2
        self.__vertical_margin = (screen_height - pit_pixel_height) // 2

    def render(self):
        self.__render_pit()
        self.__render_shape()

    def __render_pit(self):
        pit = self.__tetris.pit
        for y in range(pit.height):
            for x in range(pit.width):
                position = Position(x, y)
                block = pit[position]
                color = pygame.Color(block) if block is not None else pygame.Color('black')
                self.__render_block(position, color)

    def __render_shape(self):
        shape = self.__tetris.current_shape
        shape_position = self.__tetris.current_shape_position
        block_pixel_size = self.__block_pixel_size
        for y in range(shape.height):
            for x in range(shape.width):
                position = Position(x, y)
                block = shape[position]
                if block is not None:
                    color = pygame.Color(block)
                    self.__render_block(shape_position + position, color)

    def __render_block(self, position, color):
        block_pixel_size = self.__block_pixel_size
        rectangle = pygame.Rect(
            self.__horizontal_margin + position.x * block_pixel_size,
            self.__vertical_margin + position.y * block_pixel_size,
            block_pixel_size,
            block_pixel_size,
        )
        pygame.draw.rect(self.__surface, color, rectangle)