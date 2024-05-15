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


