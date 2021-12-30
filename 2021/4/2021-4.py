# https://adventofcode.com/2021/day/4

def print_card(c):
    for line in c:
        print(line)


def wins(c):
    for i in range(0, 5):
        if sum(c[i]) == -5:
            return True
        if sum([x[i] for x in c]) == -5:
            return True
    return False


def score(c, val):
    s = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if c[i][j] != -1:
                s += c[i][j]
    return s * val


def load(file):
    with open(file) as f:
        data = f.readlines()

    vals = [int(v) for v in data[0][:-1].split(",")]

    lines = []
    for i in range(1, len(data)):
        c = [int(v) for v in data[i][:-1].split()]
        if len(c) > 0:
            lines.append(c)
    cards = []
    num_cards = int(len(lines) / 5)
    for i in range(0, num_cards):
        card = []
        for j in range(0, 5):
            card.append(lines[i * 5 + j])
        cards.append(card)

    return (cards, vals)


def play(card, vals):
    step = 0
    for val in vals:
        step += 1
        for r in range(0, 5):
            for c in range(0, 5):
                if card[r][c] == val:
                    card[r][c] = -1
        if wins(card):
            return (step, score(card, val))
    return -1, -1


def part1(file):
    cards, vals = load(file)
    for val in vals:
        for ic in range(0, len(cards)):
            for r in range(0, 5):
                for c in range(0, 5):
                    if cards[ic][r][c] == val:
                        cards[ic][r][c] = -1

            if wins(cards[ic]):
                print_card(cards[ic])
                print(score(cards[ic], val))
                return


def part2(file):
    cards, vals = load(file)
    res = {}
    for card in cards:
        st, sc = play(card, vals)
        if st != -1:
            res[st] = sc
    las = max(k for k in res.keys())
    print(res[las])


file = "input.txt"
part1(file)
print("##########")
part2(file)
