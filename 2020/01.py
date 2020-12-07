from functools import reduce
import operator as op
import itertools as it


target = 2020


def load_input():
    with open('01.txt') as f:
        return tuple(map(int, f))


def solve(expenses, count):

    for values in it.combinations(expenses, count):
        if sum(values) == target:
            return values, reduce(op.imul, values)
    else:
        raise ValueError("Did not find a match")


data = load_input()


print("Part 1: {} {}".format(*solve(data, 2)))
print("Part 2: {} {}".format(*solve(data, 3)))
