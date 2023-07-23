from game import *

def input_direction():
    while (result := input()) not in "asdw":
        pass
    return result


def print_grid(tiles):
    def format_tile(tile):
        if tile is not None:
            return str(tile).center(5, ' ')
        else:
            return '.'.center(5, ' ')

    for row in tiles:
        print("".join(format_tile(tile) for tile in row))


def main():
    tiles = create_empty_grid(4)
    add_random_tile(tiles)
    has_changed = True

    while not is_filled(tiles):
        if has_changed:
            add_random_tile(tiles)
        print_grid(tiles)
        match input_direction():
            case 'a':
                tiles, has_changed = shift_grid_left(tiles)
            case 's':
                tiles, has_changed = shift_grid_down(tiles)
            case 'd':
                tiles, has_changed = shift_grid_right(tiles)
            case 'w':
                tiles, has_changed = shift_grid_up(tiles)


if __name__ == '__main__':
    main()
