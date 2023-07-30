from pit import Pit
from position import Position
import shape


class Tetris:
    def __init__(self, width, height):
        self.pit = Pit(width, height)
        self.__game_over = False
        self.__prepare_new_shape()
        self.__time_until_next_drop = 1.0

    def __prepare_new_shape(self):
        n_rows_removed = self.pit.remove_full_rows()
        self.__current_shape = shape.random_shape()
        self.__current_shape_position = Position(self.pit.width // 2, 0)
        self.__game_over = not self.pit.fits(self.__current_shape, self.__current_shape_position)

    @property
    def game_over(self):
        return self.__game_over

    @property
    def current_shape(self):
        return self.__current_shape

    @property
    def current_shape_position(self):
        return self.__current_shape_position

    def tick(self, elapsed_seconds):
        self.__time_until_next_drop -= elapsed_seconds
        if self.__time_until_next_drop < 0:
            self.drop()
            self.__time_until_next_drop += 1

    def full_drop(self):
        if not self.game_over:
            self.pit.drop_shape(self.__current_shape, self.__current_shape_position)
            self.__prepare_new_shape()

    def rotate_shape(self):
        if not self.game_over:
            rotated_shape = self.__current_shape.rotate_cw()
            if self.pit.fits(rotated_shape, self.__current_shape_position):
                self.__current_shape = rotated_shape

    def drop(self):
        if not self.game_over:
            new_position = self.__current_shape_position + Position(0, 1)
            if self.pit.fits(self.__current_shape, new_position):
                self.__current_shape_position = new_position
            else:
                self.pit.place_shape(self.__current_shape, self.__current_shape_position)
                self.__prepare_new_shape()

    def move_left(self):
        if not self.game_over:
            new_position = self.__current_shape_position + Position(-1, 0)
            if self.pit.fits(self.__current_shape, new_position):
                self.__current_shape_position = new_position

    def move_right(self):
        if not self.game_over:
            new_position = self.__current_shape_position + Position(1, 0)
            if self.pit.fits(self.__current_shape, new_position):
                self.__current_shape_position = new_position