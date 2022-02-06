# https://adventofcode.com/2021/day/14
import math

def load(file):
    with open(file) as f:
        seq = f.readline().strip()
        trans = {}
        for l in f.readlines():
            s = l.strip().split(" -> ")
            if len(s) == 2:
                trans[s[0]] = s[1]
        return seq, trans


def part1(file, iter):
    seq, trans = load(file)

    for it in range(0, iter):
        new = []
        for i in range(0, len(seq) - 1):
            new.append(seq[i])
            new.append(trans[seq[i:i + 2]])
        new.append(seq[-1])
        seq = "".join(new)

    occurences = {}
    for c in set([c for c in seq]):
        occurences[c] = sum([1 for c2 in seq if c2 == c])

    counts = [occ for occ in occurences.values()]
    counts.sort()
    print(counts[-1] - counts[0])


def part2(file, iter):
    seq, trans = load(file)

    duos = {}
    for i in range(0, len(seq) - 1):
        k = seq[i:i + 2]
        duos[k] = duos.get(k, 0) + 1

    for it in range(0, iter):
        new = {}
        for duo, count in duos.items():
            k = duo[0] + trans[duo]
            new[k] = new.get(k, 0) + count
            k = trans[duo] + duo[1]
            new[k] = new.get(k, 0) + count
        duos = new

    counts = {}
    for duo, count in duos.items():
        counts[duo[0]] = counts.get(duo[0], 0) + count
        counts[duo[1]] = counts.get(duo[1], 0) + count

    scores = [math.ceil(count/2) for count in counts.values()]
    scores.sort()
    print(scores[-1] - scores[0])


part2("input.txt", 40)
