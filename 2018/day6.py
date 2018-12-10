# https://adventofcode.com/2018/day/6

import numpy as np

from utils import get_input

data = get_input(6, 2018).strip()


# data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""


def get_coordinates(data):
    points = []
    for line in data.splitlines():
        points.append(tuple([int(i) for i in line.split(', ')]))
    return points


def manhattan_distance(point1, point2):
    x1, x2 = point1[0], point2[0]
    y1, y2 = point1[1], point2[1]
    return abs(x2 - x1) + abs(y2 - y1)


points_coord = get_coordinates(data)

min_x = min(points_coord, key=lambda x: x[0])[0]
max_x = max(points_coord, key=lambda x: x[0])[0]
min_y = min(points_coord, key=lambda x: x[1])[1]
max_y = max(points_coord, key=lambda x: x[1])[1]

print(min_x, max_x, min_y, max_y)

results = np.zeros(len(points_coord), dtype=np.int)
infinite = set()

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distances = [manhattan_distance(point, (x, y)) for point in points_coord]
        min_distance = min(distances)

        if not distances.count(min_distance) > 1:
            results[distances.index(min_distance)] += 1

        if x == min_x or x == max_x or y == min_y or y == max_y:
            infinite.add(distances.index(min_distance))

results = np.delete(results, [inf for inf in infinite])
print(f'Part 1 result: {max(results)}')
