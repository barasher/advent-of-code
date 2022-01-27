# https://adventofcode.com/2021/day/8
import re


def part1(file):
    r = re.compile("^.* \\| (.*)$")
    with open(file) as f:
        data = [r.search(l).group(1).split() for l in f.readlines()]
    count = 0
    selected = [2, 4, 3, 7]
    for i in range(0, len(data)):
        count += sum([1 for c in data[i] if len(c) in selected])
    print(count)


part1("input.txt")
