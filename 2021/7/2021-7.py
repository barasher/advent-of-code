# https://adventofcode.com/2021/day/7

def load(file):
    with open(file) as f:
        data = f.readlines()
    return [int(v) for v in data[0][:-1].split(",")]


def part1(file):
    vals = load(file)
    mi, ma = min(vals), max(vals)
    minpath = len(vals) * ma
    for i in range(mi, ma + 1):
        path = 0
        for j in range(0, len(vals)):
            path += abs(i - vals[j])
        minpath = min(minpath, path)
    print(minpath)


part1("input.txt")
