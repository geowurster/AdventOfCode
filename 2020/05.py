import itertools as it


def load_input():
    with open('05.txt') as f:
        return tuple(l.strip() for l in f)


def bisect(steps, rng):
    for step in steps:
        delta = rng.stop - rng.start
        # Lower half: front and left
        if step in 'FL':
            rng = range(rng.start, rng.stop - (delta // 2))
        # Upper half: back and right
        elif step in 'BR':
            rng = range(rng.start + (delta // 2), rng.stop)
        else:
            raise ValueError(f"invalid step: {step}")

    assert rng.start + 1 == rng.stop, rng
    return rng.start


def passes_to_ids(passes):

    row_range = range(0, 128)
    col_range = range(0, 8)

    for p in passes:
        row_steps = p[:-3]
        col_steps = p[-3:]
        row = bisect(row_steps, row_range)
        col = bisect(col_steps, col_range)

        seat_id = (row * 8) + col
        yield seat_id


def part1(passes):

    maximum = None
    for seat_id in passes_to_ids(passes):
        if maximum is None or seat_id > maximum:
            maximum = seat_id

    return maximum


def part2(passes):

    passes = list(passes)
    expected_ids = range(part1(passes))
    actual_ids = sorted(passes_to_ids(passes))
    missing_ids = sorted(set(expected_ids) - set(actual_ids))

    min_id = actual_ids[0]
    max_id = actual_ids[-1]
    for missing in missing_ids:

        # We know neighboring seats must exist
        if missing in (min_id, max_id):
            continue

        # A neighboring seat is also missing, but we know neighbors
        # must be present.
        elif missing - 1 in missing_ids or missing + 1 in missing_ids:
            continue

        else:
            return missing


data = load_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
