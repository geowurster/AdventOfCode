from collections import deque


def load_input():
    bags = {}
    with open('07.txt') as f:
        for line in (l.strip() for l in f):
            color, contains_text = line.split('bags contain')
            color = color.strip()
            if 'no other bags' in contains_text.strip():
                contains = None
            else:
                contains = []
                for child in contains_text.split(','):
                    child = child.strip()
                    child_count, child_color = child.split(' ', 1)
                    child_count = int(child_count)
                    child_color = child_color.split('bag')[0].strip()
                    contains.extend(child_color for _ in range(child_count))

            bags[color] = contains

    return bags


def bag_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for node in graph[at] or []:
            if node not in dist:
                dist[node] = [dist[at], node]
                q.append(node)
    return dist.get(end)


def paths_containing(graph, item):

    """Graph paths containing ``item``."""

    out = []
    for k in (k for k in graph if k != item):
        path = bag_path(graph, k, item)
        if path:
            out.append(path)

    return out


def part1(graph):
    return len(paths_containing(graph, 'shiny gold'))


def part2(graph):

    start = 'shiny gold'

    count = 0
    q = deque([start])
    while q:
        bag = q.popleft()
        contains = graph[bag]
        if contains:
            count += len(contains)
            q.extend(contains)

    return count


data = load_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
