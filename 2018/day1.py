# https://adventofcode.com/2018/day/1

from utils import get_input

data = get_input(1, 2018)
inp = list(map(int, data.splitlines()))
print(f'Frequency is {sum(inp)}')
