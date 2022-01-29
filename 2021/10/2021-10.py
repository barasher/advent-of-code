# https://adventofcode.com/2021/day/10


def load(file):
    with open(file) as f:
        return [[int(c) for c in l[:-1]] for l in f.readlines()]


matchs = {"[": "]", "(": ")", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
compl_scores = {")": 1, "]": 2, "}": 3, ">": 4}


def match(o, c):
    return matchs[o] == c


def compile(l):
    stack = []
    for c in l:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            poped = stack.pop()
            if not match(poped, c):
                return (stack, scores[c])
    return (stack, 0)


def part1(file):
    with open(file) as f:
        res = 0
        for l in f.readlines():
            res += compile(l[:-1])[1]
        print(res)

def part2(file):
    with open(file) as f:
        s=[]
        for l in f.readlines():
            stack, score = compile(l[:-1])
            if score == 0 and len(stack)>0:
                sum = 0
                while len(stack) > 0:
                    c = matchs[stack.pop()]
                    sum = (sum * 5) + compl_scores[c]
                s.append(sum)
        s.sort()
        print(s[int(len(s)/2)])

part2("input.txt")
