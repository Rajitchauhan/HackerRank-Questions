def merge_the_tools(s , k):
    res = ""
    n = len(s)
    for i in range(0 , n ,  k):
        seen = set()
        st  = s[i:i+k]
        for c in st:
            if c not in seen:
                seen.add(c)
                res += c
        res +=  "\n"
    print(res)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3

# len = 9
# len/k = 9/3 = 3
# AB
# CA 
# AD
# Sample Output
# AB
# CA
# AD


# st = aab
# caa 
# ada 

# trick  : 
#     seen = set()
#     st = a d a
#     if 'a' not in seen:
#         seen(a , d)
#         res += ''
#     res += '\n'

# i/p : n a m a n
# 12321

