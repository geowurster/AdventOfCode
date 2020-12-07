import operator as op


def load_input():

    # Parse input data into a friendly format.
    # Given a line like:
    #   15-16 f: ffffffffffffffhf
    # parse into a tuple like:
    #   ((15, 16), "f", ffffffffffffffhf)
    policies = []
    with open('02.txt') as f:
        for line in f:
            policy, password = line.split(':')
            password = password.strip()
            mm, character = policy.split()
            v1, v2 = map(int, mm.split('-'))
            policies.append(
                ((v1, v2), character, password)
            )

    return policies


def part1(policies):

    valid = 0
    for (minimum, maximum), character, password in policies:
        count = password.count(character)
        if minimum <= count <= maximum:
            valid += 1

    return valid


def part2(policies):

    valid = 0
    for (idx1, idx2), character, password in policies:

        # Convert 1-based indexing to 0
        idx1 -= 1
        idx2 -= 1

        try:
            v1 = password[idx1]
        except IndexError:
            v1 = None
        try:
            v2 = password[idx2]
        except IndexError:
            v2 = None

        if {v1, v2} == {character}:
            continue
        elif v1 == character or v2 == character:
            valid += 1

    return valid


data = load_input()
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
