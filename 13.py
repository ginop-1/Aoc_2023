def p1(f, part2: bool = False):
    patterns = [pattern.split("\n") for pattern in f.read().split("\n\n")]
    res = 0
    for debug, pattern in enumerate(patterns):
        if debug == 14:
            pass
        axe = None
        for i in range(1, len(pattern)):  # check horizontal symmetry
            up = "".join(reversed(pattern[0:i]))
            down = "".join(pattern[i:])
            mirror = [up[j] == down[j] for j in range(min(len(up), len(down)))]
            if all(mirror) and part2 is False:
                axe = i
                break
            if mirror.count(False) == 1 and part2 is True:
                axe = i
                break
        if axe is not None:
            res += axe * 100
            continue
        for i in range(1, len(pattern[0])):  # check vertical symmetry
            left = []
            for col_n in range(0, i):
                left.insert(0, [])
                for row_n in range(len(pattern)):
                    left[0].append(pattern[row_n][col_n])
            left = [item for sublist in left for item in sublist]
            right = []
            for col_n in range(i, len(pattern[0])):
                for row_n in range(len(pattern)):
                    right.append(pattern[row_n][col_n])
            mirror = [left[j] == right[j] for j in range(min(len(left), len(right)))]
            if all(mirror) and part2 is False:
                axe = i
                break
            if mirror.count(False) == 1 and part2 is True:
                axe = i
                break
        if axe is not None:
            res += axe
        if axe is None:
            pass
    return res


def p2(f):
    return p1(f, part2=True)


if __name__ == "__main__":
    with open("inputs/input13.txt") as f:
        print(p2(f))
