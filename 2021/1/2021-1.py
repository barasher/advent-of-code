# https://adventofcode.com/2021/day/1

with open("input.txt") as f:
    measures = [int(c) for c in f.readlines()]

last = measures[0]
count = 0
for i in range(1, len(measures)):
    cur = measures[i]
    if cur > last:
        count += 1
    last = cur
print(f"part1: {count}")

last = sum(measures[:3])
count = 0
for i in range(1, len(measures) - 2):
    cur = sum(measures[i:i + 3])
    if cur > last:
        count += 1
    last = cur
print(f"part2: {count}")
