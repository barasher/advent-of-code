# https://adventofcode.com/2021/day/11


def load(file):
    with open(file) as f:
        return [[int(c) for c in l[:-1]] for l in f.readlines()]


def display(grid):
    for line in grid:
        print(line)


def neighbor(lc, cc, l, c):
    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= l + i < lc and 0 <= c + j < cc:
                res.append((l + i, c + j))
    res.remove((l, c))
    return res


def flashing(grid):
    flash = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] > 9:
                flash.append((i, j))
    # print(f"flashing : {flash}")
    return flash

def part1(file, iter):
    grid = load(file)
    lc = len(grid)
    cc = len(grid[0])
    flash_count=0
    for it in range(0, iter):
        # inc
        for l in range(0, lc):
            for c in range(0, cc):
                grid[l][c] += 1
        to_flash = flashing(grid)
        have_flashed = []
        while (len(to_flash) > 0):
            for coord in to_flash:
                have_flashed.append(coord)
                for n in neighbor(lc, cc, coord[0], coord[1]):
                    grid[n[0]][n[1]] += 1
                grid[coord[0]][coord[1]] = 0
            for coord in have_flashed:
                grid[coord[0]][coord[1]] = 0
            to_flash = flashing(grid)
        flash_count+=len(have_flashed)
        # print(f"{it + 1} after flash")
        # display(grid)
    print(flash_count)


part1("input.txt", 100)
