import math


class Node:
    def __init__(self, raw: str) -> None:
        self.value = raw.split(" = ")[0]
        self.nearby = raw.split(" = ")[1][1:-1].split(", ")
        pass


def getNodeIndex(target, nodes):
    for i, node in enumerate(nodes):
        if target == node.value:
            return i


def p1(f):
    lines = f.read().splitlines()
    steps, nodes = lines[0], lines[2:]
    nodes = [Node(node) for node in nodes]
    n_steps = 0
    curr_node = nodes[getNodeIndex("AAA", nodes)]
    while True:
        if curr_node.value == "ZZZ":
            break
        for step in steps:
            if step == "L":
                curr_node = nodes[getNodeIndex(curr_node.nearby[0], nodes)]
            else:
                curr_node = nodes[getNodeIndex(curr_node.nearby[1], nodes)]
            n_steps += 1
    return n_steps


def p2(f):
    lines = f.read().splitlines()
    steps, nodes = lines[0], lines[2:]
    nodes = [Node(node) for node in nodes]
    starting_nodes = [node for node in nodes if node.value[2] == "A"]
    n_steps = [0 for _ in range(len(starting_nodes))]
    for i, node in enumerate(starting_nodes):
        curr_node = node
        while True:
            if curr_node.value[2] == "Z":
                break
            for step in steps:
                if step == "L":
                    curr_node = nodes[getNodeIndex(curr_node.nearby[0], nodes)]
                else:
                    curr_node = nodes[getNodeIndex(curr_node.nearby[1], nodes)]
                n_steps[i] += 1
    return math.lcm(*n_steps)


if __name__ == "__main__":
    with open("input8.txt") as f:
        print(p2(f))
