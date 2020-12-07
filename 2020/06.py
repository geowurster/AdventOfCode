from functools import reduce
import itertools as it
import operator as op
import string


def load_input():

    out = []
    with open('05.txt') as f:

        for k, values in it.groupby((l.strip() for l in f), bool):
            if not k:
                continue
            else:
                out.append(tuple(tuple(v) for v in values))

    return tuple(out)


def part1(answers):

    total = 0
    for group in answers:
        unique = set(it.chain.from_iterable(group))
        filtered = unique & set(string.ascii_letters)
        total += len(filtered)

    return total


def part2(answers):

    total = 0
    for group in answers:
        all_yes = reduce(op.iand, map(set, group))
        all_yes = all_yes & set(string.ascii_letters)
        total += len(all_yes)

    return total


data = load_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
