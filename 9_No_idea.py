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



# arr = 1 5 3
# a = 3 1
# b  = 5 7

# score = 0(2)
# arr [1 , 5 , 3]
# a = [3] yes +1
# a = [1] yes + 1
# b = [5] yes -1
# b = [7] no 
# score = (2-1) = 1


