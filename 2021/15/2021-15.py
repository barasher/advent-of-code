# https://adventofcode.com/2021/day/15
import sys
import time


def load(file):
    with open(file) as f:
        grid = {}
        i = 0
        for l in f.readlines():
            for j in range(0, len(l[:-1])):
                grid[(i, j)] = int(l[j])
            i += 1
        return grid


def run(grid):
    exit_l = max(l for l, _ in grid.keys())
    exit_c = max(c for _, c in grid.keys())
    exit = (exit_l, exit_c)
    weights = {(0, 0): 0}

    while True:
        min_w = min(weights.values())
        min_k = None
        for k, w in weights.items():
            if w == min_w:
                min_k = k

        # breaking condition
        if min_k == exit:
            break

        # neighbors update
        for n in [(min_k[0] - 1, min_k[1]), (min_k[0] + 1, min_k[1]), (min_k[0], min_k[1] - 1),
                  (min_k[0], min_k[1] + 1)]:
            if n in grid:
                weights[n] = min(weights.get(n, sys.maxsize), weights.get(min_k) + grid[n])
        del weights[min_k]
        del grid[min_k]

    print(weights[exit])


def part1(file):
    run(load(file))


def display(grid):
    lm = max(l for l, _ in grid.keys())
    cm = max(c for _, c in grid.keys())
    for l in range(0, lm + 1):
        for c in range(0, cm + 1):
            print(f"{grid[(l, c)]} ", end="")
        print("")


def expand(grid):
    lm = max(l for l, _ in grid.keys())
    cm = max(c for _, c in grid.keys())
    new_grid = {}
    for li in range(0, 5):
        for ci in range(0, 5):
            for k, v in grid.items():
                new_val = v + ci + li
                if new_val > 9:
                    new_val = new_val % 10 + 1
                new_grid[(k[0] + li * (lm + 1), k[1] + ci * (cm + 1))] = new_val
    return new_grid


def part2(file):
    grid = load(file)
    expanded = expand(grid)
    run(expanded)


part2("input.txt")
