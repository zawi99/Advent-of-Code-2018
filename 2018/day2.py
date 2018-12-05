# https://adventofcode.com/2018/day/2

from collections import Counter

from utils import get_input

data = get_input(2, 2018).splitlines()

two_letters = 0
three_letters = 0

for line in data:
    letter_counter = set(Counter(line).values())
    if 3 in letter_counter:
        three_letters += 1
    if 2 in letter_counter:
        two_letters += 1

checksum = two_letters * three_letters
print(f'Checksum is {checksum}')
