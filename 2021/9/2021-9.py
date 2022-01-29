# https://adventofcode.com/2021/day/9


def load(file):
    with open(file) as f:
        return [[int(c) for c in l[:-1]] for l in f.readlines()]


def neighbors_coords(tab, l, c):
    nv = [neighbors_coord(tab, l, c - 1),
          neighbors_coord(tab, l, c + 1),
          neighbors_coord(tab, l + 1, c),
          neighbors_coord(tab, l - 1, c)]
    return [c for c in nv if c != None]


def neighbors_coord(tab, l, c):
    if 0 <= l < len(tab) and 0 <= c < len(tab[l]):
        return (l, c)
    return None


def is_low(tab, l, c):
    return tab[l][c] < min([tab[nc[0]][nc[1]] for nc in neighbors_coords(tab, l, c)])


def val(tab, l, c):
    if 0 <= l < len(tab) and 0 <= c < len(tab[l]):
        return tab[l][c]
    return None


def part1(file):
    tab = load(file)
    lines = len(tab)
    cols = len(tab[0])
    risk = 0
    for l in range(0, lines):
        for c in range(0, cols):
            if is_low(tab, l, c):
                risk += (tab[l][c] + 1)
    print(risk)


visited = []


def part2(file):
    tab = load(file)
    lines = len(tab)
    cols = len(tab[0])
    areas = []
    for l in range(0, lines):
        for c in range(0, cols):
            if is_low(tab, l, c):
                explore(tab, l, c)
                areas.append( len(visited))
                visited.clear()
    areas.sort()
    print(areas[-1] * areas[-2] * areas[-3])

def explore(tab, l, c):
    if (l, c) not in visited:
        visited.append((l, c))
    for coord in neighbors_coords(tab, l, c):
        if coord not in visited and tab[coord[0]][coord[1]] != 9:
            visited.append(coord)
            explore(tab, coord[0], coord[1])


part2("input.txt")
