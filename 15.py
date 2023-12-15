from collections import OrderedDict


def p1(f):
    strs = f.read().split(",")
    res = 0
    for str in strs:
        current_val = 0
        for char in str:
            current_val += ord(char)
            current_val *= 17
            current_val %= 256
        res += current_val
    return res


def p2(f):
    strs = f.read().split(",")
    res = 0
    boxes = [OrderedDict() for _ in range(256)]
    for str in strs:
        if "=" in str:
            label, focal_len = str.split("=")[0], int(str.split("=")[1])
        else:
            label = str.split("-")[0]
        box = 0
        for char in label:
            box += ord(char)
            box *= 17
            box %= 256
        if "=" in str:
            boxes[box][label] = focal_len
        else:
            for box_ in boxes:
                if label in box_.keys():
                    box_.pop(label)
    for i, box in enumerate(boxes):
        for j, (k, v) in enumerate(box.items()):
            res += (i + 1) * (j + 1) * v

    return res


if __name__ == "__main__":
    with open("inputs/input15.txt") as f:
        print(p2(f))
