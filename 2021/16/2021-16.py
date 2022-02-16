# https://adventofcode.com/2021/day/16


hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

type_label = {
    0: "sum",
    1: "x",
    2: "min",
    3: "max",
    4: "litteral",
    5: ">",
    6: "<",
    7: "="}


class Packet:
    def __init__(self, v, t):
        self.v = v
        self.t = t
        self.c = []

    def add_child(self, c):
        self.c.append(c)

    def version(self):
        return self.v

    def type(self):
        return self.t

    def children(self):
        return self.c

    def __str__(self):
        s = [f"{type_label[self.t]}("]
        sub = []
        for c in self.children():
            sub.append(f"{c}")
        s.append(",".join(sub))
        s.append(")")
        return "".join(s)


class Operator(Packet):
    def __init__(self, v, t):
        super().__init__(v, t)


class Litteral(Packet):
    def __init__(self, v, t, val):
        super().__init__(v, t)
        self.val = val

    def value(self):
        return self.val

    def __str__(self):
        return str(self.value())


def hexa_to_bin(hexa):
    return "".join([hex_to_bin[c] for c in hexa])


def load(file):
    with open(file) as f:
        return hexa_to_bin(f.readline()[:-1])


def part1(file):
    bin = load(file)
    p, remains = parse(bin)
    print(f"sum: {sum_version(p)}")


def sum_version(p):
    res = p.version()
    for c in p.children():
        res += sum_version(c)
    return res


def eval(p):
    t = p.type()
    if t == 0:  # sum
        return sum([eval(c) for c in p.children()])
    elif t == 1:  # product
        prod = 1
        for c in p.children():
            prod *= eval(c)
        return prod
    elif t == 2:  # min
        return min([eval(c) for c in p.children()])
    elif t == 3:  # max
        return max([eval(c) for c in p.children()])
    elif t == 4:  # literals
        return p.value()
    elif t == 5:  # >
        return 1 if eval(p.children()[0]) > eval(p.children()[1]) else 0
    elif t == 6:  # <
        return 1 if eval(p.children()[0]) < eval(p.children()[1]) else 0
    elif t == 7:  # =
        return 1 if eval(p.children()[0]) == eval(p.children()[1]) else 0


def parse(bin):
    version = int(bin[0:3], 2)
    type = int(bin[3:6], 2)
    if type == 4:  # litteral
        last = False
        idx = 6
        bin_val = []
        while not last:
            last = (bin[idx] == "0")
            bin_val.append(bin[idx + 1: idx + 5])
            idx += 5
        val = int("".join(bin_val), 2)
        return Litteral(version, type, val), bin[idx:]
    else:  # operator
        op = Operator(version, type)
        length_type_id = bin[6]
        if length_type_id == "0":  # 15 bits for length
            length = int(bin[7:22], 2)
            children_end_idx = 22 + length
            remains = bin[22:children_end_idx]
            while len(remains) > 0:
                child, remains = parse(remains)
                op.add_child(child)
            return op, bin[children_end_idx:]
        else:  # nb packets
            count = int(bin[7:18], 2)
            remains = bin[18:]
            for _ in range(0, count):
                child, remains = parse(remains)
                op.add_child(child)
            return op, remains


def part2(hexa):
    p, remains = parse(hexa_to_bin(hexa))
    print(f"{hexa}: {p} = {eval(p)}")


# part1("sample0a.txt")
# print("")
# part1("sample0b.txt")
# print("")
# part1("sample0c.txt")
# print("")
# part1("sample1.txt")
# print("")
# part1("sample2.txt")
# print("")
# part1("sample3.txt")
# print("")
# part1("sample4.txt")
# print("")
# part1("input.txt")

part2("C200B40A82")
part2("04005AC33890")
part2("880086C3E88112")
part2("CE00C43D881120")
part2("D8005AC2A8F0")
part2("F600BC2D8F")
part2("9C005AC2F8F0")
part2("9C0141080250320F1802104A08")

p, remains = parse(load("input.txt"))
print(f"{p} = {eval(p)}")
