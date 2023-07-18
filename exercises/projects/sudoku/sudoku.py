def parse_char(char):
    if char == '.':
        return set(range(1, 10))
    else:
        return {int(char)}


def parse_row(row, row_index):
    return [((col_index, row_index), parse_char(char)) for col_index, char in enumerate(row)]


def parse(string):
    return [
        box
        for row_index, row in enumerate(string.splitlines())
        for box in parse_row(row, row_index)
    ]


def format_row(row):
    return "".join(map(str, row))


def create_grid(width, height, item):
    return [[item] * width for _ in range(height)]


def format_grid(solved_boxes):
    grid = create_grid(9, 9, None)
    for (x, y), v in solved_boxes:
        grid[y][x] = v
    return "\n".join(map(format_row, grid))


def same_row(p, q):
    return p[1] == q[1]


def same_column(p, q):
    return p[0] == q[0]


def same_square(p, q):
    return p[0] // 3 == q[0] // 3 and p[1] // 3 == q[1] // 3


def same_group(p, q):
    return same_row(p, q) or same_column(p, q) or same_square(p, q)


def remove_options(position, number, unsolved_boxes):
    return [
        (pos, domain - {number} if same_group(position, pos) else domain)
        for pos, domain in unsolved_boxes
    ]


def sort_by_number_of_possibilities(unsolved_boxes):
    return sorted(unsolved_boxes, key=lambda pair: len(pair[1]))


def solve(unsolved_boxes, solved_boxes):
    if len(unsolved_boxes) == 0:
        yield solved_boxes
    else:
        (pos, domain), *rest = sort_by_number_of_possibilities(unsolved_boxes)
        for value in domain:
            yield from solve(remove_options(pos, value, rest), [*solved_boxes, (pos, value)])


sudoku = """
..3.2.6..
9..3.5..1
..18.64..
..81.29..
7.......8
..67.82..
..26.95..
8..2.3..9
..5.1.3..
""".strip()

grid = parse(sudoku)

for solution in solve(grid, []):
    print(format_grid(solution))
    print()
