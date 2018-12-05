import sys

def get_input(day, year):
    try:
        with open(f'../{year}/inputs/day{day}_input.txt') as file:
            data = file.read()
    except FileNotFoundError:
        print(f'Failed to load {year}/inputs/day{day}_input.txt')
        sys.exit()
    return data
