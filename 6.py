def p1(f):
    lines = f.readlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    races = zip(times, distances)
    result = 1
    for race in races:
        count = 0
        for i in range(0, race[0] + 1):
            space = (race[0] - i) * i
            if space > race[1]:
                count += 1
        result *= count
    return result


def p2(f):
    # bruteforce solution
    lines = f.readlines()
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    race = (time, distance)
    result = 1
    for i in range(0, race[0] + 1):
        space = (race[0] - i) * i
        if space > race[1]:
            result += 1
    return result


if __name__ == "__main__":
    with open("input6.txt") as f:
        print(p2(f))
