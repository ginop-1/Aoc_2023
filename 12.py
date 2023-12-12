import cProfile
import itertools


def isCombinationValid(combination, nums):
    hashtags = [hashtag for hashtag in combination.split(".") if hashtag != ""]
    if len(hashtags) != len(nums):  # too much or too few hastags
        return False
    for hashtag, num in zip(hashtags, nums):
        if len(hashtag) != num:
            return False
    return True


def p1(f):
    lines = f.read().splitlines()
    # given a string with .,# and ?, get all permutation replacing ? with . and #
    res = 0
    for debug, line in enumerate(lines):
        raw_input, nums = line.split(" ")
        nums = [int(n) for n in nums.split(",")]

        indices = []
        for i, c in enumerate(raw_input):
            if c == "?":
                indices.append(i)

        for replacement in itertools.product(".#", repeat=len(indices)):
            x = list(raw_input)
            for i, r in zip(indices, replacement):
                x[i] = r

            if isCombinationValid("".join(x), nums):
                res += 1

    return res


def p2(f):
    pass


if __name__ == "__main__":
    with open("inputs/input12.txt") as f:
        cProfile.run("p1(f)", sort="cumulative")
