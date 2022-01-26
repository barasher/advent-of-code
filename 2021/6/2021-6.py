# https://adventofcode.com/2021/day/6

def load(file):
    with open(file) as f:
        data = f.readlines()
    return [int(v) for v in data[0][:-1].split(",")]


def part1(file, iter):
    vals = load(file)
    for i in range(0, iter):
        for j in range(0, (len(vals))):
            if vals[j] == 0:
                vals.append(8)
                vals[j] = 6
            else:
                vals[j] -= 1
    print(len(vals))


def part2(file, iter):
    tab = [0 for i in range(0, 9)]
    vals = load(file)
    for i in range(0, len(vals)):
        tab[vals[i]] += 1
    for i in range(0, iter):
        z = tab.pop(0)
        tab[6] += z
        tab.append(z)
    print(sum(tab))


part2("input.txt", 256)
