# https://adventofcode.com/2021/day/12

def load(file):
    with open(file) as f:
        raw = [l[:-1].split("-") for l in f.readlines()]
        edges = {}
        for elt in raw:
            if elt[0] not in edges:
                edges[elt[0]] = []
            if elt[1] not in edges:
                edges[elt[1]] = []
            edges[elt[0]].append(elt[1])
            edges[elt[1]].append(elt[0])
        return edges


def part1(file):
    edges = load(file)
    paths = []
    visited = []
    explore(edges, "", "start", paths, visited)
    print(len(paths))


def explore(edges, cur_path, cur_node, paths, visited_nodes):
    if cur_node.islower():
        if cur_node in visited_nodes:
            return
        visited_nodes.append(cur_node)

    cur_path = f"{cur_path},{cur_node}"

    for next in edges[cur_node]:
        if next == "end":
            paths.append(f"{cur_path},end")
            continue
        explore(edges, cur_path, next, paths, visited_nodes[:])


part1("input.txt")