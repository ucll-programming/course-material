def count_lines_in_file(path):
    result = 0
    with open(path) as file:
        while file.readline():
            result += 1
    return result


def remove_empty_lines(source, destination):
    with open(source) as in_file:
        with open(destination, 'w') as out_file:
            for line in in_file:
                if line != '\n':
                    out_file.write(line)
