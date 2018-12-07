# https://adventofcode.com/2018/day/5

from utils import get_input

polymer = get_input(5, 2018).strip()


def units_match(a, b):
    """ Checks if units can react with each other """
    return a.lower() == b.lower() and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))


def react(polymer):
    stack = []
    for unit in polymer:
        if stack and units_match(unit, stack[-1]):
            stack.pop()
        else:
            stack.append(unit)
    return stack


print(f'Part 1 result: {len(react(polymer))}')
