# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
score = list(map(int  , input().split()))
max = max(score)
runner_up = -10e7

for s in score:
    if runner_up < s < max:
        runner_up = s 
print(runner_up)