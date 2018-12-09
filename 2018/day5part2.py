# https://adventofcode.com/2018/day/5

import string
from collections import defaultdict
from utils import get_input

polymer = get_input(5, 2018).strip()


def units_match(a, b):
    """ Checks if units can react with each other """
    return a.lower() == b.lower() and (
            (a.isupper() and b.islower()) or (a.islower() and b.isupper())
    )


def react(polymer):
    C = defaultdict(list)
    for letter in string.ascii_lowercase:
        polymer_removed = polymer.replace(letter, '').replace(letter.upper(), '')
        for unit in polymer_removed:
            if C[letter] and units_match(unit, C[letter][-1]):
                C[letter].pop()
            else:
                C[letter].append(unit)
    return C


def maxarg(d):
    max_ = None
    for k, v in d.items():
        if max_ is None or len(v) < len(d[max_]):
            max_ = k
    return max_


C = react(polymer)
max_key = maxarg(C)
print(f'Part 2 result: {len(C[max_key])}')
