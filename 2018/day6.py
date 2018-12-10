# https://adventofcode.com/2018/day/6

from collections import defaultdict
from utils import get_input

data = get_input(6, 2018).strip()


def get_coordinates(data):
    points = []
    for line in data.splitlines():
        points.append(tuple([int(i) for i in line.split(', ')]))
    return points


def manhattan_distance(point1, point2):
    x1, x2 = point1[0], point2[0]
    y1, y2 = point1[1], point2[1]
    return abs(x2 - x1) + abs(y2 - y1)


def closest(x, y):
    best = points_coord[0]
    tie = False
    for point in points_coord:
        if manhattan_distance(point, (x, y)) < manhattan_distance(best, (x, y)):
            best = point
            tie = False
        elif manhattan_distance(point, (x, y)) == manhattan_distance(best, (x, y)):
            tie = True
    if tie:
        return (-1, -1)
    else:
        return best


def score_around(W=0):
    score = defaultdict(int)
    for x in range(min_x - W, max_x + 1 + W):
        for y in range(min_y - W, max_y + 1 + W):
            score[closest(x, y)] += 1
    return score


points_coord = get_coordinates(data)

min_x = min(points_coord, key=lambda x: x[0])[0]
max_x = max(points_coord, key=lambda x: x[0])[0]
min_y = min(points_coord, key=lambda x: x[1])[1]
max_y = max(points_coord, key=lambda x: x[1])[1]

score = score_around()
score2 = score_around(1)

result = [(score[k] if score[k] == score2[k] else 0, k) for k in score.keys()]
print(max(result, key=lambda x: x[0])[0])
