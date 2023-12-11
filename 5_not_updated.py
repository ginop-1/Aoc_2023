def p1(f):
    lines = f.readlines()
    seeds = [int(seed) for seed in lines[0].split()[1:]]
    next_step = [seed for seed in seeds]
    for line in lines[1:]:
        if line == "\n":
            seeds = next_step.copy()
        if len(line.split()) != 3:  # x-to-x map, skip
            continue
        dst_start, src_start, range_len = map(int, line.split())
        for ix, seed in enumerate(seeds):
            if seed > src_start and seed < src_start + range_len - 1:
                next_step[ix] = seed - src_start + dst_start
    return min(next_step)


def p2(f):
    lines = f.readlines()
    seeds = []
    # generate all seeds
    raw_first_line = [int(seed) for seed in lines[0].split()[1:]]
    for i in range(0, len(raw_first_line), 2):
        seeds.append([raw_first_line[i], raw_first_line[i + 1]])
    next_step = seeds.copy()
    for line in lines[1:]:
        if line == "\n":
            seeds = next_step.copy()
        if len(line.split()) != 3:  # x-to-x map, skip
            continue
        dst_start, src_start, range_len = map(int, line.split())
        for ix, seed in enumerate(seeds):
            # too small or too big
            if seed[0] + seed[1] < src_start or seed[0] >= src_start + range_len:
                continue
            # check for left part
            if seed[0] < src_start:
                new_seed = [seed[0], (src_start - 1) - seed[0]]
                seeds.append(new_seed.copy())
                next_step.append(new_seed.copy())
            # check for right part
            if seed[0] + seed[1] > src_start + range_len:
                new_seed = [
                    src_start + range_len,
                    seed[0] + seed[1] - (src_start + range_len),
                ]
                seeds.append(new_seed.copy())
                next_step.append(new_seed.copy())
            next_step[ix][0] = seed[0] - src_start + dst_start
    return min(location[0] for location in next_step)


if __name__ == "__main__":
    with open("inputs/input5.txt") as f:
        print(p2(f))

# 15880236
