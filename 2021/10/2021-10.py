# https://adventofcode.com/2021/day/10


def load(file):
    with open(file) as f:
        return [[int(c) for c in l[:-1]] for l in f.readlines()]


matchs = {"[": "]", "(": ")", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def match(o, c):
    return matchs[o] == c


def score(l):
    stack = []
    for c in l:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            poped = stack.pop()
            if not match(poped, c):
                return scores[c]
    return 0


def part1(file):
    with open(file) as f:
        res = 0
        for l in f.readlines():
            res += score(l[:-1])
        print(res)


part1("input.txt")
