def issymbol(char):
    if char.isdigit() or char == ".":
        return False
    return True


def process_line(previous: str, current: str, next: str):
    previous = "." + previous[:-1] + "."
    current = "." + current[:-1] + "."
    next = "." + next[:-1] + "."
    num_result = 0
    num_str = ""
    is_valid = False
    for i, char in enumerate(current[1:-1]):
        i = i + 1
        if char.isdigit():
            num_str = num_str + char
            # upper elements
            if (
                issymbol(previous[i - 1])
                or issymbol(previous[i])
                or issymbol(previous[i + 1])
            ):
                is_valid = True
            # lower elements
            elif issymbol(next[i - 1]) or issymbol(next[i]) or issymbol(next[i + 1]):
                is_valid = True
            # left and right
            elif issymbol(current[i - 1]) or issymbol(current[i + 1]):
                is_valid = True
        else:
            if num_str != "":
                if is_valid:
                    num_result += int(num_str)
                num_str = ""
                is_valid = False
    if num_str != "" and is_valid is True:
        num_result += int(num_str)
    return num_result


if __name__ == "__main__":
    result = 0
    with open("inputs/input3.txt", "r") as f:
        lines = f.readlines()
        empty_line = "".join("." for _ in range(len(lines[0])))  # full dots
        result += process_line(empty_line, lines[0], lines[1])  # first line
        for i in range(1, len(lines) - 1):
            result += process_line(lines[i - 1], lines[i], lines[i + 1])
        result += process_line(
            lines[len(lines) - 2], lines[len(lines) - 1], empty_line
        )  # last line
    print(result)

""" THIS IS PART 2, commented for now
gears = {}


def process_line(previous: str, current: str, next: str, linenumber: int):
    global gears
    previous = "." + previous[:-1] + "."
    current = "." + current[:-1] + "."
    next = "." + next[:-1] + "."
    num_str = ""
    gear_num = None
    for i, char in enumerate(current[1:-1]):
        i = i + 1
        if char.isdigit():
            num_str = num_str + char
            # upper elements
            if previous[i - 1] == "*":
                gear_num = (linenumber - 1, i - 1)
            elif previous[i] == "*":
                gear_num = (linenumber - 1, i)
            elif previous[i + 1] == "*":
                gear_num = (linenumber - 1, i + 1)
            # lower elements
            elif next[i - 1] == "*":
                gear_num = (linenumber + 1, i - 1)
            elif next[i] == "*":
                gear_num = (linenumber + 1, i)
            elif next[i + 1] == "*":
                gear_num = (linenumber + 1, i + 1)
            # left and right
            elif current[i - 1] == "*":
                gear_num = (linenumber, i - 1)
            elif current[i + 1] == "*":
                gear_num = (linenumber, i + 1)
        elif gear_num is not None:
            if gear_num not in gears.keys():
                gears[gear_num] = [num_str]
            else:
                gears[gear_num].append(num_str)
            gear_num = None
            num_str = ""
        else:
            num_str = ""
    if gear_num is not None:
        if gear_num not in gears.keys():
            gears[gear_num] = [num_str]
        else:
            gears[gear_num].append(num_str)


if __name__ == "__main__":
    result = 0
    with open("inputs/input3.txt", "r") as f:
        lines = f.readlines()
        empty_line = "." * (len(lines[0]))  # full dots
        process_line(empty_line, lines[0], lines[1], 0)  # first line
        for i in range(1, len(lines) - 1):
            process_line(lines[i - 1], lines[i], lines[i + 1], i)
        process_line(
            lines[len(lines) - 2], lines[len(lines) - 1], empty_line, len(lines) - 1
        )  # last line
    for v in gears.values():
        if len(v) == 2:
            result += int(v[0]) * int(v[1])
    print(result)

"""
