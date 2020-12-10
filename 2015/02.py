from functools import reduce
import operator as op


def parse_input():
    with open('02.txt') as f:
        return tuple(tuple(map(int, l.split('x'))) for l in f)


def part1(presents):

    total = 0
    for l, w, h in presents:
        area_3_faces = ((l * w), (w * h), (h * l))
        area = 2 * sum(area_3_faces)
        slack = min(area_3_faces)
        total += area + slack

    return total


def part2(presents):

    total = 0
    for l, w, h in presents:
        side1, side2 = sorted((l, w, h))[:2]
        ribbon = (side1 * 2) + (side2 * 2)
        bow = reduce(op.imul, (l, w, h))
        total += ribbon + bow
    return total


data = parse_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
