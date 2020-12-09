def parse_input():
    out = []
    with open('08.txt') as f:
        for line in f:
            inst, val = line.strip().split()
            out.append((inst, int(val)))
    return tuple(out)


def execute(idx, acc, op, code):

    """Execute a single opcode."""

    if op == 'nop':
        idx += 1
    elif op == 'acc':
        idx += 1
        acc += code
    elif op == 'jmp':
        idx += code
    else:
        raise ValueError(
            f"invalid opcode at index {idx}: {op} {code}")

    return idx, acc


def part1(opcodes):

    trace = []

    acc = 0
    idx = 0
    while True:

        if idx in trace:
            return acc

        op, code = opcodes[idx]
        newidx, acc = execute(idx, acc, op, code)
        trace.append(idx)
        idx = newidx


def part2(opcodes):

    """Algorithm works like this:

    1. Execute opcodes until recursion is detected.
    2. Given that a single opcode needs to be updated we now know
       that the problem is in an opcode that has already executed.
    3. Step through the trace and examine each previously executed opcode.
       If the operation is `jmp` or `nop` record its index and as a potential
       change to test.
    4. Take the first index to test and apply its change to the input opcodes.
       Record the index and its original value in order to undo this change
       should the experiment prove unsuccessful.
    5. Restart the program.
    6. If the program fully executes then the first opcode was the problem.
       If recursion is detected again then apply another opcode to test and
       go back to ``5``. Repeat this cycle until all tests are exercised.
       If the last test hits recursion then something has gone horribly
       wrong and it is now time to cry!
    """

    # Need mutability
    opcodes = list(opcodes)

    # Track which indexes in 'opcodes' are executed during a given run.
    trace = []

    # Once recursion is hit this stores all of the potential changes that
    # could be applied.
    patches = {}

    # When a change is applied its original value needs to be stored so that
    # it can be replaced if another change needs to be tested.
    original_codes = {}
    patched_idx = None

    # Used to detect when the opcode substitution has hopelessly failed.
    patched = False

    acc = 0
    idx = 0

    def reset():
        nonlocal acc, idx, trace
        acc = 0
        idx = 0
        trace = []

    while idx < len(opcodes):

        op, code = opcodes[idx]

        # Recursed!
        if idx in trace:

            if patches and not patches:
                raise RuntimeError("failure :(")

            # Still have some experiments to run. Reset.
            elif patches:

                reset()

                # Replace the original opcode
                opcodes[patched_idx] = original_codes[patched_idx]

                # Swap in a new opcode to test
                patched_idx, sw_opcode = patches.popitem()
                opcodes[patched_idx] = sw_opcode
                continue

            # Set up experiments. Given that we have the full trace we know
            # that the problem must be in the instructions that have already
            # been executed. Check each and flip 'jmp <-> nop' and then restart
            # the program which knows to check 'patches'.
            else:

                # Indicate that 'patches' has been populated so that a
                # complete failure condition can be detected for R&D purposes.
                patched = True

                # 'patches' are applied to 'opcodes' with 'dict.popitem()',
                # which is a "last in first out" queue, so ensure to insert
                # in an appropriate order.
                for tr_idx in reversed(trace):
                    original_codes[tr_idx] = opcodes[tr_idx]
                    patch_op, patch_code = opcodes[tr_idx]
                    if patch_op == 'jmp':
                        patches[tr_idx] = ('nop', patch_code)
                    elif patch_op == 'nop':
                        patches[tr_idx] = ('jmp', patch_code)

                # Apply the first experiment
                patched_idx, sw_opcode = patches.popitem()
                original_codes[patched_idx] = opcodes[patched_idx]
                opcodes[patched_idx] = sw_opcode

                # Restart
                reset()
                continue

        # Execute the opcode
        newidx, acc = execute(idx, acc, op, code)
        trace.append(idx)
        idx = newidx

    else:
        return acc


data = parse_input()


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
