# https://adventofcode.com/2018/day/2#part2

from utils import get_input

data = get_input(2, 2018).splitlines()

for box1 in data:
    for box2 in data:
        diff = 0
        for idx, char in enumerate(box1):
            if char != box2[idx]:
                diff += 1

        if diff == 1:
            common_letters = [char for idx, char in enumerate(box1) if char == box2[idx]]
            print(''.join(common_letters))