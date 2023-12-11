def generate_complete_history(origin: list, part2=False):
    res = []
    res.append(origin)
    while True:
        res.append([])
        for i, val in enumerate(res[-2][:-1]):
            res[-1].append(res[-2][i + 1] - res[-2][i])
        if not any(res[-1]):  # all 0
            break
    res = list(reversed(res))
    res[0].append(0) if not part2 else res[0].insert(0, 0)
    for i, step in enumerate(res[1:], start=1):
        index = 0 if part2 else -1
        elem = step[index] + res[i - 1][index] * (-1 if part2 else 1)
        step.append(elem) if not part2 else step.insert(0, elem)
    return res


def p1(f):
    lines = f.read().splitlines()
    history = []
    for line in lines:
        vals = list(map(int, line.split()))
        test = generate_complete_history(vals)
        history.append(test[-1][-1])
    return sum(history)


def p2(f):
    lines = f.read().splitlines()
    history = []
    for line in lines:
        vals = list(map(int, line.split()))
        test = generate_complete_history(vals, part2=True)
        history.append(test[-1][0])
    return sum(history)


if __name__ == "__main__":
    with open("inputs/input9.txt") as f:
        print(p2(f))
