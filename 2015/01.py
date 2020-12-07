import operator as op


def load_input():
    with open('01.txt') as f:
        return f.read().strip()


def part1(instructions):
    return instructions.count('(') - instructions.count(')')


def part2(instructions):

    # Convert instruction characters to integers that can be
    # operated on directly
    mapping = {'(': 1, ')': -1}
    values = map(lambda x: mapping[x], instructions)

    position = 0
    for idx, v in enumerate(values, 1):
        position += v
        if position < 0:
            return idx
    else:
        raise RuntimeError(f"did not enter basement")


data = load_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
