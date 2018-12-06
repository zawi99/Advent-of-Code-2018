# https://adventofcode.com/2018/day/3

from utils import get_input
from collections import defaultdict

# #40 @ 416,470: 24x11

data = get_input(3, 2018).splitlines()

C = defaultdict(int)

for line in data:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = words[3].split('x')
    w, h = int(w), int(h)
    doesnt_overlap = True
    for dx in range(w):  # go through all points of box
        for dy in range(h):
            C[(x + dx, y + dy)] += 1  # if any point is overlaps with another add 1

overlapped_squares = 0
for value in C.values():
    if value > 1:  # if true -> square belongs to at least two or more boxes == overlap
        overlapped_squares += 1

print(f'Part 1 result: {overlapped_squares}')

for line in data:
    words = line.split()
    id = words[0]
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = words[3].split('x')
    w, h = int(w), int(h)
    doesnt_overlap = True
    for dx in range(w):
        for dy in range(h):
            if C[(x + dx, y + dy)] != 1:
                doesnt_overlap = False

    if doesnt_overlap:
        print(f'Part 2 result: {id[1:]}')
