from collections import deque
import itertools as it


def load_input():
    with open('09.txt') as f:
        return tuple(map(int, f))


def chunker(stream, size):
    stream = (i for i in stream)
    while True:
        try:
            preamble = tuple(it.islice(stream, size))
            value = next(stream)
            if len(preamble) != size:
                raise StopIteration
        except StopIteration:
            raise RuntimeError("stream exhausted")

        yield preamble, value
        stream = it.chain(preamble[1:], [value], stream)


def part1(stream):
    size = 25
    for preamble, value in chunker(stream, size):
        if not any(sum(i) == value for i in it.combinations(preamble, 2)):
            return value
    else:
        raise RuntimeError("all data valid")


def part2(stream):

    value = part1(stream)

    candidates = stream[:stream.index(value)]
    for min_idx in range(len(candidates)):
        for max_idx in range(min_idx + 1, len(candidates)):
            chunk = candidates[min_idx:max_idx]
            if sum(chunk) == value:
                return min(chunk) + max(chunk)
    else:
        raise RuntimeError("failure :(")


data = load_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
