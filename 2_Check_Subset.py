T = int(input())

for _ in range(T):
    i , A = int(input()) , set(map(int , input().split()))
    j, B = int(input()) , set(map(int , input().split()))
    # print(A.issubset(B)) pre-define function
    if(A<=B):
        print(True)
    else:
        print(False)

