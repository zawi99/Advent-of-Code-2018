# https://adventofcode.com/2018/day/4#part2

from utils import get_input

# [1518-03-05 23:57] Guard #2963 begins shift
# [1518-03-06 00:25] falls asleep
# [1518-03-06 00:46] wakes up

from collections import defaultdict

data = get_input(4, 2018).splitlines()
data.sort()

guards_sleep_time = defaultdict(int)
guards_sleep_time_minutes = defaultdict(int)

guard_id = None
falls_asleep_time = None

for line in data:
    time = int(line.split()[1][3:-1])  # minutes
    if 'begins shift' in line:
        guard_id = int(line.split()[3][1:])
        falls_asleep_time = None  # new guard begins shift so his sleep time is None
    elif 'falls asleep' in line:
        falls_asleep_time = time  # save the time when the particular guard fell asleep
    elif 'wakes up' in line:
        wakes_up_time = time
        for minute in range(falls_asleep_time, wakes_up_time):
            guards_sleep_time[guard_id] += 1  # how long the particular guard slept
            guards_sleep_time_minutes[(guard_id, minute)] += 1  # how many times guard slept in the particular minute


def max_key_by_value(dict):
    best = None
    for k, v in dict.items():
        if best is None or v > dict[best]:
            best = k
    return best


guard, minute = max_key_by_value(guards_sleep_time_minutes)
print(f'Part 2 result: {guard * minute}')
