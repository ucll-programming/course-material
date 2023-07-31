def count_lines_in_file(path):
    with open(path) as file:
        return len(file.readlines())
