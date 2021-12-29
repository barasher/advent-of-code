# https://adventofcode.com/2021/day/3

with open("input.txt") as f:
    data = f.readlines()

num_digits = len(data[0][:-1])
num_records = len(data)


def gamma_epsilon_bits(digit):
    s = sum([int(v[digit]) for v in data])
    res = ("0", "1")
    if s >= (num_records / 2):
        res = ("1", "0")
    return res


gamma, epsilon = "", ""
for cur_digit in range(0, num_digits):
    geb = gamma_epsilon_bits(cur_digit)
    gamma += geb[0]
    epsilon += geb[1]

print(f"gamma: b{gamma} <-> {int(gamma, 2)}")
print(f"epsilon: b{epsilon} <-> {int(epsilon, 2)}")
print(f"part1: {int(gamma, 2) * int(epsilon, 2)}")