def count_lines_in_file(path):
    result = 0
    with open(path, encoding='utf-8') as file:
        while file.readline():
            result += 1
    return result


def remove_empty_lines(source, destination):
    with open(source) as in_file:
        with open(destination, 'w', encoding='utf-8') as out_file:
            for line in in_file:
                if line != '\n':
                    out_file.write(line)


def remove_duplicate_lines(source, destination):
    with open(source) as in_file:
        with open(destination, 'w', encoding='utf-8') as out_file:
            last_line = None
            for line in in_file:
                if line != last_line:
                    out_file.write(line)
                    last_line = line
