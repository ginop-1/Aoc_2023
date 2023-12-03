def is_set_valid(set: str):
    values = [s.strip() for s in set.split(",")]
    for val in values:
        num, color = val.split(" ")
        num = int(num)
        if (num > 13 and color == "green"):
            return False
        elif (num >12 and color=="red"):
            return False
        elif (num>14 and color == "blue"):
            return False
    return True

def min_cubes_power(game: str):
    mins = {"red":-1, "green":-1, "blue": -1}
    for set in game.split(": ")[1].split(";"):
        values = [s.strip() for s in set.split(",")]
        for val in values:
            num, color = val.split(" ")
            num = int(num)
            if (mins[color] == -1 or num > mins[color]):
                mins[color] = num
    result = 1
    for v in mins.values():
        result *= v
    return result
            

if __name__ == "__main__":
    result = 0
    with open("input2.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            # valid=True
            # for set in line.split(": ")[1].split(";"):
                # if not is_set_valid(set.strip()):
                #     valid=False
            result += min_cubes_power(line)
            # if valid:
                # result += i+1
    print(result)