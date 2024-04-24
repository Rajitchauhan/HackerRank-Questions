# link : https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import defaultdict

n = int(input())
rooms = list(map(int, input().split()))

dt = defaultdict(int)  # Specify int as the default value type

for r in rooms:
    dt[r] += 1  # Increment the count for room number r

# print(dt) defaultdict(<class 'int'>, {1: 5, 2: 5, 3: 5, 6: 5, 5: 5, 4: 5, 8: 1})

for key in dt.keys():
    if dt[key] == 1:
        print(key)
        break




