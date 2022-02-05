# https://adventofcode.com/2021/day/13
import re


def load(file):
    with open(file) as f:
        cells = []
        folds = []
        r = re.compile("fold along (.)=(.*)$")
        for l in f.readlines():
            s = l.split(",")
            if len(s) == 2:
                cells.append((int(s[0]), int(s[1][:-1])))
                continue
            g = r.search(l)
            if g is not None:
                folds.append((g.group(1), int(g.group(2))))

        grid = []
        x_max = max([t[0] for t in cells])
        y_max = max([t[1] for t in cells])
        for y in range(0, y_max + 1):
            grid.append(["." for i in range(0, x_max + 1)])

        for c in cells:
            grid[c[1]][c[0]] = "#"

        return grid, folds


def display(grid):
    for l in grid:
        print("".join(l))


def fold_x(grid, x):
    res = []
    for line in grid:
        res.append(line[0:x])

    for y in range(0, len(grid)):
        for i in range(0, x):
            if grid[y][x + i + 1] == "#":
                res[y][x - i - 1] = "#"
    return res


def fold_y(grid, y):
    res = grid[0:y]
    for i in range(0, y):
        for x in range(0, len(res[0])):
            if grid[y + 1 + i][x] == "#":
                res[y - 1 - i][x] = "#"
    return res


def fold(grid, folds):
    for f in folds:
        if f[0] == "y":
            grid = fold_y(grid, f[1])
        elif f[0] == "x":
            grid = fold_x(grid, f[1])
    return grid


def part1(file):
    grid, folds = load(file)
    grid = fold(grid, folds[0:1])
    count = 0
    for l in grid:
        for c in l:
            if c == "#":
                count += 1
    print(count)


def part2(file):
    grid, folds = load(file)
    grid = fold(grid, folds)
    display(grid)


part2("input.txt")
