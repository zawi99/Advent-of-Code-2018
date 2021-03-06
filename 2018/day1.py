# https://adventofcode.com/2018/day/1

from utils import get_input

data = get_input(1, 2018)
inp = list(map(int, data.splitlines()))
print(f'Frequency is {sum(inp)}')

frequency = 0
frequency_set = set()
frequency_reached_twice = False

while (not frequency_reached_twice):
    for freq in inp:
        frequency += freq
        if frequency in frequency_set:
            frequency_reached_twice = True
            print(f'First frequency reached twice is: {frequency}')
            break
        else:
            frequency_set.add(frequency)