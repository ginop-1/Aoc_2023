def p1(f):
    result = 0
    for line in f.readlines():
        line = line.split(": ")[1]
        winning = set(int(num) for num in line.split("|")[0].split(" ") if num != "")
        my_nums = set(int(num) for num in line.split("|")[1].split(" ") if num != "")
        intersection = winning.intersection(my_nums)
        if not intersection:
            continue
        result += pow(2, len(intersection) - 1)
    return result


def p2(f):
    n_lines = len(f.readlines())
    cards = [1 for _ in range(n_lines)]
    f.seek(0)
    for i, line in enumerate(f.readlines()):
        line = line.split(": ")[1]
        winning = set(int(num) for num in line.split("|")[0].split(" ") if num != "")
        my_nums = set(int(num) for num in line.split("|")[1].split(" ") if num != "")
        n_wins = len(winning.intersection(my_nums))
        for j in range(i + 1, i + 1 + n_wins):
            if not j > n_lines:
                cards[j] += 1 * cards[i]
    return sum(cards)


if __name__ == "__main__":
    with open("inputs/input4.txt", "r") as f:
        # print(p1(f))
        print(p2(f))
