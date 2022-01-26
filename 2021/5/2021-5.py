# https://adventofcode.com/2021/day/5
import re


def load(file):
    with open(file) as f:
        data = f.readlines()
    r = re.compile("([^,]*),([^,]*) -> ([^,]*),([^,]*)")
    res = []
    for i in range(0, len(data)):
        captured = r.search(data[i])
        cur = {
            "x1": int(captured.group(1)),
            "y1": int(captured.group(2)),
            "x2": int(captured.group(3)),
            "y2": int(captured.group(4)),
        }
        res.append(cur)
    return res


def display(tab):
    for y in range(0, len(tab)):
        print(tab[y])


def is_diag(seg):
    minx, maxx = min(seg["x1"], seg["x2"]), max(seg["x1"], seg["x2"])
    miny, maxy = min(seg["y1"], seg["y2"]), max(seg["y1"], seg["y2"])
    return maxx - minx == maxy - miny


def path(seg, with_diag):
    if seg["x1"] == seg["x2"]:
        return [(seg["x1"], y) for y in range(min(seg["y1"], seg["y2"]), max(seg["y1"], seg["y2"]) + 1)]
    elif seg["y1"] == seg["y2"]:
        return [(x, seg["y1"]) for x in range(min(seg["x1"], seg["x2"]), max(seg["x1"], seg["x2"]) + 1)]
    elif with_diag and is_diag(seg):
        res = []
        xs = vals_between(seg["x1"], seg["x2"])
        ys = vals_between(seg["y1"], seg["y2"])
        for i in range(0, len(xs)):
            res.append((xs[i], ys[i]))
        return res


def vals_between(v1, v2):
    if v1 < v2:
        return range(v1, v2 + 1)
    else:
        return range(v1, v2 - 1, -1)


def part(file, with_diag):
    data = load(file)

    x_max, y_max = 0, 0
    for i in range(0, len(data)):
        cur = data[i]
        x_max = max(x_max, cur["x1"], cur["x2"])
        y_max = max(y_max, cur["y1"], cur["y2"])
    tab = [[0 for x in range(0, x_max + 1)] for y in range(0, y_max + 1)]

    for i in range(0, len(data)):
        p = path(data[i], with_diag)
        for j in range(0, len(p)):
            tab[p[j][1]][p[j][0]] += 1

    overlaps = 0
    for y in range(0, y_max + 1):
        for x in range(0, x_max + 1):
            if tab[y][x] > 1:
                overlaps += 1

    print(overlaps)


def part1(file):
    part(file, False)


def part2(file):
    part(file, True)


part2("input.txt")
