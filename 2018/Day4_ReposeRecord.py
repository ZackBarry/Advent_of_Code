import re
import sys
import operator

# open the data
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\2018\Input_Day4.txt')
Input = InputFile.read()
# strip() removes whitespace at the start and end of file
Input = Input.strip()
data = Input.split('\n')

# -------------------------------------------------------------------------
# Task 1: Find the guard that has the most minutes asleep. What minute does
#         that guard spend asleep the most? Note that your entries are in
#         the order you found them. You'll need to organize them before
#         they can be analyzed.  What is the ID of the guard multiplied by
#         the minute you chose?
# -------------------------------------------------------------------------

# data can be sorted based on normal string comparison
data = sorted(data)

# regular expressions to extract id and sleep start/end

guard_id = re.compile(r'Guard #(\d+)')
sleep_time = re.compile(r'\d\d:(\d\d)')

# dict for storing ids : total sleep length

SleepInfo = {}

on_duty = 0
dozes = 0
wakes = 0

for event in data:
    if 'Guard' in event:
        # update the value of on_duty
        on_duty = int(guard_id.search(event).groups()[0])
    elif 'falls asleep' in event:
        # start the timer for sleep length
        dozes = int(sleep_time.search(event).groups()[0])
    elif 'wakes up' in event:
        # calculate sleep length and add to appropriate guard_id
        wakes = int(sleep_time.search(event).groups()[0])
        length = wakes - dozes
        SleepInfo.setdefault(on_duty, 0)
        SleepInfo[on_duty] += length

# get the heaviest sleeper's id

max_id = -1
max_length = -1

for key, value in SleepInfo.items():
    if value > max_length:
        max_id = key
        max_length = value

# create a dict, time : # days slept then, to find most often slept time

TimeInfo = {}

for event in data:
    if 'Guard' in event:
        on_duty = int(guard_id.search(event).groups()[0])
    elif 'falls asleep' in event:
        dozes = int(sleep_time.search(event).groups()[0])
    elif 'wakes up' in event:
        wakes = int(sleep_time.search(event).groups()[0])
        if on_duty == max_id:
            for i in range(dozes, wakes):
                TimeInfo.setdefault(i, 0)
                TimeInfo[i] += 1

# determine the time the guard slept during the most

max_time = -1
frequency = -1

for key, value in TimeInfo.items():
    if value > frequency:
        max_time = key
        frequency = value

# find the product of the ID and the most slept time

solution1 = max_id * max_time

print("Task 1: The product of the ID and the sleep time is " + str(solution1) + ".")

# -------------------------------------------------------------------------
# Task 2: Find the guard that is most frequently asleep on the same minute.
#         Calculate the product of their ID and the minute.
# -------------------------------------------------------------------------

SleepInfo = {}

on_duty = 0
dozes = 0
wakes = 0

for event in data:
    if 'Guard' in event:
        # update the value of on_duty
        on_duty = int(guard_id.search(event).groups()[0])
    elif 'falls asleep' in event:
        # start the timer for sleep length
        dozes = int(sleep_time.search(event).groups()[0])
    elif 'wakes up' in event:
        # calculate sleep length and add to appropriate guard_id
        wakes = int(sleep_time.search(event).groups()[0])
        length = wakes - dozes
        SleepInfo.setdefault(on_duty, {})
        for i in range(dozes, wakes):
            SleepInfo[on_duty].setdefault(i, 0)
            SleepInfo[on_duty][i] += 1

most_frequent_id = -1
most_frequent_time = -1
most_frequency = -1

for guard, time_info in SleepInfo.items():
    current_most_time = -1
    current_frequency = -1
    for minute, frequency in time_info.items():
        if frequency > current_frequency:
            current_most_time = minute
            current_frequency = frequency
    if current_frequency > most_frequency:
        most_frequency = current_frequency
        most_frequent_time = current_most_time
        most_frequent_id = guard

solution2 = most_frequent_id * most_frequent_time

print("Task 2: The product of the ID and the sleep time is " + str(solution2) + ".")
