# https://adventofcode.com/2021/day/6

def part1(file, iter):
    with open(file) as f:
        data = f.readlines()
    vals = [int(v) for v in data[0][:-1].split(",")]

    for i in range(0, iter):
        for j in range(0,(len(vals))):
            if vals[j] == 0:
                vals.append(8)
                vals[j]=6
            else:
                vals[j] -= 1

    print(len(vals))

part1("input.txt", 80)