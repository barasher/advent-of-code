# https://adventofcode.com/2021/day/7
import sys


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


def part2(file):
    vals = load(file)
    mi, ma = min(vals), max(vals)
    minpath = sys.maxsize
    for i in range(mi, ma + 1):
        path = 0
        for j in range(0, len(vals)):
            path += gaz(abs(i - vals[j]))
        print(f"{i}: {path}")
        minpath = min(minpath, path)
    print(minpath)


g = dict()


def gaz(dist):
    if dist not in g:
        g[dist] = sum([i for i in range(1, dist + 1)])
    return g[dist]


part2("input.txt")
