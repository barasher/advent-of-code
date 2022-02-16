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


class Operator(Packet):
    def __init__(self, v, t):
        super().__init__(v, t)


class Litteral(Packet):
    def __init__(self, v, t, val):
        super().__init__(v, t)
        self.value = val

    def value(self):
        return self.value()


def load(file):
    with open(file) as f:
        hexa = f.readline()[:-1]
        bin_seq = "".join([hex_to_bin[c] for c in hexa])
        return bin_seq


def part1(file):
    bin = load(file)
    p, remains = parse(bin)
    print(f"sum: {sum_version(p)}")


def sum_version(p):
    res = p.version()
    for c in p.children():
        res += sum_version(c)
    return res


def parse(bin):
    print(f"### {bin}")
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
        print(f"Litteral: {val}")
        return Litteral(version, type, val), bin[idx:]
    else:  # operator
        op = Operator(version, type)
        length_type_id = bin[6]
        print(f"Operator {type}")
        if length_type_id == "0":  # 15 bits for length
            length = int(bin[7:22], 2)
            print(f"length: {length}")
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
part1("input.txt")
