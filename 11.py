def p1(f):
    lines = [line.strip() for line in f.read().splitlines()]
    i = 0
    while i < len(lines):
        if lines[i] == "." * len(lines[i]):
            lines.insert(i + 1, "." * len(lines[i]))
            i += 2
        else:
            i += 1
    i = 0
    while i < len(lines[0]):
        if all([line[i] == "." for line in lines]):
            for j in range(len(lines)):
                lines[j] = lines[j][: i + 1] + "." + lines[j][i + 1 :]
            i += 2
        else:
            i += 1
    matrix_coords = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                matrix_coords.append((i, j))
    matrix_dist = {}
    for ix, (i, j) in enumerate(matrix_coords):
        matrix_dist[(i, j)] = {}
        for x, y in matrix_coords[ix:]:
            if (i, j) != (x, y):
                matrix_dist[(i, j)][(x, y)] = abs(i - x) + abs(j - y)
    sum = 0
    for galax in matrix_dist:
        for distances in matrix_dist[galax].values():
            sum += distances
    return sum


def p2(f):
    lines = [line.strip() for line in f.read().splitlines()]
    empty_rows = [i for i, line in enumerate(lines) if line == "." * len(lines[i])]
    empty_cols = [
        i for i in range(len(lines[0])) if all([line[i] == "." for line in lines])
    ]
    matrix_coords = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                matrix_coords.append((x, y))
    matrix_dist = {}
    # empty line and empty cols are counted as 1000000 distance
    for ix, (i, j) in enumerate(matrix_coords):
        matrix_dist[(i, j)] = {}
        for x, y in matrix_coords[ix:]:
            if (i, j) != (x, y):
                matrix_dist[(i, j)][(x, y)] = 0
                # check if a empty row or col is between the two points
                for empty_row in empty_rows:
                    if j < empty_row < y:
                        matrix_dist[(i, j)][(x, y)] += 999999
                for empty_col in empty_cols:
                    if i < empty_col < x or x < empty_col < i:
                        matrix_dist[(i, j)][(x, y)] += 999999
                matrix_dist[(i, j)][(x, y)] += abs(i - x) + abs(j - y)
    sum = 0
    for galax in matrix_dist:
        for distances in matrix_dist[galax].values():
            sum += distances
    return sum


if __name__ == "__main__":
    with open("input11.txt") as f:
        print(p2(f))
