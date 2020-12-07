import re


def load_input():

    """Parse input data into a friendly format."""

    out = []
    with open('04.txt') as f:

        record = {}
        while True:

            try:
                line = next(f).strip()
            except StopIteration:
                break

            if not line:
                out.append(record)
                record = {}
                continue

            for item in line.split():
                k, v = item.split(':')
                record[k] = v

    # Could still have a pending record
    if record:
        out.append(record)

    return tuple(filter(None, out))


def part1(passports):

    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

    valid = 0
    for passport in passports:
        missing = fields - passport.keys()
        if not missing or missing == {'cid'}:
            valid += 1

    return valid


def part2(passports):

    ecl_values = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    hcl_re = re.compile(r"^\#[a-z0-9]{6}$")
    pid_re = re.compile(r"^[0-9]{9}$")

    valid = 0
    for passport in passports:

        # Birth year
        if not 1920 <= int(passport.get('byr', -1)) <= 2002:
            continue

        # Issue year
        if not 2010 <= int(passport.get('iyr', -1)) <= 2020:
            continue

        # Expiration year
        if not 2020 <= int(passport.get('eyr', -1)) <= 2030:
            continue

        # Height
        hgt = passport.get('hgt', '')
        if 'in' not in hgt and 'cm' not in hgt:
            continue
        elif 'cm' in hgt and not 150 <= int(hgt.rstrip('cm')) <= 193:
            continue
        elif 'in' in hgt and not 59 <= int(hgt.rstrip('in')) <= 76:
            continue

        # Hair color
        if not re.match(hcl_re, passport.get('hcl', '')):
            continue

        # Eye color
        if passport.get('ecl', None) not in ecl_values:
            continue

        # Passport ID
        if not re.match(pid_re, passport.get('pid', '')):
            continue

        # All validations passed
        valid += 1

    return valid


data = load_input()

print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
