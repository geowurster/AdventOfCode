from functools import reduce
import operator as op


def load_input():
    with open('03.txt') as f:
        return [list(l.strip()) for l in f]


def part1(slope, cstep, rstep):

    ridx = 0
    cidx = 0

    # Ensure all rows are the same width
    assert len(set(len(r) for r in slope)) == 1
    width = len(slope[0])

    trees = 0
    while ridx + 1 != len(slope):

        cidx += cstep
        ridx += rstep

        # Wrap columns to stay on single slope instance
        if cidx >= width:
            cidx -= width

        if slope[ridx][cidx] == '#':
            trees += 1

    return trees


def part2(slope):

    cstep_rstep = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )

    trees = []
    for cstep, rstep in cstep_rstep:
        trees.append(part1(slope, cstep=cstep, rstep=rstep))

    return reduce(op.imul, trees)


data = load_input()


print(f"Part 1: {part1(data, cstep=3, rstep=1)}")
print(f"Part 2: {part2(data)}")
