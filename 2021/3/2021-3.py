# https://adventofcode.com/2021/day/3

with open("input.txt") as f:
    data = f.readlines()

num_digits = len(data[0][:-1])
num_records = len(data)


def gamma_epsilon_bits(d, i):
    s = sum([int(v[i]) for v in d])
    res = ("0", "1")
    if s >= (len(d) / 2):
        res = ("1", "0")
    return res


gamma, epsilon = "", ""
for cur_digit in range(0, num_digits):
    geb = gamma_epsilon_bits(data, cur_digit)
    gamma += geb[0]
    epsilon += geb[1]

print(f"gamma: b{gamma} <-> {int(gamma, 2)}")
print(f"epsilon: b{epsilon} <-> {int(epsilon, 2)}")
print(f"part1: {int(gamma, 2) * int(epsilon, 2)}")

print("")


def maj(d, i):
    if i >= num_digits or len(d) == 1:
        return d
    s = sum([int(v[i]) for v in d])
    ma = "1" if s >= (len(d) / 2) else "0"
    sub = [sel for sel in d if sel[i] == ma]
    return maj(sub, i + 1)


def mino(d, i):
    if i >= num_digits or len(d) == 1:
        return d
    s = sum([int(v[i]) for v in d])
    mi = "0" if s >= (len(d) / 2) else "1"
    sub = [sel for sel in d if sel[i] == mi]
    return mino(sub, i + 1)


ogr = maj(data, 0)[0][:-1]
print(f"ogr: b{ogr} <-> {int(ogr, 2)}")
csr = mino(data, 0)[0][:-1]
print(f"csr: b{csr} <-> {int(csr, 2)}")
print(f"part2: {int(ogr, 2)*int(csr, 2)}")