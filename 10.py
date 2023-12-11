import os


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y


def nextPoint(x, y, lines, direction, pointsSeen):
    match direction:
        case "north":
            if Point(x - 1, y) in pointsSeen:
                return
            if lines[x - 1][y] in ["|", "7", "F"]:
                return Point(x - 1, y)
        case "south":
            if Point(x + 1, y) in pointsSeen:
                return
            if lines[x + 1][y] in ["|", "L", "J"]:
                return Point(x + 1, y)
        case "east":
            if Point(x, y + 1) in pointsSeen:
                return
            if lines[x][y + 1] in ["-", "J", "7"]:
                return Point(x, y + 1)
        case "west":
            if Point(x, y - 1) in pointsSeen:
                return
            if lines[x][y - 1] in ["-", "L", "F"]:
                return Point(x, y - 1)
        case _:
            assert False


def p1(f, onlyPath=False):
    lines = f.read().splitlines()
    lines.append("." * (len(lines[0])))  # last . points
    lines.insert(0, lines[-1])
    lines = ["." + line + "." for line in lines]
    lines = [[char for char in line] for line in lines]
    start = []
    for i, line in enumerate(lines):
        for j, elem in enumerate(line):
            if elem == "S":
                start = Point(i, j)
                break
    lines[start.x][start.y] = "-"
    current = Point(start.x, start.y)
    steps = 0
    seen = []
    if onlyPath and "path10.out" in os.listdir():
        with open("path10.out") as f:
            return [Point(*map(int, line.split())) for line in f.read().splitlines()]
    while True:
        if current.x == start.x and current.y == start.y and steps != 0:
            break
        match lines[current.x][current.y]:
            case "|":
                next = nextPoint(current.x, current.y, lines, "north", seen)
                if not next:
                    next = nextPoint(current.x, current.y, lines, "south", seen)
                seen.append(next)
            case "-":
                next = nextPoint(current.x, current.y, lines, "east", seen)
                if not next:
                    next = nextPoint(current.x, current.y, lines, "west", seen)
                seen.append(next)
            case "L":
                next = nextPoint(current.x, current.y, lines, "east", seen)
                if not next:
                    next = nextPoint(current.x, current.y, lines, "north", seen)
                seen.append(next)
            case "J":
                next = nextPoint(current.x, current.y, lines, "west", seen)
                if not next:
                    next = nextPoint(current.x, current.y, lines, "north", seen)
                seen.append(next)
            case "7":
                next = nextPoint(current.x, current.y, lines, "south", seen)
                if not next:
                    next = nextPoint(current.x, current.y, lines, "west", seen)
                seen.append(next)
            case "F":
                next = nextPoint(current.x, current.y, lines, "south", seen)
                if not next:
                    next = nextPoint(current.x, current.y, lines, "east", seen)
                seen.append(next)
            case _:
                assert False
        current = next
        steps += 1
    with open("path10.out", "w") as f:
        for point in seen:
            f.write(f"{point.x} {point.y}\n")
    if onlyPath:
        return seen
    return steps // 2


def p2(f):
    path = p1(f, True)
    # calculate area of polygon using shoelace formula
    area = 0.0
    for i in range(len(path)):
        j = (i + 1) % len(path)
        area += path[i].x * path[j].y
        area -= path[j].x * path[i].y
    area = abs(area) / 2.0
    # given area and number of points, calculate internal points
    # using Pick's theorem
    i = area - len(path) / 2.0 + 1
    return int(i)


if __name__ == "__main__":
    with open("input10.txt") as f:
        print(p2(f))
