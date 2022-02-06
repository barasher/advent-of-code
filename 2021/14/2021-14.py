# https://adventofcode.com/2021/day/14

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


part1("input.txt", 10)
