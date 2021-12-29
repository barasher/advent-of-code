# https://adventofcode.com/2021/day/2

with open("input.txt") as f:
    actions = [c[:-1].split(" ") for c in f.readlines()]

position, depth = 0, 0
for action in actions:
    if action[0] == "up":
        depth -= int(action[1])
    elif action[0] == "down":
        depth += int(action[1])
    elif action[0] == "forward":
        position += int(action[1])
    else:
        print(f"unsupported action: {action}")
print(f"depth: {depth}, position: {position}")
print(f"result1: {depth * position}")

# actions = [["forward", "5"], ["down", "5"], ["forward", "8"], ["up", "3"], ["down", "8"], ["forward", "2"]]
position, depth, aim = 0, 0, 0
for action in actions:
    if action[0] == "up":
        aim -= int(action[1])
    elif action[0] == "down":
        aim += int(action[1])
    elif action[0] == "forward":
        position += int(action[1])
        if aim != 0:
            depth += (aim * int(action[1]))
    else:
        print(f"unsupported action: {action}")
print(f"depth: {depth}, position: {position}, aim: {aim}")
print(f"result1: {depth * position}")
