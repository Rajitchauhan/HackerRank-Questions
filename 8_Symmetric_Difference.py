# https://www.hackerrank.com/challenges/symmetric-difference/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
a = set(map(int , input().split()))

n = int(input())
b = set(map(int , input().split()))

# res = []

# for i in a:
#     if i not in b:
#         res.append(i)

# for i in b:
#     if i not in a:
#         res.append(i)
        
# res.sort()
# for i in res:
#     print(i)

res = []
t = a.difference(b)
u = b.difference(a)
for i in t:
    res.append(i)

for i in u:
    res.append(i)
res.sort()

for i in res:
    print(i)


