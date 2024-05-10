# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr=map(int, input().split())
A=set(map(int, input().split()))
B=set(map(int, input().split()))
score = 0

for i in arr:
    if i in A:
        score += 1
    if i in B:
        score -= 1
        
print(score)
