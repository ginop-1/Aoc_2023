def spin_cycle(lines):
    cache = {tuple(line for line in lines): 0}
    cycle_n = 1
    while True:
        # north
        cols = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]
        lines = [[] for _ in range(len(lines))]
        for col in cols:
            splitted = col.split("#")
            splitted = [
                "O" * split.count("O") + "." * split.count(".") for split in splitted
            ]
            final = list("".join(split for split in splitted if split != ""))
            hashtags = [i for i, c in enumerate(col) if c == "#"]
            for hashtag in hashtags:
                final.insert(hashtag, "#")
            [lines[i].append(c) for i, c in enumerate(final)]
        # west
        rows = ["".join(line) for line in lines]
        lines = [[] for _ in range(len(lines))]
        for c, row in enumerate(rows):
            splitted = row.split("#")
            splitted = [
                "O" * split.count("O") + "." * split.count(".") for split in splitted
            ]
            final = list("".join(split for split in splitted if split != ""))
            hashtags = [i for i, c in enumerate(row) if c == "#"]
            for hashtag in hashtags:
                final.insert(hashtag, "#")
            lines[c] = final
        # south
        cols = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]
        lines = [[] for _ in range(len(lines))]
        for col in cols:
            splitted = col.split("#")
            splitted = [
                "." * split.count(".") + "O" * split.count("O") for split in splitted
            ]
            final = list("".join(split for split in splitted if split != ""))
            hashtags = [i for i, c in enumerate(col) if c == "#"]
            for hashtag in hashtags:
                final.insert(hashtag, "#")
            [lines[i].append(c) for i, c in enumerate(final)]
        # east
        rows = ["".join(line) for line in lines]
        lines = [[] for _ in range(len(lines))]
        for c, row in enumerate(rows):
            splitted = row.split("#")
            splitted = [
                "." * split.count(".") + "O" * split.count("O") for split in splitted
            ]
            final = list("".join(split for split in splitted if split != ""))
            hashtags = [i for i, c in enumerate(row) if c == "#"]
            for hashtag in hashtags:
                final.insert(hashtag, "#")
            lines[c] = final

        lines = tuple(tuple(line) for line in lines)
        if lines in cache:
            cycle = cycle_n - cache[lines]
            idx = cache[lines] + (1000000000 - cache[lines]) % cycle
            for k, v in cache.items():
                if v == idx:
                    return k
        else:
            cache[lines] = cycle_n
        lines = [list(line) for line in lines]
        cycle_n += 1


def p1(f):
    lines = f.read().split("\n")
    tot_rows = len(lines)
    cols = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]
    res = 0
    for col in cols:
        splitted = col.split("#")
        splitted = [
            "O" * split.count("O") + "." * split.count(".") for split in splitted
        ]
        final = list("".join(split for split in splitted if split != ""))
        hashtags = [i for i, c in enumerate(col) if c == "#"]
        for hashtag in hashtags:
            final.insert(hashtag, "#")
        for i, c in enumerate(final):
            if c == "O":
                res += tot_rows - i
    return res


def p2(f):
    lines = f.read().split("\n")
    lines = spin_cycle(lines)
    res = 0
    for ix, line in enumerate(lines):
        res += line.count("O") * (len(lines) - ix)
    return res


if __name__ == "__main__":
    with open("inputs/input14.txt") as f:
        print(p2(f))
